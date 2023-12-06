from sentence_transformers import SentenceTransformer, util
import torch 
import pandas as pd
model = SentenceTransformer('models')



def get_multiple_matching(jd_data, resume_data, column_name):
    '''this method take two list as a input one for job description and one for resume'''
    # convert the Job description skill into embedding
    jd_embedding = model.encode(jd_data, convert_to_tensor=True)


    multiple_matching = dict()
    multiple_matching['jd_' + column_name] = []
    multiple_matching['resume_' + column_name] = []
    multiple_matching['matching_score'] = []

    # finding the most relevant skill in the resume with respect to JD skill
    count = 0
    for embeding in jd_embedding:
        # creating embeddings 
        resume_embedding = model.encode(resume_data, convert_to_tensor=True) 
        # calculating cosine similarity   
        cos_scores = util.cos_sim(embeding, resume_embedding)[0]
        top_results = torch.topk(cos_scores, k=1)
        score = top_results[0].numpy()[0]
        index = top_results[1].numpy()[0]
        
        multiple_matching['jd_' + column_name].append(jd_data[count])
        multiple_matching['resume_' + column_name].append(resume_data[index])
        multiple_matching['matching_score'].append(float(score))
        resume_data.remove(resume_data[index])
        count += 1
        
    multiple_matching = pd.DataFrame(multiple_matching)

    return multiple_matching


def get_similarity_text(jd, resume):
    '''finding similarity between two texts'''
    # creating embeddings 
    jd_embedding = model.encode(jd, convert_to_tensor=True)    
    resume_embedding = model.encode(resume, convert_to_tensor=True)   
    
    # calculating cosine similarity
    cos_scores = util.cos_sim(jd_embedding, resume_embedding)[0]
    top_results = torch.topk(cos_scores, k=1)
    score = top_results[0].numpy()[0]
    
    return score


def get_similar_score(dataframe, score):
    '''Perform filter in dataframe with respect to dataframe'''
    df = dataframe[dataframe['matching_score']>= score]

    return df