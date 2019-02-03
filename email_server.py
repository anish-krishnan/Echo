import smtplib, ssl


def open_server():
    port = 587  # For SSL
    password = "pharmabot44"
# Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("pharmabot44@gmail.com", password)
            # TODO: Send email here
