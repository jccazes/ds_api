from pydantic import BaseModel
from typing import Optional
    
class Quizz(BaseModel):
    question: str
    subject: str
    correct: str
    use: str
    reponseA: str
    reponseB: str
    reponseC: str
    reponseD: Optional[str]