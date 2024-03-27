from fastapi import FastAPI
from fastapi import Header
import uvicorn
from utils.sample import sample_questions
from typing import Annotated, Union
from utils.auth import auth_user
from utils.schemas import Quizz
from pydantic import StringConstraints

app = FastAPI()

@app.get('/')
def get_index():
    return {'status': 'Service is up'}

@app.get('/authorization')
async def read_items(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()] = None) -> dict:
    if header:
        if auth_user(header):
            return {"User-Login-Header": 'authorized'}
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}        
    
@app.get('/question')
async def get_questionnaire(header: Annotated[str, StringConstraints(pattern='\w*:\w*'), Header()] = None, n_samples: int = 10) -> Union[list[Quizz],dict]:
    if header:
        if auth_user(header):
            sampled_questions = sample_questions(n_samples)
            return sampled_questions
        else:
            return {"User-Login-Header": 'not_authorized'}   
    else:
        return {"User-Login-Header": 'not_authorized'}   
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)