from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)





if __name__ == "__main__":
    app.run(debug=True)

#Hack 1
@app.route("/users", methods=["GET"])
def hack_1():
    return {'payload':'success'}


#Hack 2
@app.route("/user", methods=["POST"])
def hack_2():
    return {'payload':'success'}


#Hack 3
@app.route("/user", methods=["DELETE"])
def hack_3():
    return {'payload':'success'}

#Hack 4
@app.route("/user", methods=["PUT"])
def hack_4():
    return {'payload':'success', 'error':False}

#Hack 5
@app.route("/api/v1/users", methods=["GET"])
def hack_5():
    return {'payload':[]}


#Hack 6
@app.route("/api/v1/user", methods=["POST"])
def hack_6():
    email = request.args.get("email")
    name = request.args.get("name")
    payload = {
        "email":email,
        "name": name
    }
    return jsonify({"payload":payload})

#Hack 7
@app.route("/api/v1/user/add", methods=["POST"])
def hack_7():
    email = request.form.get("email")
    name = request.form.get("name")
    id = request.form.get("id")
    payload = {
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    }
    return jsonify(payload)


#Hack 8
@app.route("/api/v1/user/create", methods=["POST"])
def hack_8():
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    id = data.get("id")
    payload = {
        'payload': {
            'email':email,
            'name':name,
            'id':id,
        }
    }
    return jsonify(payload)
