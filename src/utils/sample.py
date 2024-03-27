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

def _update_questions_db(quizz: Quizz | None):
    global df_questions
    if quizz:
        data = {'question': quizz.question, 'subject': quizz.subject, 'use': quizz.use, 
                'responseA': quizz.reponseA, 'responseB': quizz.reponseB, 'responseC': quizz.reponseC, 
                'responseD': quizz.reponseD, 'correct': quizz.correct}
        df_questions = pd.concat([df_questions, pd.DataFrame([data])], ignore_index=True)
        
        
        return None
    else:
        return None