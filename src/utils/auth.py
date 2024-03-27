from utils.db.load import load_users_db

users_db = load_users_db()

def auth_user(auth: str):
    extracted_user, extracted_password = tuple(auth.split(':'))
    try: 
        users_db[extracted_user] == extracted_password
        return auth
    except:
        return None