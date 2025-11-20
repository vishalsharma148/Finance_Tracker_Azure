import streamlit as st
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

AZURE_ENDPOINT = st.secrets["AZURE_ENDPOINT"]
AZURE_KEY = st.secrets["AZURE_KEY"]

def create_text_analytics_client():
    return TextAnalyticsClient(
        endpoint=AZURE_ENDPOINT,
        credential=AzureKeyCredential(AZURE_KEY)
    )

def analyze_sentiment(text):
    client = create_text_analytics_client()
    result = client.analyze_sentiment([text])[0]
    return result.sentiment

def extract_keywords(text):
    client = create_text_analytics_client()
    result = client.extract_key_phrases([text])[0]
    return result.key_phrases