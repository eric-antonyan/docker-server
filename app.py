from flask import Flask, make_response, jsonify
import os

app = Flask(__name__)

SERVICE_NAME = os.environ.get("SERVICE_NAME", "application")


@app.route("/hello/<user>")
def say_hello(user: str):
    return make_response(jsonify({"message": f"Hi from {SERVICE_NAME}, {user}!"}), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
