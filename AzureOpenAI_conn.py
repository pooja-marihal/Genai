import openai
import os
from openai import AzureOpenAI
import streamlit as st
 
# Set environment variables
os.environ['AZURE_OPENAI_API_KEY'] == st.secrets["AZURE_OPENAI_API_KEY"]
os.environ['AZURE_OPENAI_ENDPOINT'] == st.secrets["AZURE_OPENAI_ENDPOINT"]
 
# Retrieve environment variables
api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
 
# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,  
    api_version="2024-05-13"
)
