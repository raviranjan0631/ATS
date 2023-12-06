import re

def get_numbers_fromstring(st):
    ''' method to get numbers from a string'''
    
    nums = re.findall(r'\d+', st)

    return nums

def get_skills(st):
    ''' method to clean the and get the relevent skills from the text'''
    

    result = []
    for skill in st.split('\n'):
        temp = skill.split('-')[-1].strip()

        temp = ''.join([i for i in temp if not i.isdigit()])
        temp = temp.split(',')
        for t in temp:
            result.append(t)

    return result


def get_educations(st):
    ''' method to clean the and get the relevent education degree from the text'''

    result = []
    for skill in st.split('\n'):
        temp = skill.split('-')[-1].strip()

        temp = ''.join([i for i in temp if not i.isdigit()])
        
        result.append(temp)

    return result