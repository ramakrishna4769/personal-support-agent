from src.escalator import should_escalate

query = input("Enter query: ")

if should_escalate(query):
    print("ESCALATE TO HUMAN AGENT")
else:
    print("NORMAL AI RESPONSE")