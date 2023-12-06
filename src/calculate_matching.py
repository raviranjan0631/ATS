def get_matching_score(score, weightage_score):
    '''method to calculate weighted score with respect to feature'''
    total = 0
    for i in range(len(score)):
        total += score[i] * weightage_score[i]

    return total / sum(weightage_score)


