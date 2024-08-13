import pandas as pd

initial_keywords = [
    "monthly update", "Monthly Update", "MONTHLY UPDATE",
    "January update", "january update", "JANUARY UPDATE",
    "February update", "february update", "FEBRUARY UPDATE",
    "March update", "march update", "MARCH UPDATE",
    "April update", "april update", "APRIL UPDATE",
    "May update", "may update", "MAY UPDATE",
    "June update", "june update", "JUNE UPDATE",
    "July update", "july update", "JULY UPDATE",
    "August update", "august update", "AUGUST UPDATE",
    "September update", "september update", "SEPTEMBER UPDATE",
    "October update", "october update", "OCTOBER UPDATE",
    "November update", "november update", "NOVEMBER UPDATE",
    "December update", "december update", "DECEMBER UPDATE",
    "2024 update", "Monthly Report"
]

def label_email(text):
    if isinstance(text, str):
        for keyword in initial_keywords:
            if keyword in text:
                return 1
    return 0

def label_emails_with_keywords(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df["Label"] = df["Parsed_Text"].apply(label_email)
    update_count = df["Label"].sum()
    non_update_count = len(df) - update_count
    print(f"Number of emails labeled as updates: {update_count}")
    print(f"Number of emails labeled as non-updates: {non_update_count}")
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    label_emails_with_keywords("data/parsed_emails.csv", "data/labeled_emails.csv")
