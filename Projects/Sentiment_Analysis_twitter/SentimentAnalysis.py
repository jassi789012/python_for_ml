import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


df = pd.read_csv('Projects\\twitter_training.csv')

# print(df.columns)
# print(df.shape)
# print(df.head(10))
# print(df.tail(10))
# print(df['Positive'] == 'Positive')
# print(df.isnull().sum())
# print(df.value_counts())
# print(df.info())

print("Total missing values in each column:")
print(df.isnull().sum())

new_column_names = ['ID', 'Entity', 'Sentiment', 'Text']

df.columns = new_column_names

print("Column names have been fixed successfully!")
print("Your new columns are:", df.columns.tolist())

df.dropna(subset=['Text'], inplace=True)

print("\nTotal missing values after cleaning:")
print(df.isnull().sum())


# The corrected version of the cleaning function.
# Notice the change to 'stop_words' in the middle of the function.

def clean_text_fully(text):
    # Convert to string and lowercase
    text = str(text).lower()
    # Remove punctuation, etc.
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize and remove stop words
    words = text.split()
    # THE FIX IS HERE: We use 'stop_words' with an underscore
    words = [word for word in words if word not in stop_words]
    
    # Stemming
    stemmed_words = [stemmer.stem(word) for word in words]
    
    # Join back to a single string and return the result
    return ' '.join(stemmed_words)

# --- After replacing the function, you can run the .apply() command again ---

print("Starting to clean all tweets with the corrected function...")

df['clean_text'] = df['Text'].apply(clean_text_fully)

print("All tweets have been cleaned successfully!")

print("\nHere is a comparison of the original 'Text' and the new 'clean_text' column:")
print(df[['Text', 'clean_text']].head())

X = df['clean_text']

y = df['Sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nData has been split into training and testing sets.")
print(f"Training set has {len(X_train)} entries.")
print(f"Testing set has {len(X_test)} entries.")



print("Converting text to numbers (Vectorizing)...")
# Create the vectorizer object
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
# Use the same learned vocabulary to transform the testing data
X_test_tfidf = vectorizer.transform(X_test)

print("Vectorization complete.")

model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)

print("Model training complete.")

y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)

print("\n--- MODEL EVALUATION COMPLETE ---")
print(f"The accuracy of our model is: {accuracy:.4f}")
print(f"(This means the model correctly predicted the sentiment for {accuracy:.2%} of the tweets in the test set.)")


# --- BONUS STEP: Build a Predictive System ---

def predict_sentiment(new_text):
    # 1. We use our existing function to clean the new text
    cleaned_text = clean_text_fully(new_text)
    
    # 2. We use our fitted vectorizer to convert the text to numbers
    # NOTE: We use .transform() here because the vectorizer is already trained.
    # We put the text in a list [ ] because the vectorizer expects a list of documents.
    vectorized_text = vectorizer.transform([cleaned_text])
    
    # 3. We use our trained model to predict the sentiment
    prediction = model.predict(vectorized_text)
    
    # The result is an array (e.g., ['Positive']), so we take the first element.
    return prediction[0]

# --- Let's test it! ---
my_positive_tweet = "I am having such a great time, this is the best day ever!"
my_negative_tweet = "This was a horrible experience, I am so disappointed and angry."
my_neutral_tweet = "I am going to the store this afternoon."

print("\n--- Testing with new sentences ---")
print(f"Prediction for '{my_positive_tweet}': {predict_sentiment(my_positive_tweet)}")
print(f"Prediction for '{my_negative_tweet}': {predict_sentiment(my_negative_tweet)}")
print(f"Prediction for '{my_neutral_tweet}': {predict_sentiment(my_neutral_tweet)}")