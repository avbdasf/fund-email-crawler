# Monthly Update Email Classifier

## Overview

This project is designed to classify monthly update emails, extract relevant PDF attachments, and process metadata. It involves fetching emails from an IMAP server, parsing email bodies, labeling emails with keywords, training a machine learning model, predicting email labels, extracting and saving PDFs to Google Drive, extracting metadata, and categorizing emails in Gmail.

## Features

1. **Email Crawler**: Fetches emails from an IMAP server and saves them to a CSV file.
2. **Email Parser**: Parses email bodies and prepares them for analysis.
3. **Keyword Labelling**: Labels emails with keywords to aid in the classification process.
4. **Model Training**: Trains a machine learning model to classify monthly update emails.
5. **Prediction**: Uses the trained model to predict labels for emails.
6. **PDF Extraction**: Extracts PDF attachments from emails and saves them to Google Drive.
7. **Metadata Extraction**: Extracts metadata from emails and saves it to a CSV file.
8. **Email Categorization**: Categorizes emails in Gmail based on the predictions.

## Project Structure

- `email_crawler.py`: Contains functions to fetch emails from an IMAP server.
- `parse_emails.py`: Contains functions to parse email bodies.
- `keyword_labelling.py`: Contains functions to label emails with keywords.
- `train_model.py`: Contains functions to train and save the machine learning model.
- `predict_emails.py`: Contains functions to predict email labels using the trained model.
- `extract_pdfs.py`: Contains functions to extract PDF attachments from emails.
- `extract_metadata.py`: Contains functions to extract metadata from emails.
- `categorize_emails.py`: Contains functions to categorize emails in Gmail.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Pip package manager
- Google Drive API credentials (for saving PDFs)
- Gmail API credentials (for email categorization)

### Installation 
To install the required SpaCy model, run the following command:
```
python -m spacy download en_core_web_sm
```