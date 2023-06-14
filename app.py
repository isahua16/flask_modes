from dbhelpers import run_statement
from dbcreds import production_mode
from apihelpers import check_data
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.post('/api/painting')
def new_painting():
    error = check_data(request.json, ['artist', 'year', 'title', 'image_url'])
    if (error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call new_painting(?,?,?,?)', [request.json.get('artist'), request.json.get('year'), request.json.get('title'), request.json.get('image_url')])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)

@app.get('/api/painting')
def get_paintings ():
    results = run_statement('call get_paintings(?)')
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)

if(production_mode == True):
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
    
