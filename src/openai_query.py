from openai import OpenAI


def get_answer_openai(openai_client, prompt):
    
    ''' method to get the answer from the open ai '''
    
    completion = openai_client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
           {"role": "system", "content": prompt}


      ]
    )

    return completion.choices[0].message.content
 


