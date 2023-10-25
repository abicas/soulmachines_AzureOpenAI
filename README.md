# soulmachines_AzureOpenAI

## Azure OpenAI skill for Soul Machines

The idea behind this repository is to bring a simple API that will become a skill for Soul MAchines  (https://www.soulmachines.com/)
This skill will be able to interact with Azure Cognitive Services and OpenAI API.
We will also pack it into a Docker Container

To build Container: 
docker build --tag smskill_openai .

Run: 
docker run -t  -p  8000:8000 smskill_openai 

Access via 
http://localhost:8000/

Should be able to see the response for the get request
{"Default": "Hello World"}

Sample POST to session: 
{
  "projectId": "ABC123",
  "deploymentEnvironment": "preview",
  "config": {
    "Azure OpenAPI key": "string",
    "Azure OpenAPI Endpoint": "string",
    "Azure OpenAPI Deployment Name": "string",
    "Azure OpenAI Prompt": "string",
  }
}

Sample POST for execute: 
{
  "projectId": "ABC123",
  "deploymentEnvironment": "preview",
  "sessionId": "7600aff2-6ebd-44de-bcd2-1facd8ab4f29",
  "intent": {
    "name": "MY_INTENT",
    "confidence": 0
  },
  "text": "Describe me a cat",
  "context": {
    "Current_Time": "11 05 pm",
    "FacePresent": 1,
    "Turn_Id": "2050c232-f49c-4cfe-a440-13bde4af120f",
    "stt_final_result_string": "Describe me a cat",
    "UserTurn_IsAttentive": 0.3602287173271179,
    "UserTurn_IsTalking": null,
    "UserTurn_TextAnger": 0,
    "UserTurn_TextCare": 0,
    "UserTurn_TextConcern": 0,
    "UserTurn_TextDisgust": 0,
    "UserTurn_TextDistress": 0,
    "UserTurn_TextExcitement": 0,
    "UserTurn_TextFear": 0,
    "UserTurn_TextInterest": 0,
    "UserTurn_TextJoy": 0,
    "UserTurn_TextShame": 0,
    "UserTurn_TextSurprise": 0,
    "UserTurn_TextValence": 0,
    "User_Turn_Confusion": null,
    "User_Turn_Negativity": null,
    "User_Turn_Positivity": 0.5356926918029785,
    "is_speaking": false,
    "PersonaTurn_IsAttentive": null,
    "PersonaTurn_IsTalking": null,
    "Persona_Turn_Confusion": null,
    "Persona_Turn_Negativity": null,
    "Persona_Turn_Positivity": null
  }
}

Soul Machines Skill Definition:
{
  "name": "Azure OpenAI Raw Skill",
  "summary": "Azure OpenAI Raw Skill,
  "description": "This skill will be able to interact with Azure Cognitive Services and OpenAI API.",
  "isPublic": false,
  "status": "ACTIVE",
  "serviceProvider": "SKILL_API",
  "categoryIds": [],
  "endpointInitialize": "https://[ENDPOINT]/init",
  "endpointSession": "https://[ENDPOINT]/session",
  "endpointExecute": "https://[ENDPOINT]/execute",
  "endpointEndSession": null,
  "endpointEndProject": null,
  "endpointMatchIntent": null,
  "languages": null,
  "config": {
    "matchType": "FALLBACK",
    "skillType": "DEFAULT",
    "configMeta": [
      {
        "name": "Azure OpenAPI key",
        "type": "TEXT",
        "label": "Key generated for the Azure OpenAPI",
        "required": "true",
        "placeholder": "ba5aa5c22aa94b29aaa8919a584e01da",
        "defaultValue": ""
      },
      {
        "name": "Azure OpenAPI Endpoint",
        "type": "TEXT",
        "label": "Endpoint for the Azure OpenAPI",
        "required": "true",
        "placeholder": "https://[endpoint].openai.azure.com/",
        "defaultValue": "[endpoint].azurewebsites.net"
      },
      {
        "name": "Azure OpenAPI Deployment Name",
        "type": "TEXT",
        "label": "Deployment name for the Azure OpenAPI",
        "required": "true",
        "placeholder": "gpt4",
        "defaultValue": ""
      },
      {
        "name": "Azure OpenAI Prompt",
        "type": "TEXT",
        "label": "Full prompt for OpenAI, including KB",
        "required": "true",
        "placeholder": "You are XXX...",
        "defaultValue": ""
      }
    ],
    "exitPhrase": ".*"
  }
}
