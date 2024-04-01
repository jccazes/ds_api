from fastapi import FastAPI
from fastapi import Header
import uvicorn
from utils.sample import sample_questions, _update_questions_db
from typing import Annotated, Union
from utils.auth import auth_user, _is_admin
from utils.schemas import Quizz
from pydantic import StringConstraints

app = FastAPI()

@app.get('/')
def get_index():
    return {'status': 'Service is up'}

@app.get('/authorization')
async def read_items(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()] = None) -> dict:
    if header:
        if auth_user(header) or _is_admin(header):
            return {"User-Login-Header": 'authorized'}
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}        
    
@app.get('/question')
async def get_questionnaire(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()] = None, 
                            n_samples: int = 10, use: str = 'Total Bootcamp', 
                            subject: Annotated[str, StringConstraints(pattern='^[\w\s]*(?:,\s*[\w\s]+)*$')] = 'Machine Learning, Data Science') -> Union[list[Quizz],dict]:
    if header:
        if auth_user(header) or _is_admin(header):
            sampled_questions = sample_questions(n_samples, use, subject)
            if sampled_questions:
                return sampled_questions
            else:
                return  {"Query-Parameters-Error": 'no_data'}   
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}   
    
@app.post('/add_question')
async def add_question(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()] = None, quizz: Quizz = None) -> dict:
    if header:
        if _is_admin(header):
            _update_questions_db(quizz)
            return {"User-Login-Header": 'quizz updated'}   
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}   
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)