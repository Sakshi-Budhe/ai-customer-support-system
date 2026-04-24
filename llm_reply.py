def generate_reply(category):

    if category == "Greeting":
        return "Hi How can I help you today?"

    elif category == "Billing":
        return "We are checking your billing issue. Please wait for an update."

    elif category == "Technical":
        return "Our technical team is working on this issue."

    elif category == "Account":
        return "Please check your account settings or reset password."

    else:
        return "Please describe your issue in detail so we can help you better."
