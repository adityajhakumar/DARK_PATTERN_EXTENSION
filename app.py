from flask import Flask, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
import time
import spacy

app = Flask(__name__)

# Download spaCy English model
spacy.cli.download("en_core_web_sm")

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Define the new file ID from the updated Google Drive link
new_file_id = '1OTfNifGO_71pl1f8X2N-a0M4PaZhiDZd'

# Construct the new download link
new_download_link = f'https://drive.google.com/uc?id={new_file_id}'

# Make a request to download the new file
response = requests.get(new_download_link)
# Save the downloaded file to the destination path
destination_path = 'output.csv'  # Modify the destination path as needed
with open(destination_path, 'wb') as f:
    f.write(response.content)

# Load the dataset from the updated CSV file
df = pd.read_csv(destination_path, encoding='latin-1')

# Split the dataset into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Extract features from 'text' column using TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(train_df['text'])

# Extract labels from 'label' column
y_train = train_df['label']

# Use Support Vector Machine with GridSearch for hyperparameter tuning
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly'], 'gamma': ['scale', 'auto']}
svm_clf = SVC(random_state=42)
grid_search = GridSearchCV(svm_clf, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best model from the grid search
best_svm_model = grid_search.best_estimator_

def scrape_website_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        time.sleep(2)  # Add a delay to avoid overloading the server
        soup = BeautifulSoup(response.text, 'html.parser')
        text_data = [element.get_text(strip=True) for element in soup.find_all(True)]
        return text_data
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the website. Error: {e}")
        return None

def analyze_text_with_nlp(text_data):
    analyzed_data = []
    for line in text_data:
        doc = nlp(line)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        tokens = [token.text for token in doc]
        pos_tags = [token.pos_ for token in doc]
        dependencies = [(token.text, token.dep_) for token in doc]
        analyzed_data.append({
            'text': line,
            'entities': entities,
            'tokens': tokens,
            'pos_tags': pos_tags,
            'dependencies': dependencies
        })
    return analyzed_data

def identify_dark_patterns(text_data, dark_patterns_column):
    identified_patterns_list = []
    for line in text_data:
        identified_patterns = dark_patterns_column.apply(lambda pattern: pattern.lower() in line.lower())
        identified_patterns_list.append(identified_patterns.tolist())
    return identified_patterns_list

# Flask route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for processing the form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        website_url = request.form['website_url']
        webpage_text_data = scrape_website_text(website_url)

        if webpage_text_data:
            transformed_text = vectorizer.transform(webpage_text_data)
            predictions = best_svm_model.predict(transformed_text)

            analyzed_text_data = analyze_text_with_nlp(webpage_text_data)
            identified_patterns_list = identify_dark_patterns(webpage_text_data, test_df['Pattern Category'])

            min_length = min(len(webpage_text_data), len(predictions), min(len(lst) for lst in identified_patterns_list))

            webpage_text_data = webpage_text_data[:min_length]
            predictions = predictions[:min_length]
            analyzed_text_data = analyzed_text_data[:min_length]
            identified_patterns_list = [lst[:min_length] for lst in identified_patterns_list]

            result_df = pd.DataFrame({
                'Text': webpage_text_data,
                'Prediction': predictions,
                'Analyzed_Text': analyzed_text_data,
                'Identified_Patterns': identified_patterns_list[0],
                'Pattern_Category': test_df['Pattern Category'].tolist()[:min_length]
            })

            correct_predictions_df = result_df[result_df['Prediction'] == 1].drop_duplicates(subset=['Text'])

            if not correct_predictions_df.empty:
                return render_template('result.html', result_df=correct_predictions_df.to_html())
            else:
                return "No correct predictions or identified dark patterns found."
        else:
            return "Failed to scrape the website. Please check the URL and try again."

if __name__ == '__main__':
    app.run(debug=True)
