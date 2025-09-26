from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, auth

# Create Flask app
app = Flask(__name__)

cred = credentials.Certificate(r"C:\Users\HP\save file\sample\key.json") 
firebase_admin.initialize_app(cred)

# Middleware to verify token
def verify_token(func):
    def wrapper(*args, **kwargs):
        id_token = request.headers.get("Authorization")
        if not id_token:
            return jsonify({"success": False, "error": "Missing Authorization Header"}), 401

        try:
            decoded_token = auth.verify_id_token(id_token)
            request.user = decoded_token
        except Exception as e:
            return jsonify({"success": False, "error": str(e)}), 401

        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route("/profile")
@verify_token
def profile():
    user = request.user
    return jsonify({
        "success": True,
        "message": "You are authenticated (anonymous or not)!",
        "user": user
    })

if __name__ == "__main__":
    app.run(debug=True)
