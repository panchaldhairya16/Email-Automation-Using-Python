import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_user = "YOUR_MAIL_ADDR"
password = "YOUR_PASSWORD"
subject = "Holiday Reminder"

# Connect to Gmail SMTP server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Login
server.login(email_user, password)

# Read CSV file
with open("email.csv", "r", newline="", encoding="utf-8") as csvfile:

    reader = csv.reader(csvfile)

    # Skip header
    next(reader)

    for line in reader:

        email_send = line[0]
        name = line[1]

        # Personalized message
        text = f"""
Hello {name},

Today you have a holiday, so relax and enjoy it!

Have a great day!
"""

        # Create email
        msg = MIMEMultipart()

        msg["From"] = email_user
        msg["To"] = email_send
        msg["Subject"] = subject

        # Add message
        msg.attach(MIMEText(text, "plain"))

        # Send email
        server.sendmail(
            email_user,
            email_send,
            msg.as_string()
        )

        print(f"Email sent successfully to {name} ({email_send})")

# Close connection
server.quit()

print("All emails sent successfully!")
