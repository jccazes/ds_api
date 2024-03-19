from fastapi import FastAPI
from fastapi import Header
import uvicorn
from load import load_db, load_users_db
from typing import Optional
from auth import auth_user


app = FastAPI()

@app.get('/')
def get_index():
    return {'data': db['question'][0]}

@app.get('/authorization')
def check_user(auth: Optional[str] = Header(None, description='user:password format')):
    auth_status = auth_user(auth, users_db)
    if auth_status == 'auth':
        return 'Authorized'
    elif auth_status == 'not_auth':
        return 'Not Authorized'
    else:
        return f'{auth} invalid format, check above for more details'
    

if __name__ == "__main__":
    db = load_db()
    users_db = load_users_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)