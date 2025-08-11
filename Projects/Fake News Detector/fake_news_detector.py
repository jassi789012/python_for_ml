import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df_fake = pd.read_csv('Projects\\Fake News Detector\\Fake.csv')
df_true = pd.read_csv('Projects\\Fake News Detector\\True.csv')

# print(df_fake.head())
# print(df_true.head())

df_fake['label'] = 0
df_true['label'] = 1

df_combined = pd.concat([df_fake, df_true])[['text', 'label']]


df = df_combined.sample(frac=1, random_state=42).reset_index(drop=True)

labels = df['label']

# stop_words='english' removes common English words like 'the', 'a', 'in'
# max_df=0.7 ignores words that appear in more than 70% of the articles (as they are too common to be useful)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

tfidf_matrix = tfidf_vectorizer.fit_transform(df['text'])

print("\nThe text data has been converted into a numerical matrix.")

# print(tfidf_matrix)

X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

pac = PassiveAggressiveClassifier(max_iter=50)

pac.fit(X_train, y_train)

y_pred = pac.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

def classify_news(news_text):

    vectorized_text = tfidf_vectorizer.transform([news_text])

    prediction = pac.predict(vectorized_text)
    
    if prediction[0] == 0:
        return "This looks like FAKE news."
    else:
        return "This looks like REAL news."
    
fake_news_example = "NASA confirms Earth is flat and the moon landing was a hoax filmed in a desert."
real_news_example = "The Indian Space Research Organisation (ISRO) successfully launched its latest communication satellite, GSAT-30, from Kourou launch base in French Guiana on Friday."

print("\n--- Testing with a new headline ---")
print(f"Headline 1: {fake_news_example}")
print(f"Prediction: {classify_news(fake_news_example)}\n")

print(f"Headline 2: {real_news_example}")
print(f"Prediction: {classify_news(real_news_example)}")