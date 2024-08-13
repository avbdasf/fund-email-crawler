import pandas as pd
import re
import spacy
from dateutil.parser import parse

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_metadata(subject):
    # Extract date using dateutil
    date = None
    try:
        date = parse(subject, fuzzy=True)
    except ValueError:
        pass
    
    # Extract potential fund name using spaCy
    doc = nlp(subject)
    fund_name = " ".join([ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE"]])
    
    if date:
        date_str = date.strftime('%Y-%m-%d')
    else:
        date_str = None
    
    return fund_name, date_str

def extract_and_save_metadata(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df["Fund_Name"], df["Update_Date"] = zip(*df["Subject"].apply(extract_metadata))
    df[["Fund_Name", "Update_Date"]].to_csv(output_csv, index=False)

if __name__ == "__main__":
    extract_and_save_metadata("data/final_labeled_emails.csv", "data/email_metadata.csv")
