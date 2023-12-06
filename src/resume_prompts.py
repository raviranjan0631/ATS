def get_work_experience_resume(resume):
    ''' prompt to find the work experience from the resume '''

    work_experience = """
    1. what is total work experience of the candidate . Please just answer the exact year and months. you don't need to explain the calculations to me
    the answer should be return in this format 
    year :
    month :
    
    if you are unabale to calculate it then return 0
    """
    
    return work_experience + '\n' + resume


def get_skills_resume(resume):
    ''' prompt to find the list of skills from the resume '''

    skills = """
    1. what are the skills of the candidate. Please make a list of the skills mentioned in the JD
    the answer should be return in this format 
    skills :


    
    if you are unabale to find the skills then return NA"""
    
    return skills + '\n' + resume


def get_education_resume(resume):
    ''' prompt to find the education from the resume '''


    education = """
    1. what are the education degree of the candidate. Please make a list of the Job description mentioned in the JD
    the answer should be return in this format. 
    educations : degree name


    
    if you are unabale to find the skills then return NA"""
    
    return education + '\n' + resume


def get_recent_title_resume(resume):
    ''' prompt to find the recent position from the resume '''


    title = """ 1. what is the current position of the candidate in his latest company
    the answer should be return in this format. 
    position : position name

    
    if you are unabale to find the skills then return NA"""
    
    return title + '\n' + resume


def get_recent_location_resume(resume):
    ''' prompt to find the location from the resume '''

    location = """ 1. what is the most recent location of the candidate in his latest company
    the answer should be return in this format. 
    location : location name

    
    if you are unabale to find the skills then return NA"""
    
    return location + '\n' + resume

def calculate_work_ex(st):
    ''' method to calculate the total work exp of candidate from the string '''


    total = 0
    for ex in st.split('\n'):
        if 'year' in ex:
            total += int( ex.split(':')[-1].strip() )
        if 'month' in ex:
            total += float( ex.split(':')[-1].strip() ) /12
    
    return total


def get_min_education_resume (resume):
    ''' prompt to find the education from the resume '''

    education_resume = """Please fetch the following details from the Job description
    1. what are the education degree mention in the resume below, Please return the list of degrees
    the answer should be in format
    education : 
    """
    return education_resume + '\n' + resume