import csv
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Sender Configuration
email_user = "shivjani.aws@gmail.com"
password = "hcln pgxe ajld dfwc"
subject = "Invitation: Hands-on Workshop on Agentic Workflows & Searchable Applications | Elastic User Group Gujarat"

# Attachment file path
attachment_image_path = "Gujarat Badge Template.png"

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
Shiv Jani
Contact: +91 8160308850
Elastic User Group Gujarat | Organizing Team
"""

        # HTML version of the email
        html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333333;
      background-color: #f9f9f9;
      margin: 0;
      padding: 20px;
    }}
    .container {{
      max-width: 650px;
      margin: 0 auto;
      background-color: #ffffff;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
      border: 1px solid #e2e8f0;
    }}
    h2 {{
      color: #00557f;
      margin-top: 0;
    }}
    .highlight-box {{
      background-color: #f0f7ff;
      border-left: 4px solid #00557f;
      padding: 15px 20px;
      margin: 20px 0;
      border-radius: 4px;
    }}
    ul {{
      margin: 10px 0 10px 20px;
      padding: 0;
    }}
    li {{
      margin-bottom: 6px;
    }}
    .btn {{
      display: inline-block;
      background-color: #00557f;
      color: #ffffff !important;
      padding: 12px 24px;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
      margin: 15px 0;
    }}
    .details {{
      background-color: #f8fafc;
      padding: 15px;
      border-radius: 6px;
      margin: 20px 0;
    }}
    .footer {{
      margin-top: 25px;
      border-top: 1px solid #e2e8f0;
      padding-top: 15px;
      color: #555555;
    }}
    .badge-img {{
      max-width: 100%;
      height: auto;
      margin-top: 20px;
      border-radius: 6px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <p>Dear <strong>{name}</strong>,</p>
    
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
      <p>📅 <strong>Date:</strong> Sunday, 23 August 2026</p>
      <p>📍 <strong>Location:</strong> Ahmedabad, Gujarat</p>
      <p>🔗 <a href="https://luma.com/mcntdcu1" class="btn">Register Now</a></p>
    </div>
    
    <p>We would greatly appreciate it if you could share this invitation with relevant members of your engineering and technology teams who may be interested in attending.</p>
    
    <p>We look forward to welcoming your team and creating a valuable technical learning experience together.</p>
    
    <div class="footer">
      <table role="presentation" width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
        <tr>
          <td valign="middle" style="vertical-align: middle; padding-right: 15px;">
            <p style="margin: 0 0 5px 0;">Best regards,</p>
            <p style="margin: 0 0 5px 0; font-size: 16px; color: #111827;"><strong>Shiv Jani</strong></p>
            <p style="margin: 0 0 5px 0; color: #555555;">Contact: +91 8160308850</p>
            <p style="margin: 0; color: #00557f; font-weight: 600;">Elastic User Group Gujarat | Organizing Team</p>
          </td>
          <td valign="middle" align="right" style="vertical-align: middle; text-align: right; width: 180px;">
            <img src="cid:badge_template" alt="Gujarat Badge Template" style="max-width: 180px; width: 100%; height: auto; border-radius: 6px; display: block; margin-left: auto;" />
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
            print(f"Email sent successfully to {name} ({email_send})")
        except Exception as e:
            print(f"Failed to send email to {name} ({email_send}): {e}")

# Close connection
server.quit()
print("All emails processed successfully!")