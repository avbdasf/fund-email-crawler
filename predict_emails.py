import pandas as pd
import joblib

def predict_and_save_labels(input_csv, model_filepath, output_csv):
    final_model = joblib.load(model_filepath)

    df = pd.read_csv(input_csv)
    df["Parsed_Text"] = df["Parsed_Text"].fillna("")  # Replace NaN with empty string

    df["Final_Label"] = final_model.predict(df["Parsed_Text"])

    print(f"Number of emails labeled as updates: {df['Final_Label'].sum()}")
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    predict_and_save_labels("data/parsed_emails.csv", "models/email_classifier.pkl", "data/final_labeled_emails.csv")
