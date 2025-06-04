from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)





if __name__ == "__main__":
    app.run(debug=True)


@app.route("/users", methods=["GET"])
def hack_1():
    return {'payload':'success'}


@app.route("/user", methods=["POST"])
def hack_2():
    return {'payload':'success'}


@app.route("/user", methods=["DELETE"])
def hack_3():
    return {'payload':'success'}

#No sirve
@app.route("/user", methods=["PUT"])
def hack_4():
    return {'payload':'success'}


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