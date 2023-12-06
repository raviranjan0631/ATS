# ATS Matching
### This project aim is to perform a matching between a Job Description and Resume.
#### It is build using OpenAI 3.5 turbo, Hugging face Sentence Transformers and Streamlit

### How to run  this.

#### In the project you will find a docker image there. You can use the docker image by building it
#### Step 1 - The command to build that docker image is

docker build . -t image_name

or 

docker pull raviranjan0631/ats:1

Since, it's using openai 3.5 turbo you also need an access key to run it

#### Step 2 - Once the image is build then you have to run the following command
if you have build the image
docker run --rm -p 80:80 -d -e OPEN_API_KEY = Your_open_ai_key imagename 

or 

if you have pulled the image
docker run --rm -p 80:80 -d -e OPEN_API_KEY = Your_open_ai_key raviranjan0631/ats:1

#### Step 3 - Once you have run the container then go to http://localhost:80