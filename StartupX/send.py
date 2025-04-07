import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "mohanprasanth169@gmail.com"  # Replace with your email
    receiver_email = "23z237@psgtech.ac.in"  # Replace with the recipient's email
    password = "mohan123!@#prasath"  # Replace with your email password or app password

    # Create the email message
    subject = "Test Email"
    body = "Hello, this is a test email sent from Python!"

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection

        # Login to your email account
        server.login(sender_email, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

        # Close the connection
        server.quit()

        print("✅ Test email sent successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the send_email function
if __name__ == "__main__":
    send_email()
