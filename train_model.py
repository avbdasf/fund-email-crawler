import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from sklearn.metrics import classification_report
import os

def train_and_save_model(input_csv, model_filepath):
    df = pd.read_csv(input_csv)
    X = df["Parsed_Text"].fillna("")  # Replace NaN with empty string
    y = df["Label"]

    # Using a pipeline to include feature extraction and model training
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
        ('clf', LogisticRegression(class_weight='balanced'))  # Added class_weight='balanced' to handle class imbalance
    ])

    # Using GridSearchCV to find the best parameters
    parameters = {
        'tfidf__max_df': [0.9, 0.95, 1.0],
        'tfidf__min_df': [1, 2, 5],
        'clf__C': [0.1, 1, 10]
    }

    grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
    grid_search.fit(X, y)

    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best cross-validation score: {grid_search.best_score_}")

    # Train the final model with the best parameters
    final_model = grid_search.best_estimator_
    final_model.fit(X, y)

    # Save the trained model pipeline
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(model_filepath), exist_ok=True)
    joblib.dump(final_model, model_filepath)

    # Display classification report
    y_pred = final_model.predict(X)
    print(classification_report(y, y_pred))

if __name__ == "__main__":
    train_and_save_model("data/labeled_emails.csv", "models/email_classifier.pkl")
