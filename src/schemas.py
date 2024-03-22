from pydantic import BaseModel
from typing import Optional

class user_login(BaseModel):
    username_password: str
    
    
class quizz(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    reponseA: str
    reponseB: str
    reponseC: str
    reponseD: Optional[str]
