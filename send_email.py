import csv
import smtplib
import os
import sys
import time
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Sender Configuration
email_user = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")

if not email_user or not password:
    print("Error: EMAIL_USER or EMAIL_PASSWORD not found in environment or .env file.")
    print("Please make sure you have a .env file configured with EMAIL_USER and EMAIL_PASSWORD.")
    sys.exit(1)

subject = "Invitation: Hands-on Workshop on Agentic Workflows & Searchable Applications | Elastic User Group Gujarat"

# Attachment file path
attachment_image_path = "Gujarat Badge Template.png"

# Delay in seconds between consecutive emails to prevent rate limiting / spam flags
DELAY_BETWEEN_EMAILS = 2.0

# Logging files
LOG_FILE = "delivery_log.txt"
FAILED_CSV_FILE = "failed_emails.csv"

# Tracking metrics
successful_sends = []
failed_sends = []

# Connect to Gmail SMTP server
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

# Login
server.login(email_user, password)

def log_delivery(status, email, name, error_msg=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] [{status}] {name} <{email}>"
    if error_msg:
        log_line += f" - Error: {error_msg}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

# Read CSV file
with open("email.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)

    # Skip header
    next(reader)

    for line in reader:
        if not line or len(line) < 2:
            continue

        email_send = line[0].strip()
        name = line[1].strip()

        # Plain-text version of the email
        text_content = f"""Dear {name},

Greetings from the Elastic User Group Gujarat team.

We are pleased to invite your engineering and technology team to our upcoming hands-on technical workshop focused on Agentic Workflows and Searchable Applications using Elasticsearch, Jina, and Agent-to-Agent (A2A) Communication.

We especially welcome professionals working with data, search, backend services, product catalogs, DevOps, cloud, AI applications, and software engineering.

Workshop Highlights:
• Data ingestion into Elasticsearch
• Geo-spatial and semantic search
• Keyword search
• Elastic Agent Builder and workflows
• Automated emails through AI agents
• Connecting tools, skills, and agents
• Agent-to-Agent (A2A) communication
• Practical implementation of search-driven and agent-driven applications

This will be a practical, hands-on session where participants will build real-world features applicable to e-commerce, search applications, AI solutions, and modern software systems.

No prior Elasticsearch experience is required. Participants are requested to bring a laptop and be comfortable running basic code.

Date: Sunday, 23 August 2026
Location: Ahmedabad, Gujarat
Register now: https://luma.com/mcntdcu1

We would greatly appreciate it if you could share this invitation with relevant members of your engineering and technology teams who may be interested in attending.

We look forward to welcoming your team and creating a valuable technical learning experience together.

Best regards,
Shiv Jani (LinkedIn: https://www.linkedin.com/in/shiv-jani/)
Contact: +91 8160308850
Elastic User Group Gujarat | Organizing Team
"""

        # HTML version of the email
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      color: #2d3748;
      background-color: #f4f6f9;
      margin: 0;
      padding: 16px 8px;
      -webkit-text-size-adjust: 100%;
    }}
    .container {{
      max-width: 620px;
      margin: 0 auto;
      background-color: #ffffff;
      padding: 28px 24px;
      border-radius: 8px;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
      border: 1px solid #e2e8f0;
      box-sizing: border-box;
    }}
    .highlight-box {{
      background-color: #f0f7ff;
      border-left: 4px solid #00557f;
      padding: 14px 18px;
      margin: 20px 0;
      border-radius: 4px;
    }}
    ul {{
      margin: 8px 0 8px 18px;
      padding: 0;
    }}
    li {{
      margin-bottom: 6px;
    }}
    .btn {{
      display: inline-block;
      background-color: #00557f;
      color: #ffffff !important;
      padding: 11px 24px;
      text-decoration: none;
      border-radius: 5px;
      font-weight: 600;
      font-size: 15px;
    }}
    .details {{
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      padding: 16px 18px;
      border-radius: 6px;
      margin: 20px 0;
    }}
    .footer-wrapper {{
      margin-top: 28px;
      border-top: 1px solid #e2e8f0;
      padding-top: 20px;
    }}
    .contact-badge {{
      display: inline-block;
      background-color: #f0f7ff;
      color: #00557f !important;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 4px;
      border: 1px solid #cce3f5;
      text-decoration: none;
      font-size: 13px;
    }}
    @media only screen and (max-width: 540px) {{
      body {{
        padding: 8px 4px !important;
      }}
      .container {{
        padding: 20px 16px !important;
        border-radius: 6px !important;
      }}
      .footer-table td {{
        display: block !important;
        width: 100% !important;
        padding: 0 !important;
        box-sizing: border-box !important;
      }}
      .badge-cell {{
        padding-top: 16px !important;
        text-align: left !important;
      }}
      .badge-cell img {{
        margin-left: 0 !important;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <p style="margin-top: 0;">Dear <strong>{name}</strong>,</p>
    
    <p>Greetings from the <strong>Elastic User Group Gujarat</strong> team.</p>
    
    <p>We are pleased to invite your engineering and technology team to our upcoming hands-on technical workshop focused on <strong>Agentic Workflows and Searchable Applications</strong> using <strong>Elasticsearch, Jina, and Agent-to-Agent (A2A) Communication</strong>.</p>
    
    <p>We especially welcome professionals working with data, search, backend services, product catalogs, DevOps, cloud, AI applications, and software engineering.</p>
    
    <div class="highlight-box">
      <strong>Workshop Highlights:</strong>
      <ul>
        <li>Data ingestion into Elasticsearch</li>
        <li>Geo-spatial and semantic search</li>
        <li>Keyword search</li>
        <li>Elastic Agent Builder and workflows</li>
        <li>Automated emails through AI agents</li>
        <li>Connecting tools, skills, and agents</li>
        <li>Agent-to-Agent (A2A) communication</li>
        <li>Practical implementation of search-driven and agent-driven applications</li>
      </ul>
    </div>
    
    <p>This will be a practical, hands-on session where participants will build real-world features applicable to e-commerce, search applications, AI solutions, and modern software systems.</p>
    
    <p><em>No prior Elasticsearch experience is required. Participants are requested to bring a laptop and be comfortable running basic code.</em></p>
    
    <div class="details">
      <p style="margin: 0 0 6px 0;"><strong>Date:</strong> Sunday, 23 August 2026</p>
      <p style="margin: 0 0 14px 0;"><strong>Location:</strong> Ahmedabad, Gujarat</p>
      <div>
        <a href="https://luma.com/mcntdcu1" class="btn">Register Now</a>
      </div>
    </div>
    
    <p>We would greatly appreciate it if you could share this invitation with relevant members of your engineering and technology teams who may be interested in attending.</p>
    
    <p style="margin-bottom: 0;">We look forward to welcoming your team and creating a valuable technical learning experience together.</p>
    
    <div class="footer-wrapper">
      <table class="footer-table" role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
        <tr>
          <td valign="middle" style="vertical-align: middle; padding-right: 12px;">
            <div style="border-left: 3px solid #00557f; padding-left: 12px;">
              <p style="margin: 0 0 4px 0; color: #718096; font-size: 13px;">Best regards,</p>
              <p style="margin: 0 0 3px 0; font-size: 16px; font-weight: 700; color: #0f172a;">
                <a href="https://www.linkedin.com/in/shiv-jani/" target="_blank" style="color: #00557f; text-decoration: underline;">Shiv Jani</a>
              </p>
              <p style="margin: 0 0 6px 0; font-size: 13px; color: #4a5568;">
                <strong>Elastic User Group Gujarat</strong> | Organizing Team
              </p>
              <p style="margin: 0; font-size: 13px; color: #4a5568;">
                Contact: <a href="tel:+918160308850" class="contact-badge">+91 8160308850</a>
              </p>
            </div>
          </td>
          <td class="badge-cell" valign="middle" align="right" style="vertical-align: middle; text-align: right; width: 95px;">
            <img src="cid:badge_template" alt="Elastic User Group Gujarat Badge" style="width: 88px; max-width: 88px; height: auto; display: block; margin-left: auto;" />
          </td>
        </tr>
      </table>
    </div>
  </div>
</body>
</html>
"""

        # Create multi-part email
        msg = MIMEMultipart("related")
        msg["From"] = email_user
        msg["To"] = email_send
        msg["Subject"] = subject

        # Create alternative part for text & html
        msg_alternative = MIMEMultipart("alternative")
        msg.attach(msg_alternative)

        # Attach text and html versions
        msg_alternative.attach(MIMEText(text_content, "plain", "utf-8"))
        msg_alternative.attach(MIMEText(html_content, "html", "utf-8"))

        # Attach Image with Content-ID for inline display and as attachment
        if os.path.exists(attachment_image_path):
            with open(attachment_image_path, "rb") as img_f:
                img_data = img_f.read()
                img = MIMEImage(img_data)
                img.add_header("Content-ID", "<badge_template>")
                img.add_header("Content-Disposition", "inline", filename=os.path.basename(attachment_image_path))
                msg.attach(img)

        # Send email
        try:
            server.sendmail(email_user, email_send, msg.as_string())
            successful_sends.append({"name": name, "email": email_send})
            log_delivery("SUCCESS", email_send, name)
            print(f"[SUCCESS] Email sent to {name} ({email_send})")
        except Exception as e:
            failed_sends.append({"name": name, "email": email_send, "error": str(e)})
            log_delivery("FAILED", email_send, name, error_msg=str(e))
            print(f"[FAILED] Failed to send email to {name} ({email_send}): {e}")

        # Pause briefly between emails to respect provider rate limits
        if DELAY_BETWEEN_EMAILS > 0:
            time.sleep(DELAY_BETWEEN_EMAILS)

# Close connection
server.quit()

# Export failed emails if any exist
if failed_sends:
    with open(FAILED_CSV_FILE, "w", newline="", encoding="utf-8") as f_out:
        writer = csv.writer(f_out)
        writer.writerow(["Email", "Name", "Error"])
        for item in failed_sends:
            writer.writerow([item["email"], item["name"], item["error"]])

# Print Dispatch Summary
total_processed = len(successful_sends) + len(failed_sends)
print("\n" + "=" * 50)
print("             EMAIL DISPATCH SUMMARY")
print("=" * 50)
print(f" Total Processed : {total_processed}")
print(f" Successful      : {len(successful_sends)}")
print(f" Failed          : {len(failed_sends)}")
print(f" Detailed Log    : {LOG_FILE}")
if failed_sends:
    print(f" Failed List CSV : {FAILED_CSV_FILE}")
print("=" * 50)