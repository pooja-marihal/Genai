import openai
#import os
from openai import AzureOpenAI
import streamlit as st
 
# Set environment variables
print("okkkk")
api_key = st.secrets["AZURE_OPENAI_API_KEY"]
endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]

print("api_keyyyyyy",api_key,endpoint)
# Initialize the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,  
    api_version="2024-05-13"
)
print("connectedddd",client)
