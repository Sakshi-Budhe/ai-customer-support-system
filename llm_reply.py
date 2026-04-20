def generate_reply(ticket_text):
    if "payment" in ticket_text.lower():
        return "We are sorry for the payment issue. Our team is checking it."

    elif "login" in ticket_text.lower():
        return "Please reset your password using forgot password option."

    elif "app" in ticket_text.lower():
        return "We are working on fixing the app issue."

    else:
        return "We have received your issue and will resolve it soon."
