from fastapi import FastAPI
import uvicorn
from load import load_db

app = FastAPI()

@app.get('/')
def get_index():
    return {'data': db['question'][0]}

if __name__ == "__main__":
    db = load_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)