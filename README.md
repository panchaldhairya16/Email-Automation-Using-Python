<div align="center">

# ✉️ Email Automation Using Python

**Automated, personalized HTML email dispatch with attachments via Gmail SMTP.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Gmail SMTP](https://img.shields.io/badge/Gmail-SMTP-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](https://support.google.com/mail/answer/185833)
[![License](https://img.shields.io/badge/License-MIT-00557F?style=for-the-badge)](LICENSE)

*Automate personalized email outreach with rich HTML formatting, dynamic recipient names, and inline badge attachments — zero third-party dependencies required.*

---

</div>

## ⚡ Highlights

| Feature | Description |
| :--- | :--- |
| 👥 **Personalized Outreach** | Dynamically inserts recipient name from `email.csv` |
| 🎨 **Rich HTML & Fallback** | Professional responsive template with plain-text fallback |
| 🖼️ **Inline Branding** | Embeds inline badges & logos with email-safe layout |
| 🔒 **Secure Authentication** | SSL-encrypted SMTP connection using Gmail App Passwords |
| 📦 **Zero Dependencies** | Built 100% on Python standard libraries (`smtplib`, `email`, `csv`) |

---

## 📁 Repository Structure

```text
├── email.csv                    # Recipient list (Email, Name)
├── send_email.py                # Main automation & SMTP dispatch script
├── Gujarat Badge Template.png   # Inline attachment asset
├── .gitignore                   # Ignore cache & sensitive files
└── README.md                    # Documentation
```

---

## 🚀 Quick Start

### 1. Configure Recipients (`email.csv`)
```csv
Email,Name
panchaldhairya2005@gmail.com,Dhairya
shivjani2005@gmail.com,Shiv Jani
```

### 2. Configure Credentials (`send_email.py`)
```python
email_user = "your_email@gmail.com"
password = "your_16_char_app_password"
```
> 💡 *Generate an App Password via **Google Account → Security → 2-Step Verification → App Passwords**.*

### 3. Run Automation
```bash
python send_email.py
```

---

## 🛡️ Security Best Practice

- **Never** commit real passwords or `.env` files to GitHub.
- Keep `__pycache__/` and sensitive credentials tracked in `.gitignore`.

---

<div align="center">

Made with ❤️ by **Shiv Jani** & **Dhairya Panchal**

⭐ **Star this repository if you find it helpful!**

</div>
