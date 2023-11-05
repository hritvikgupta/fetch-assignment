from flask import Flask, render_template, request 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import spacy
import pandas as pd
import numpy as np
from helper import GetOffers
from getDataset import brand, categories, offers

app = Flask(__name__)
offers_model = GetOffers()
all_texts = offers['OFFER'].tolist()
offers_model.vectorizer.fit(all_texts)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    The index route that handles the search functionality. On a POST request, it gets the
    user's query, searches for relevant offers, calculates similarity scores, sorts the results
    by score, and renders them on the index.html page. On a GET request, it simply renders the
    page without results.
    """
    if request.method == 'POST':
        query = request.form['query'].strip()
        results = offers_model.search_offers(query)
        offer_texts = [res[0] for res in results]
        if len(offer_texts) > 0:
            similarity_scores = offers_model.get_similarity_scores(query, offer_texts)
            sorted_results = sorted([(offer, match_type, score) for (offer, match_type), score in zip(results, similarity_scores)], key=lambda x: x[2], reverse=True)
        else:
            sorted_results = []

        return render_template('index.html', results=sorted_results)
    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)
