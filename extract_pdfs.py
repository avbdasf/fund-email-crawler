import pandas as pd
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from urllib.parse import urlparse
import email
from bs4 import BeautifulSoup

# Authenticate and create the PyDrive client
def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
    drive = GoogleDrive(gauth)
    return drive

# Function to save PDF from URL to Google Drive
def save_pdf_to_drive(content, file_name, drive, folder_id=None):
    try:
        print(f"Saving PDF: {file_name}")
        temp_file_path = os.path.join("/tmp", file_name)  # Save to temporary directory
        with open(temp_file_path, 'wb') as f:
            f.write(content)
        file = drive.CreateFile({'title': file_name, 'parents': [{'id': folder_id}] if folder_id else []})
        file.SetContentFile(temp_file_path)
        file.Upload()
        print(f"Uploaded PDF: {file_name}")
        os.remove(temp_file_path)  # Remove temporary file after upload
        return True
    except Exception as e:
        print(f"An error occurred while saving PDF {file_name}: {e}")
        return False

def is_pdf_link(url):
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get('Content-Type', '')
        if 'pdf' in content_type.lower():
            return True
        # Check for known PDF content-disposition header
        content_disposition = response.headers.get('Content-Disposition', '')
        if 'attachment' in content_disposition.lower() and 'pdf' in content_disposition.lower():
            return True
    except Exception as e:
        print(f"Failed to check link {url}: {e}")
        return False

def extract_and_save_pdfs(input_csv):
    drive = authenticate_drive()
    df = pd.read_csv(input_csv)
    
    # Create a folder in Google Drive (if not exists)
    folder_metadata = {
        'title': 'Monthly_Update_Files',
        'mimeType': 'application/vnd.google-apps.folder'
    }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    folder_id = folder['id']
    print(f"Folder created with ID: {folder_id}")
    
    # Add a new column to flag emails with no files downloaded
    df['Files_Downloaded'] = False
    
    for index, row in df.iterrows():
        if row["Final_Label"] == 1:
            print(f"Processing email {index} with links: {row['Links']}")
            try:
                links = eval(row["Links"])
            except Exception as e:
                print(f"Failed to parse links for email {index}: {e}")
                continue
            files_downloaded = False
            for link in links:
                if is_pdf_link(link):
                    try:
                        response = requests.get(link)
                        file_name = f"email_{index}_{os.path.basename(urlparse(link).path)}"
                        if save_pdf_to_drive(response.content, file_name, drive, folder_id):
                            files_downloaded = True
                    except Exception as e:
                        print(f"An error occurred while downloading PDF {link}: {e}")
                else:
                    print(f"Link is not a PDF: {link}")
            df.at[index, 'Files_Downloaded'] = files_downloaded
    
    # Save the updated DataFrame to a new CSV file
    output_file = 'data/updated_final_labeled_emails.csv'
    df.to_csv(output_file, index=False)
    print(f"Updated emails saved to {output_file}")

if __name__ == "__main__":
    extract_and_save_pdfs("data/final_labeled_emails.csv")
