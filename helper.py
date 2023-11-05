import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import spacy
from getDataset import brand, categories, offers
nlp = spacy.load("en_core_web_sm")

class GetOffers():
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        
    def search_offers(self, query):
        """
        Search for offers based on a query. The method searches within product categories,
        brands, and retailers to find matches. It returns a list of tuples containing the
        offer and the type of match it found (Category Match, Brand Match, or Retailer Match).
        """
        results = []
        matching_categories = categories[categories['PRODUCT_CATEGORY'].str.contains(query, case=False)]
        if not matching_categories.empty:
            brands_for_category = brand[brand['BRAND_BELONGS_TO_CATEGORY'].isin(matching_categories['PRODUCT_CATEGORY'])]
            for _, row in brands_for_category.iterrows():
                matching_offers = offers[offers['BRAND'].str.contains(row['BRAND'], case=False)]
                for _, offer_row in matching_offers.iterrows():
                    results.append((offer_row['OFFER'], "Category Match"))

        matching_brands = brand[brand['BRAND'].str.contains(query, case=False)]
        if not matching_brands.empty:
            for _, row in matching_brands.iterrows():
                matching_offers = offers[offers['BRAND'].str.contains(row['BRAND'], case=False)]
                for _, offer_row in matching_offers.iterrows():
                    results.append((offer_row['OFFER'], "Brand Match"))
        else:
            matching_categories = brand[brand['BRAND'].str.contains(query, case=False)]['BRAND_BELONGS_TO_CATEGORY']
            for category in matching_categories:
                brands_for_category = brand[brand['BRAND_BELONGS_TO_CATEGORY'] == category]
                for _, row in brands_for_category.iterrows():
                    matching_offers = offers[offers['BRAND'].str.contains(row['BRAND'], case=False)]
                    for _, offer_row in matching_offers.iterrows():
                        results.append((offer_row['OFFER'], f"Category Match for Brand: {query}"))

        matching_offers = offers[offers['RETAILER'].str.contains(query, case=False)]
        for _, offer_row in matching_offers.iterrows():
            results.append((offer_row['OFFER'], "Retailer Match"))
        return results

    def get_similarity_scores(self, query, texts):
        """
        Calculate similarity scores between the query and a list of texts using TF-IDF vectorization
        and cosine similarity. It also adds a bias score if the query is a substring of the text to 
        enhance the match quality.
        """
        tfidf_matrix = self.vectorizer.transform(texts)
        query_vec = self.vectorizer.transform([query])
        cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
        for i, text in enumerate(texts):
            if query.lower() in text.lower():
                cosine_similarities[i] += 0.5  
        return np.clip(cosine_similarities, 0, 1)

    def get_spacy_similarity(self, query, texts):
        """
        Calculate similarity scores between the query and a list of texts using spaCy's built-in
        similarity comparison, which is based on word embeddings.
        """
        query_doc = nlp(query)
        similarities = [query_doc.similarity(nlp(text)) for text in texts]
        return similarities