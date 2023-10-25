from smskillsdk.models.api import (
    InitRequest,
    SessionRequest,
    SessionResponse,
    ExecuteRequest,
    ExecuteResponse
)

from smskillsdk.models.api import (
    Output,
    Intent,
    Memory,
    Variables
)

import os
import requests
import json
import openai

openai.api_key = ""
openai.api_base = ""
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview' # this may change in the future
deployment_name=''
prompt=''


# import FastAPI
from fastapi import FastAPI

app = FastAPI()

# execute endpoint handler containing response generation logic
def execute_handler(request: ExecuteRequest) -> ExecuteResponse:

    # response generation logic here
    print (request.text)

    # Send a completion call to generate an answer
    print('Sending a test completion job')
    start_phrase = request.text
    response = openai.ChatCompletion.create(
        engine = deployment_name,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": start_phrase }
        ]
    )

    print(response)
    print(response['choices'][0]['message']['content'])


    variables = Variables(public={})

    output = Output(
        text=response['choices'][0]['message']['content'],
        variables=variables
    )

    response = ExecuteResponse(
        output=output,
        memory=[],
        endConversation=False,
    )

    return response

# route method (using FastAPI syntax)
@app.post("/execute", status_code=200, response_model=ExecuteResponse, response_model_exclude_unset=True)
def execute(request: ExecuteRequest):
    print ("EXECUTE")
    print (request)
    return execute_handler(request)


@app.post("/init", status_code=202)
def init(request: InitRequest):
    print ("INIT")
    print (request)
    return {}

# route method (using FastAPI syntax) for session endpoint. Receives a SessionRequest and returns a SessionResponse
@app.post("/session", status_code=200, response_model=SessionResponse, response_model_exclude_unset=True)
def init(request: SessionRequest):
    # reads the config values from the request and sets the global variables openai.api_key and openai.api_base as well as deployment_name
    print ("SESSION")
    print (request)
    global openai
    global deployment_name
    global prompt
    openai.api_key= request.config['Azure OpenAPI key']
    openai.api_base= request.config['Azure OpenAPI Endpoint']
    deployment_name = request.config['Azure OpenAPI Deployment Name']
    prompt = request.config['Azure OpenAI Prompt']
    return {}

@app.get("/")
def read_root():
    return {"Default": "Hello World"}