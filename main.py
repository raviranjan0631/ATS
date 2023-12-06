import streamlit as st
import fitz
from openai import OpenAI
import os 

from src.openai_query import *
from src.jd_prompts import *
from src.string_cleaning import *
from src.resume_prompts import *
from src.calculate_similarity import *
from src.calculate_matching import *
from src.calculate_matching import *

st.title('Welcome to resume matching !!')
st.write('This will take few minutes to fetch the relevant information from Open AI API. Hence, Please have some patient')

api_key = os.environ['OPENAI_API_KEY']

st.markdown('Please upload your Job Description here')
uploaded_jd = st.file_uploader("Load job description: ", type=['pdf'] , key = '1')
### upload your job description here
text = ""
if uploaded_jd is not None:
    doc = fitz.open(stream=uploaded_jd.read(), filetype="pdf")
    
    for page in doc:
        text += page.get_text()
    
    doc.close()
jd = ''
if len(text) > 1:
    st.write('Job description loaded')
    jd = text

st.markdown('Please upload resume here')

### upload your resume here

uploaded_resume= st.file_uploader("Load resume: ", type=['pdf'], key = '2')
text = ""

if uploaded_resume is not None:
    doc = fitz.open(stream=uploaded_resume.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    
    doc.close()
resume = ''
if len(text) > 1:
    st.write('resume loaded successfully loaded')
    resume = text

### initating open ai client
openai_client = OpenAI(api_key=api_key)

if len(jd) > 1 and len(resume) > 1:

    ## fetching information from the job description and cleaning them at the same time
    position_jd = get_answer_openai( openai_client, get_job_position_jd(jd) ).split(':')[-1].strip()
    location_jd = get_answer_openai( openai_client, get_job_location_jd(jd) ).split(':')[-1].strip()
    min_exp_jd = min( get_numbers_fromstring( get_answer_openai( openai_client, get_min_experience_jd(jd) ).split(':')[-1].strip() ) )
    skills_jd =  get_skills( get_answer_openai( openai_client, get_job_skill_jd(jd) ).split(':')[-1].strip() )
    education_jd = get_educations( get_answer_openai( openai_client, get_min_education_jd(jd) ).split(':')[-1].strip() )

    st.caption('Once the Job description and resume are loaded then we try to fetch the following information from these two pdf Position, Location, minimum experience, skills and education qualification using OpenAI gpt3.5 turbo')
    st.markdown('Following information are found from the Job description you uploaded -- ')
    st.write('position :- ',position_jd)
    st.write('location of Job :-',location_jd)
    st.write('minimum experience required for the job :-',min_exp_jd)
    st.write('skills needed for the job :-\n', ', '.join(skills_jd) )
    st.write('education qualification needed for the job :-\n', ', '.join(education_jd) )

    st.write('--------------------')
    ### fetching information from the resume and cleaning them at the same time
    position_resume = get_answer_openai( openai_client, get_recent_title_resume(resume) ).split(':')[-1].strip()
    location_resume = get_answer_openai( openai_client, get_recent_location_resume(resume) ).split(':')[-1].strip()
    min_exp_resume = calculate_work_ex( get_answer_openai( openai_client, get_work_experience_resume(resume) ) )
    skills_resume = get_skills( get_answer_openai( openai_client, get_skills_resume(resume) ).split(':')[-1].strip()  )
    education_resume = get_educations( get_answer_openai( openai_client, get_min_education_resume(resume) ).split(':')[-1].strip() )

    st.markdown('Following information are found from the resume you uploaded -- ')
    st.write('current position of candidate :- ',position_resume)
    st.write('location of candidate :-',location_resume)
    st.write('minimum experience of the candidate :-',min_exp_resume)
    st.write('skills of candidate :- \n', ', '.join(skills_resume) )
    st.write('education qualification of candidate :- \n', 'and '.join(education_resume) )

    st.caption('once the information is loaded then we use to find the similarity between the values of Job Description and resume values using Sentence Transformer and cosine similarity')

    ### started matching part of the resume and the job description
    skill_matching = get_multiple_matching(skills_jd, skills_resume, 'skill')
    position_matching = get_similarity_text(position_jd, position_resume)
    location_matching = get_similarity_text(location_jd, location_resume)
    education_matching = get_multiple_matching(education_jd, education_resume, 'education')

    ### set the matching threshold of the skills, education
    st.caption('The similarity score between skill ans school is by deafult 0.4 but the user can choose the score according to his need. In my case 0.4 work best for me')
    skill_score = st.slider('Please enter your skill matching percentage', min_value = 1, max_value = 100, value = 40)
    skill_matched_threshold = get_similar_score(skill_matching, skill_score/100)
    st.write('Out of ', skill_matching.shape[0], ' only ', skill_matched_threshold.shape[0],' matched')
    st.dataframe(skill_matched_threshold, use_container_width = True)

    education_score = st.slider('Please enter your qualification matching percentage', min_value = 1, max_value = 100, value = 40)
    education_matched_threshold = get_similar_score(education_matching, education_score/100)
    st.write('Out of ', education_matching.shape[0], ' only ', education_matched_threshold.shape[0],' matched')
    st.dataframe(education_matched_threshold, use_container_width = True)

    ### set the ignorance level of skills
    st.caption('It"s very rare to find the candidate whose skills completely aligned with the Job Description. Hence, I had considered that the total skill wouls be matched with 80% skills mention in the JD. User can increase the percentage to 100%')
    skill_ignore = st.slider('Please enter the minimum number of skills you want to consider ', min_value = 1, max_value = skill_matching.shape[0], value = int(skill_matching.shape[0]*0.8) )

    ### Matching code start here

    education_matching_score = education_matched_threshold.shape[0] / education_matching.shape[0]
    skill_matching_score = skill_matched_threshold.shape[0] / skill_matching.shape[0]

    exp_matching = float(min_exp_resume) / float(min_exp_jd)

    if exp_matching > 1:
        exp_matching = 1

    scores = [position_matching, education_matching_score, exp_matching, skill_matching_score]

    st.caption('The matching is calculated on following basis position, education, experience, and skill. Also the user can give weightage to the feature he wants to. By default I had given equally weigtage to each of the features.')
    st.caption('In the matching part i had used the cosine similarity of position and education as there was no way to convert them to number.')
    st.markdown('Enter the weightage you want to give to various matching features :- ')

    position_slider = st.slider('Please enter the weightage you want to give position', min_value = 1, max_value = 10, value = 1)
    education_slider = st.slider('Please enter the weightage you want to give education', min_value = 1, max_value = 10, value = 1)
    experience_slider = st.slider('Please enter the weightage you want to give experience', min_value = 1, max_value = 10, value = 1)
    skill_slider = st.slider('Please enter the weightage you want to give skill', min_value = 1, max_value = 10, value = 1)

    weightage = [position_slider, education_slider, experience_slider, skill_slider]

    matching_button = st.button('calculate matching score')

   
    matching_score = get_matching_score(scores, weightage)

    st.markdown('The matching score is :---')
    st.title(matching_score)

