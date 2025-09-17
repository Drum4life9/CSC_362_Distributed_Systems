import json
import jwt
from flask import Flask, request, make_response
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        token = jwt.encode({'user': 'alice',
                            'authorities': ["inventory:admin", "payroll:admin"]},
                            'SUPER_SECRET_APP_KEY', algorithm="HS256")

        response = make_response()
        response.set_cookie('jwt_token', token)
        response.set_data(token)
        
        return response
    return None

if __name__ == '__main__':
    app.run(debug=True)