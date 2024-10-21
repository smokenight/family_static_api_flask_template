from flask import Flask, request, jsonify
from datastructure import FamilyStructure

app = Flask(__name__)
jackson_family = FamilyStructure('Jackson')

@app.route('/')
def hello():
    return 'API SERVER IS UP!!'

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

# Activado modo debug para auto reloading o hot reloading
app.run(host='0.0.0.0', debug=True)