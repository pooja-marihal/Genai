import openai
import os
from openai import AzureOpenAI
 
# Set environment variables
os.environ['AZURE_OPENAI_API_KEY'] = 'de87392f71a84ccaa4e62ec942c56f6c'
os.environ['AZURE_OPENAI_ENDPOINT'] = 'https://idea-4-azure-open-ai.openai.azure.com/'
 
# Retrieve environment variables
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
 
# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,  
    api_version="2024-02-01"
)
