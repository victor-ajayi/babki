from flask import Response, jsonify, request
from flask_api import status
from sqlalchemy import exc
from werkzeug.security import generate_password_hash

from app.api import bp as api
from app.extensions import db
from app.models import *


@api.route("/")
def index():
    return "This is the main blueprint"


@api.post("/user")
def create_user():
    """Create User"""

    data = request.json

    # Create password hash and update data object
    password_hash = generate_password_hash(data["password"])
    data = {"username": data["username"], "password_hash": password_hash}

    new_user = User(**data)
    try:
        db.session.add(new_user)
        db.session.commit()
    except (exc.DBAPIError, exc.InvalidRequestError) as e:
        return {"message": f"An <{e}> error occured"}, status.HTTP_400_BAD_REQUEST

    db.session.refresh(new_user)

    return {"data": "User created successfully"}, status.HTTP_201_CREATED


@api.get("/user/<id>")
def get_user(id):
    """Get single user"""

    user = User.query.filter(User.id == id).first_or_404()

    data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "cash": user.cash,
        "savings": user.savings,
        "debt": user.debt,
        "loans": user.loans,
        "created_at": user.created_at,
    }

    return jsonify(data), status.HTTP_200_OK


@api.get("/users")
def get_users():
    """Get all users"""

    users = User.query.all()
    response = [{"id": user.id, "username": user.username} for user in users]

    return jsonify(response), status.HTTP_200_OK
