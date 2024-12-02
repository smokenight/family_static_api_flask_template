import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructure import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure('Jackson')

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member: 
        return jsonify(member), 200
    else:
        return jsonify({"Message": "Member doesn't exist"}), 404

@app.route('/members', methods = ['POST'])
def add_member():
    member = request.json
    #member = request.get_json()

    if not member:
        return jsonify({"Message": "Error"}), 400
    jackson_family.add_member(member)
    return jsonify({"Message": "Member added successfully"}), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    print(member)
    if not member:
        return jsonify({"Message": "Error"}), 400
    #return jsonify({"message": "Member deleted successfully"}), 200
    return jsonify({"done": True}), 200

@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

# Activado modo debug para auto reloading o hot reloading
#app.run(host='0.0.0.0', debug=True)
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)