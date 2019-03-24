from flask import Flask, render_template

app=Flask(__name__) # instantiate Flask object

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")
    
if __name__=="__main__":
    app.run(debug=True)

'''
CASE 1 - Script executed
     __name__=="__main__"

CASE 2 - Script imported
     __name__=="script1"
'''