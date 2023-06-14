from dbhelpers import run_statement
from dbcreds.py import production_mode
from apihelpers import check_data
from flask import Flask, request, make_response, jsonify
app = Flask(__name__)
@app.get('')
def new_function():
    return
if(production_mode == True):
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
    CORS(app)
