from flask import Flask, jsonify, request, render_template
from c_utils import script_path, from_json
from difflib import get_close_matches
import json

app = Flask(__name__)

data = from_json('{}/data.json'.format(script_path))

@app.route("/")
def homepage():
    return render_template('home.html')


@app.route("/translate")
def translate():
    query = request.args.get('q')
    query = query.lower()
    if query in data:
        return render_template('home.html', content = data[query])
    elif query.title() in data:
        return render_template('home.html', content = data[query.title()])
    elif query.upper() in data:
        return render_template('home.html', content = data[query.upper()])
    elif len(get_close_matches(query, data.keys())) > 0:
        lst = []
        lst.append("Did you mean %s instead?" % get_close_matches(query, data.keys())[0])
        return render_template('home.html', content = lst)
    #     if yn == "Y":
    #         return data[get_close_matches(query, data.keys())[0]]
    #     elif yn == "N":
    #         return "The word doesn't exist. Please double check it."
    #     else:
    #         return "We didn't understand your entry."
    # else:
    #     return "The word doesn't exist. Please double check it."

        




# word = input("Enter word: ")

# output = translate(word)
# if type(output) == list:
#     for item in output:
#         print(item)
# else:
#     print(output)

app.run(port=4997, debug=True)