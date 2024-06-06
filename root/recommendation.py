import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import HackathonRecord
from django_pandas.io import read_frame


class RecommendationSystemWrapper:
    def __init__(self, query):
        self.query = query
        self.df = self.load_data()
        self.vectorizer = TfidfVectorizer()
        self.setup_nltk()
        if not self.df.empty:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.df['cleaned_combined'])

    def setup_nltk(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def load_data(self):
        try:
            
            # df = pd.read_csv(self.dataset_path)
            records = HackathonRecord.objects.all()
            df = read_frame(records)
            print('working 31')
            print(df.to_csv('djangoset.csv'))
            print('working 33')
            print('working 34')
            df['combined'] = df['problem_statement'].astype(str) + " " + df['tech'] + " " + df['tag'].astype(str)
            print(df['combined'])
            df['cleaned_combined'] = df['combined'].apply(self.clean_text)
            print('working 41')
            return df.drop_duplicates(subset=['cleaned_combined'])
        except Exception as e:
            print(e)
            return pd.DataFrame()

    def clean_text(self, text):
        stop_words = set(stopwords.words('english'))
        stemmer = PorterStemmer()
        tokens = word_tokenize(text.lower())
        filtered_tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
        return " ".join(filtered_tokens)

    def get_recommendations(self, query):
        if self.df.empty:
            return "No data loaded."
        query_keywords = self.extract_keywords(query)
        doc_vector = self.vectorizer.transform([' '.join(query_keywords)])
        similarities = cosine_similarity(doc_vector, self.tfidf_matrix).flatten()
        self.df['similarity_score'] = similarities
        sorted_df = self.df.sort_values(by='similarity_score', ascending=False)
        return sorted_df.head(5)['problem_statement'].tolist()

    def extract_keywords(self, text):
        cleaned_text = self.clean_text(text)
        tfidf_vector = self.vectorizer.transform([cleaned_text])
        sorted_items = tfidf_vector.toarray().flatten().argsort()[::-1]
        feature_array = self.vectorizer.get_feature_names_out()
        return feature_array[sorted_items][:5]
