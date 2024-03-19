from fastapi import FastAPI
from fastapi import Header
import uvicorn
from load import load_db, load_users_db


app = FastAPI()

@app.get('/')
def get_index():
    return {'data': db['question'][0]}

@app.get('/authorization')
def get_headers(auth=Header(None)):
    if ':' in auth:
        extracted_user, extracted_password = tuple(auth.split(':'))
        if users_db[extracted_user] == extracted_password:
            return 'authorized'
        else:
            return 'Not authorized'
    else:
        return f'{auth} invalid format'

if __name__ == "__main__":
    db = load_db()
    users_db = load_users_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)