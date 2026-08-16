# routes/auth.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/api")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    # logic here
    return jsonify({"message": "register endpoint"}), 200


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    # logic here
    return jsonify({"message": "login endpoint"}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    # logic here
    return jsonify({"message": "logout endpoint"}), 200