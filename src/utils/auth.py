def auth_user(auth: str, loaded_user_db):
    if ':' in auth:
        extracted_user, extracted_password = tuple(auth.split(':'))
        try: 
            if loaded_user_db[extracted_user] == extracted_password:
                return 'auth'
            else:
                return 'not_auth'
        except:
            return 'not_auth'
    else:
        return 'invalid'