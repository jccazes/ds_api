import pandas as pd 
from random import sample

def sample_questions(df_questions,nb_questions: int):
    sample_index = sample(df_questions.index.to_list(), nb_questions)
    
    sampled_df = df_questions.iloc[sample_index][['question','responseA','responseB','responseC','responseD','correct']]
    sampled_json = sampled_df.apply(lambda x: x.to_json(), axis=1).to_list()
    
    return(sampled_json)