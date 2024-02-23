from flask import Flask, jsonify, request
from linkedin.linkedinProfile import linkedinProfile

app = Flask(__name__)

# Route to get all items
@app.route('/api', methods=['GET'])
def get_response():
    type = request.args.get('type')
    if type == 'LINKEDIN':
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        currentOrg = request.args.get('currentOrg')
        return jsonify(linkedinProfile.getProfile(username, currentOrg, email, password))
    elif type == 'INSTAGRAM':
        return jsonify('in progress')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    #app.run(debug=True)
