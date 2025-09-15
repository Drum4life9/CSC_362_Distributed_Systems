import json
import jwt
from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        token = jwt.encode({'user': 'Bubba', 'exp': datetime.now(timezone.utc) + timedelta(hours=1),
                            'db_roles': {'inventory': 'admin', 'payroll': 'read_only'}},
                           'SUPER_SECRET_APP_KEY', algorithm="HS256")

        response = make_response()
        response.set_cookie('jwt_token', token)
        response.set_data(token)
        
        return response
    return None

if __name__ == '__main__':
    app.run(debug=True)