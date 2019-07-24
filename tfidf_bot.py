# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import operator ,os
from sklearn.feature_extraction.text import TfidfVectorizer

filepath = 'final.csv'


def bot_engine(query= ''):
    
    resp = ""
    #print (os.getcwd())
    csv_reader = pd.read_csv(filepath)
    
    question_list = csv_reader[csv_reader.columns[0]].values.tolist()
    #print(question_list)
    answers_list  = csv_reader[csv_reader.columns[1]].values.tolist()
    #print(answers_list)
    
    
    vectorizer = TfidfVectorizer(min_df=0, ngram_range=(2, 4), 
                                 strip_accents='unicode',
                                 norm='l2' , 
                                 encoding='ISO-8859-1')
    
    X_train = vectorizer.fit_transform(np.array([''.join(que) for que in question_list]))
    
    X_query=vectorizer.transform([query])
    
    XX_similarity=np.dot(X_train.todense(), X_query.transpose().todense())
    #print(XX_similarity)

    XX_sim_scores= np.array(XX_similarity).flatten().tolist()
    #print(XX_sim_scores)
    
    
    dict_sim= dict(enumerate(XX_sim_scores))
    #print(dict_sim)
    
    sorted_dict_sim = sorted(dict_sim.items(), key=operator.itemgetter(1), reverse =True)
    #print(sorted_dict_sim)
    
    
    if sorted_dict_sim[0][1]==0:
        #print("Sorry I am not aut, please try asking again in a nicer way :)")
        resp = "Sorry I am not authorized by Deep to answer this"
    
    elif sorted_dict_sim[0][1]>0:
        #print (answers_list [sorted_dict_sim[0][0]])      
        resp = answers_list [sorted_dict_sim[0][0]]

    return resp


		
		
	
	

