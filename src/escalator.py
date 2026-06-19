def should_escalate(user_query):

    sensitive_words = [
        "refund",
        "billing",
        "legal",
        "lawsuit",
        "account modification"
    ]

    query = user_query.lower()

    for word in sensitive_words:
        if word in query:
            return True

    return False