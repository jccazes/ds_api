from fastapi import FastAPI
from fastapi import Header, Depends
import uvicorn
from utils.db.load import load_questions_db, load_users_db
from utils.sample import sample_questions
from typing import Optional, Annotated
from utils.auth import auth_user
from utils.schemas import Quizz
from pydantic import BaseModel, StringConstraints
from typing import Union



app = FastAPI()

@app.get('/')
def get_index():
    return {'status': 'Service is up'}

@app.get('/authorization')
async def read_items(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()]  = None):
    if header:
        if auth_user(header):
            return {"User-Login-Header": 'authorized'}
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}        
    
@app.get('/question')
async def get_questionnaire(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()]  = None, n_samples:int = 10):
    if header:
        if auth_user(header):
            sampled_questions = sample_questions(questions_db,n_samples)
            return sampled_questions
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}   
    
if __name__ == "__main__":
    questions_db = load_questions_db()
    users_db = load_users_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)