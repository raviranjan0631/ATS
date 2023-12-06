

def get_job_position_jd (jd):
    ''' prompt to find position from the job description '''
    position_jd = """
    1. what is the position mention in the Job description given below
    About the job in short, if you can't find the position of the Job just return NA, there should not be any verb in the position
    
        the answer should be in format
    position : 
    """
    return position_jd + '\n' + jd


def get_job_location_jd (jd):
    
    ''' prompt to find location from the job description '''

    job_location_jd = """Please fetch the following details from the Job description
    1. what is the location of the job? Please answer in three words. If there is no location provided then just simply answer NA
        the answer should be in format
    location : 
    """
    return job_location_jd + '\n' + jd

def get_job_skill_jd (jd):
    ''' prompt to find the list of skills from the job description '''

    skill_jd = """User
    Please fetch the following details from the Job description
    1. what are the skills required for the job? Please return the list of skills in summary
        the answer should be in format
    skill : 
    """
    return skill_jd + '\n' + jd

def get_min_experience_jd (jd):
    ''' prompt to find minimum experience from the job description '''

    min_experience_year_jd = """Please fetch the following details from the Job description
    1. what is the minimum experience required for the job, Answer the year only no text
    the answer should be in format
    year : 
    """
    return min_experience_year_jd + '\n' + jd



def get_min_education_jd (jd):

    ''' prompt to find minimum qualification needed from the job description '''

    education_jd = """Please fetch the following details from the Job description
    1. what are the education degree required for the job, Please return the list of degrees
    the answer should be in format
    education : 
    """
    return education_jd + '\n' + jd