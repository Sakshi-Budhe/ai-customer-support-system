# AI Customer Support System

## Overview
This is a simple AI-based Customer Support System built using Python and Machine Learning.  
It classifies customer issues into categories like Billing, Technical, and Account and provides basic automated responses.

## Features
- Classifies customer issues automatically
- NLP using TF-IDF
- Machine Learning model (Naive Bayes)
- Simple Streamlit web app
- Fast predictions

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

## Project Structure
ai-support-system/
├── app.py
├── model.py
├── llm_reply.py
├── data.csv
├── README.md

## How It Works
1. User enters an issue
2. Text is processed using TF-IDF
3. ML model predicts category
4. Response is generated
5. Output is shown in Streamlit UI

## How to Run
pip install pandas scikit-learn streamlit

python -m streamlit run app.py

## Example

Input:
My payment failed but money is deducted

Output:
Category: Billing
Response: We are looking into your issue. Please wait for an update.

## What I Learned
- Machine Learning basics
- NLP (TF-IDF)
- Streamlit web apps
- Debugging Python errors
- End-to-end project building

## Future Improvements
- Add real AI (LLM-based replies)
- Improve accuracy with more data
- Add database storage
- Deploy online

## Author
Built as a learning project using Python and Machine Learning
