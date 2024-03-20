import pandas as pd
from typing import Optional
from db.users_db import users_db

def load_questions_db(path: Optional[str] = None) -> pd.DataFrame:
    if path:
        db = pd.read_csv(path)
    else:
        db = pd.read_csv('db/questions.csv')
        
    return(db)

def load_users_db() -> dict:
    return(users_db)

if __name__ == '__main__':
    db = load_questions_db()
    users_db = load_users_db()
