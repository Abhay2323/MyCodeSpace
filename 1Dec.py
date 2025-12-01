import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "microsoft/Phi-4-reasoning"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        UserMessage("What is the capital of France?"),
    ],
    temperature=0.8,
    top_p=0.95,
    max_tokens=4096,
    model=model
)

print(response.choices[0].message.content)