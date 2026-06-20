# Persona Adaptive Customer Support Agent

## Overview

This project is an AI-powered customer support agent that:

* Detects customer personas
* Retrieves relevant support information using RAG
* Generates adaptive responses
* Escalates sensitive issues to human agents

## Tech Stack

* Python 3.11+
* Google Gemini
* ChromaDB
* Streamlit
* LangChain
* PyPDF
* Python Dotenv

## Architecture

User Query
→ Persona Detection
→ Document Retrieval (RAG)
→ Response Generation
→ Escalation Check
→ Human Handoff

## Features

* Technical Expert support
* Frustrated User support
* Business Executive support
* Knowledge Base Retrieval
* Escalation for billing and refund issues
* Streamlit UI

## Setup

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## Example Queries

* How do I reset my password?
* Why is my payment failing?
* My account is locked.
* I want a refund immediately.
* What causes API authentication errors?

## Future Improvements

* Multi-turn memory
* Sentiment analysis
* LangGraph workflow
* Human approval workflow
