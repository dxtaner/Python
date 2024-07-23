import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# %% Load Twitter Data
data = pd.read_csv("gender_classifier.csv", encoding="latin1")
data = pd.concat([data['gender'], data['description']], axis=1)
data.dropna(inplace=True)
data['gender'] = data['gender'].apply(lambda x: 1 if x == "female" else 0)

# %% Data Cleaning
def clean_description(text):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub("[^a-zA-Z]", " ", text).lower()
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stopwords
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return " ".join(tokens)

# Apply cleaning function to all descriptions
data['cleaned_description'] = data['description'].apply(clean_description)

# %% Bag of Words Representation
max_features = 5000
count_vectorizer = CountVectorizer(max_features=max_features, stop_words="english")
sparce_matrix = count_vectorizer.fit_transform(data['cleaned_description']).toarray()

print(f"Top {max_features} most used words: {count_vectorizer.get_feature_names_out()}")

# %% Prepare Data for Model
X = sparce_matrix
y = data['gender'].values

# Train-Test Split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# %% Naive Bayes Classification
nb = GaussianNB()
nb.fit(x_train, y_train)

# %% Predictions and Evaluation
y_pred = nb.predict(x_test)
accuracy = nb.score(x_test, y_test)
print(f"Accuracy: {accuracy:.2f}")
