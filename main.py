import os
import email_crawler
import parse_emails
import keyword_labelling
import train_model
import predict_emails
import extract_pdfs
import extract_metadata
import categorize_emails
7
def main():
    # Step 1: Fetch emails
    # emails = email_crawler.fetch_emails(num_emails=500)
    # email_crawler.save_emails_to_csv(emails, "data/emails.csv")
    
    # Step 2: Parse email bodies
    # parse_emails.parse_email_bodies("data/emails.csv", "data/parsed_emails.csv")
    
    # Step 3: Label emails with keywords
    # keyword_labelling.label_emails_with_keywords("data/parsed_emails.csv", "data/labeled_emails.csv")
    
    # Step 4: Train the ML model
    # train_model.train_and_save_model("data/labeled_emails.csv", "models/email_classifier.pkl")
    
    # Step 5: Predict using the trained model
    # predict_emails.predict_and_save_labels("data/parsed_emails.csv", "models/email_classifier.pkl", "data/final_labeled_emails.csv")
    
    # Step 6: Extract and save PDFs to Google Drive
    extract_pdfs.extract_and_save_pdfs("data/final_labeled_emails.csv")
    
    # Step 7: Extract metadata
    # extract_metadata.extract_and_save_metadata("data/final_labeled_emails.csv", "data/email_metadata.csv")
    
    # Step 8: Categorize emails in Gmail
    # categorize_emails.categorize_emails_in_gmail("data/final_labeled_emails.csv")

if __name__ == "__main__":
    main()
