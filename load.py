import pandas as pd
from typing import Optional

def load_db(path: Optional[str] = None) -> pd.DataFrame:
    if path:
        db = pd.read_csv(path)
    else:
        db = pd.read_csv('db/questions.csv')
        
    return(db)

if __name__ == '__main__':
    db = load_db()
