import openai
import os


def createRespone(input):
    openai.api_key = #put your api key here

    messages = [{"role": "system", "content":  "You are a computer program that is named Jarvis and will call everyone sir"}] 
    message =  input
    if message: 
        messages.append( {"role": "user", "content": message}, ) 
        chat = openai.chat.completions.create( model="gpt-3.5-turbo", messages=messages) 
        reply = chat.choices[0].message.content 
    return reply 
