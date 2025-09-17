from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {}
user_id_counter = 1


#  Create User
@app.route("/users", methods=["POST"])
def create_user():
    global user_id_counter
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email required"}), 400

    user = {"id": user_id_counter, "name": data["name"], "email": data["email"]}
    users[user_id_counter] = user
    user_id_counter += 1
    return jsonify(user), 201


#  Get All Users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200


#  Get User by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


#  Update User
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200


#  Delete User
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
