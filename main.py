from fastapi import FastAPI
from fastapi import Header
import uvicorn
from load import load_db, load_users_db
from typing import Optional


app = FastAPI()

@app.get('/')
def get_index():
    return {'data': db['question'][0]}

@app.get('/authorization')
def check_user(auth: Optional[str] = Header(None, description='user:password format')):
    if ':' in auth:
        extracted_user, extracted_password = tuple(auth.split(':'))
        try: 
            if users_db[extracted_user] == extracted_password:
                return 'Authorized'
            else:
                return 'Not authorized'
        except:
            return 'Not authorized'
    else:
        return f'{auth} invalid format, please provide auth in the following format: User:Password'

if __name__ == "__main__":
    db = load_db()
    users_db = load_users_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)