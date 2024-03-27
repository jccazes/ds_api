from utils.db.load import load_users_db, _load_admin_db

users_db = load_users_db()
_admin_db = _load_admin_db()

def auth_user(auth: str):
    extracted_user, extracted_password = tuple(auth.split(':'))
    try: 
        users_db[extracted_user] == extracted_password
        return auth
    except:
        return None

def _is_admin(auth: str):
    extracted_user, extracted_password = tuple(auth.split(':'))
    try: 
        _admin_db[extracted_user] == extracted_password
        return True
    except:
        return False