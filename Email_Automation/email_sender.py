import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# --- CONFIGURATION ---
SENDER_EMAIL = "salauddin748356@gmail.com"
SENDER_PASSWORD = "here your app password"  

SUBJECT_FILE = "subject.txt"
MESSAGE_FILE = "message.txt"
RECEIVERS_FILE = "receivers.txt"

# --- READ SUBJECT ---
with open(SUBJECT_FILE, 'r', encoding='utf-8') as f:
    subject = f.read().strip()

# --- READ MESSAGE BODY ---
with open(MESSAGE_FILE, 'r', encoding='utf-8') as f:
    message_body = f.read()

# --- READ RECEIVERS LIST ---
with open(RECEIVERS_FILE, 'r') as f:
    receivers = [email.strip() for email in f if email.strip()]

# --- FUNCTION TO SEND EMAIL ---
def send_email(to_email):
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Send email
        server.send_message(msg)
        server.quit()

        print(f"Email sent to {to_email}")
        # print(f"Preview: \nTo: {to_email}\nSubject: {subject}\nMessage:\n{message_body[:50]}...")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# --- SEND TO ALL RECEIVERS ---
print("\nSending Emails...\n")
for email in receivers:
    send_email(email)

print("\nAll emails processed.")

