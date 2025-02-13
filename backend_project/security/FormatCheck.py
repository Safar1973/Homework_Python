# security/FormatCheck.py

class FormatCheck:
    @staticmethod
    def validate_username(username):
        # Einfache Validierung: Mindestens 3 Zeichen
        return len(username) >= 3

    @staticmethod
    def validate_password(password):
        # Einfache Validierung: Mindestens 6 Zeichen
        return len(password) >= 6
