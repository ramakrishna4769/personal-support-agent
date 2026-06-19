import streamlit as st
from src.retriever import retrieve_documents
from src.generator import generate_response
from src.escalator import should_escalate

st.title("Persona Adaptive Support Agent")

query = st.text_input("Ask a question")

if st.button("Submit"):

    if query:

        if should_escalate(query):
            st.error("Escalation Required")
            st.write("Human Agent Needed")

        else:
            results = retrieve_documents(query)

            context = ""

            for doc in results["documents"][0]:
                context += doc + "\n"

            answer = generate_response(query, context)

            st.success("AI Response")
            st.write(answer)