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
| 👥 **Personalized Outreach** | Dynamically inserts recipient names from `email.csv` |
| 🎨 **Rich Responsive HTML** | Professional mobile-responsive template with plain-text fallback |
| 🖼️ **Inline Branding** | Embeds inline badges & logos with clean email-safe layout |
| 🔒 **Environment Security** | Secure `.env` credential management via `python-dotenv` |
| ⏱️ **Rate Limiting** | Configurable delay between dispatches to prevent spam flags |
| 📊 **Delivery Logging & Summary** | Detailed audit logs (`delivery_log.txt`) and failed email export |

---

## 📁 Repository Structure

```text
├── .env.example                 # Environment variable template
├── email.csv                    # Recipient list (Email, Name)
├── send_email.py                # Main automation & SMTP dispatch script
├── Gujarat Badge Template.png   # Inline attachment asset
├── .gitignore                   # Ignore cache, logs & sensitive files
└── README.md                    # Documentation
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install python-dotenv
```

### 2. Configure Credentials (`.env`)
Create a `.env` file from the `.env.example` template:
```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD="your_16_digit_app_password"
```
> 💡 *Generate an App Password via **Google Account → Security → 2-Step Verification → App Passwords**.*

### 3. Configure Recipients (`email.csv`)
```csv
Email,Name
recipient1@example.com,John Doe
recipient2@example.com,Jane Smith
```

### 4. Run Automation
```bash
python send_email.py
```

---

## 🛡️ Security Best Practice

- **Never** commit real passwords or `.env` files to GitHub.
- Keep `__pycache__/`, logs, and `.env` credentials tracked in `.gitignore`.

---

<div align="center">

Made with ❤️ by [**Shiv Jani**](https://www.linkedin.com/in/shiv-jani/) & **Dhairya Panchal**

⭐ **Star this repository if you find it helpful!**

</div>
