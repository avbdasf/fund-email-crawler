import pandas as pd
from bs4 import BeautifulSoup

def parse_email_body(body):
    if isinstance(body, str):
        soup = BeautifulSoup(body, "html.parser")
        text = soup.get_text()
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return text, links
    return "", []

def parse_email_bodies(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df["Parsed_Text"] = df["Body"].apply(lambda x: parse_email_body(x)[0])
    df["Links"] = df["Body"].apply(lambda x: parse_email_body(x)[1])
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    parse_email_bodies("data/emails.csv", "data/parsed_emails.csv")
