

# Keylogger with Email Reporting 🚀

A simple Python-based keylogger that captures keystrokes, logs them to a file, and sends periodic reports via email using **Mailtrap** (primary) or **Gmail** (fallback). Designed for **educational purposes** or **authorized security testing** only.

---

## 🌟 Features

- Captures keystrokes and logs them with timestamps.  
- Recognizes special keys like space, enter, backspace, and more.  
- Sends logs at regular intervals (default: every minute).  
- Uses a primary email service, with a backup if needed.  
- Saves logs locally and can optionally delete them after sending.  
- Retries sending if delivery fails.  

---

## 🛠️ Prerequisites

- Python installed on your system.  
- Required tools: a keystroke capture library, an email service library, and basic threading support.  
- An account with **Mailtrap** (optional but recommended).  
- A **Gmail** account with a secure password setup for backup.  

---

## 📦 Installation

1. **Get the Tool**  
   - Download the keylogger file to your computer.  

2. **Install Required Tools**  
   - Open your terminal or command prompt.  
   - Install the keystroke capture library by typing: pip install keyboard.  
   - Install the email service library by typing: pip install mailtrap.  

3. **Set Up Configuration**  
   - Open the keylogger file in a text editor.  
   - Find the section labeled "Configuration (customize these)".  
   - Replace "your_email@gmail.com" with your Gmail address for backup email.  
   - Replace "your_gmail_app_password" with your Gmail App Password (generate this from your Google Account settings under Security).  
   - Set the report interval by changing "60" to your desired number of seconds (e.g., 120 for 2 minutes).  
   - Add your Mailtrap token by replacing the empty quotes after "MAILTRAP_TOKEN" with your token from the Mailtrap dashboard.  
   - Add your Mailtrap sender email by replacing the empty quotes after "MAILTRAP_SENDER_EMAIL" with your sender email.  
   - Keep "Keylogger Report" as the sender name or change it after "MAILTRAP_SENDER_NAME".  
   - Add your recipient email by replacing the empty quotes after "MAILTRAP_RECIPIENT_EMAIL" with the email address to receive logs.  

---

## 🚀 Usage

1. **Start the Tool**  
   - Open a terminal or command prompt.  
   - Navigate to the folder with the keylogger file using the "cd" command (e.g., cd path/to/folder).  
   - Launch it by typing: python keylogger.py. On some systems, use sudo python keylogger.py (Linux/Mac) or run as Administrator (Windows).  

2. **What Happens**  
   - It begins capturing keystrokes right away.  
   - Logs are saved to a file named "keylogger_log.txt" with timestamps.  
   - Reports are emailed at the set interval using Mailtrap or Gmail if Mailtrap fails.  
   - The local file may be cleared after sending, depending on settings.  

3. **Stopping the Tool**  
   - Press Ctrl+C in the terminal to stop it, though it might finish its current cycle.  

---

## 📜 Example Output

### Log File  
- Entries show the date, time, and keystrokes, like "hello world" or special key labels such as "[ENTER]".  

### Email Subject  
- Reports are titled "Keylogger Report" via Mailtrap or "Keylogger Report (Fallback)" via Gmail.  

---

## 🎨 Customization

- Adjust the report timing to send logs more or less often by changing the interval in the configuration.  
- Choose to keep the local log file instead of deleting it by editing the tool to skip the removal step.  
- Expand key recognition to include more special keys by adding them in the key handling section.  

---

## 🐞 Troubleshooting

- **Access Issues**: Run with higher permissions if keystrokes aren’t captured (e.g., as admin or with sudo).  
- **Email Not Sending**: Check your Mailtrap token, sender, and recipient details, or ensure Gmail credentials are correct.  
- **Backup Fails**: Verify your Gmail App Password and check Google’s security settings.  

---

## ⚠️ Important Notes

- **Ethical Use**: This is for learning or approved security testing only. Unauthorized use may break laws.  
- **Security**: Keep sensitive details like passwords safe, ideally not in the file itself.  
- **Requirements**: Some systems may need admin access to capture keystrokes.  

---

## 📝 License

This project is unlicensed and provided as-is for educational purposes. Use responsibly.

---

## 🤝 Contributing

Feel free to adapt this tool, suggest improvements, or share ideas via GitHub!

---

