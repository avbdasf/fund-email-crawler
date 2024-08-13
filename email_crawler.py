import imaplib
import email
from email.header import decode_header
import pandas as pd
import os

# Define email credentials and server
EMAIL = "research@gao-cap.com"
PASSWORD = "acxk rixo hcfz hjpo"
SERVER = "imap.gmail.com"
DATA_PATH = "data"

def fetch_emails(num_emails=500):
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()[-num_emails:]
    
    emails_data = []
    
    for idx, email_id in enumerate(email_ids):
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["subject"])[0]
                if isinstance(subject, bytes):
                    try:
                        subject = subject.decode(encoding if encoding else "utf-8")
                    except UnicodeDecodeError:
                        subject = subject.decode("latin1")
                from_ = msg.get("From")
                date_ = msg.get("Date")
                msg_id = msg.get("Message-ID")
                
                # Default value for body
                body = ""
                
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            part_body = part.get_payload(decode=True).decode(encoding if encoding else "utf-8", errors="ignore")
                        except:
                            part_body = ""
                        if "attachment" not in content_disposition:
                            body += part_body
                else:
                    body = msg.get_payload(decode=True).decode(encoding if encoding else "utf-8", errors="ignore")
                
                emails_data.append([from_, date_, subject, body, msg_id])
        
        print(f"Fetched email {idx + 1}/{num_emails}")
    
    return emails_data

def save_emails_to_csv(emails, filepath):
    df = pd.DataFrame(emails, columns=["From", "Date", "Subject", "Body", "Message_ID"])
    df.to_csv(filepath, index=False)
    print(f"Saved emails to {filepath}")

if __name__ == "__main__":
    emails = fetch_emails(num_emails=500)
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
    filePath = os.path.join(DATA_PATH, "emails.csv")
    save_emails_to_csv(emails, filePath)
