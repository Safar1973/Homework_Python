# security/JWTManger.py

import jwt
import datetime

class JWTManger:
    SECRET_KEY = "your_secret_key"  # Ersetze dies durch einen sicheren Schlüssel

    @staticmethod
    def generate_token(username):
        payload = {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, JWTManger.SECRET_KEY, algorithm="HS256")
        return token
