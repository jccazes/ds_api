import pandas as pd
from typing import Optional
import json

def load_questions_db(path: Optional[str] = None) -> pd.DataFrame:
    if path:
        db = pd.read_csv(path)
    else:
        db = pd.read_csv('src/utils/db/questions.csv')
        
    for col in db.columns:
        db[col] = db[col].apply(lambda x: str(x))
    return(db)

def load_users_db() -> dict:
    return(json.load(open('src/utils/db/users_db.txt')))

def _load_admin_db() -> dict:
    return(json.load(open('src/utils/db/.secret.txt')))

if __name__ == '__main__':
    db = load_questions_db()
    users_db = load_users_db()
    _admin_db = _load_admin_db()