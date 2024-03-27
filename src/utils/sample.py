import pandas as pd 
from random import sample
from utils.db.load import load_questions_db
from utils.schemas import Quizz

df_questions = load_questions_db()

def sample_questions(nb_questions: int):
    sample_index = sample(df_questions.index.to_list(), nb_questions)
    
    sampled_df = df_questions.iloc[sample_index][['question','responseA','responseB','responseC','responseD','correct','subject','use']]
    
    result_list = []
    for row in range(len(sampled_df)):
        row_data = sampled_df.iloc[row]
        quizz = Quizz(question=row_data['question'], subject= row_data['subject'], use = row_data['use'], 
                    reponseA=row_data['responseA'], reponseB=row_data['responseB'], reponseC=row_data['responseC'], 
                    reponseD=row_data['responseD'], correct=row_data['correct'])
        result_list.append(quizz)

    
    return(result_list)