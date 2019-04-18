from flask import Flask, render_template, redirect, session, redirect, request, url_for, Response, send_file
import adal
import uuid
import requests
import json
import config

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

PORT = 5000  
AUTHORITY_URL = config.AUTHORITY_HOST_URL + '/' + config.TENANT
REDIRECT_URI = 'http://localhost:{}/getAToken'.format(PORT)
TEMPLATE_AUTHZ_URL = ('https://login.microsoftonline.com/{}/oauth2/authorize?' +
                      'response_type=code&client_id={}&redirect_uri={}&' +
                      'state={}&resource={}')

graph_data = ""

@app.route("/")
def homepage():
    return render_template('home.html')

@app.route("/login")
def login():
    auth_state = str(uuid.uuid4())
    session['state'] = auth_state
    authorization_url = TEMPLATE_AUTHZ_URL.format(
        config.TENANT,
        config.CLIENT_ID,
        REDIRECT_URI,
        auth_state,
        config.RESOURCE)
    resp = Response(status=307)
    resp.headers['location'] = authorization_url
    return resp


@app.route("/getAToken")
def main_logic():
    code = request.args['code']
    state = request.args['state']
    if state != session['state']:
        raise ValueError("State does not match")
    auth_context = adal.AuthenticationContext(AUTHORITY_URL)
    token_response = auth_context.acquire_token_with_authorization_code(code, REDIRECT_URI, config.RESOURCE,
                                                                        config.CLIENT_ID, config.CLIENT_SECRET)
    session['access_token'] = token_response['accessToken']

    return redirect('/')


@app.route('/devices')
def graphcall():
    global graph_data
    if 'access_token' not in session:
        return redirect(url_for('login'))
    endpoint = config.RESOURCE + '/' + config.API_VERSION + '/deviceManagement/managedDevices/'
    http_headers = {'Authorization': 'Bearer ' + session.get('access_token'),
                    'User-Agent': 'adal-python-sample',
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'client-request-id': str(uuid.uuid4())}
    graph_data = requests.get(endpoint, headers=http_headers, stream=False).json()
    with open('output/devices.json', 'w') as f:
        json.dump(graph_data, f)
    # # Print JSON
    # graph_data_dict = [{"DeviceName": data["deviceName"], 'UPN':data["userPrincipalName"]} for data in graph_data['value']]
    # print(graph_data_dict)

    # Pass data to browser
    graph_data_parsed = [data for data in graph_data['value']]
    return render_template('devices.html', graph_data=graph_data_parsed)

@app.route("/getDevicesJSON")
def getDevicesJSON():

    with open("output/devices.json") as fp:
        devices = fp.read()

    return Response(
        devices,
        mimetype="application/json",
        headers={"Content-disposition":
                 "attachment; filename=devices.json"})
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('homepage'))
    
if __name__ == "__main__":
    app.run(port=5000)

