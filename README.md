# fetch-assignment
### Offers Search Flask Application
#### Application is live on: https://flask-offer-app-a79411e7ba39.herokuapp.com

## Introduction
This Flask application enables users to search for special offers based on various criteria such as product categories, brands, and retailers. It leverages Natural Language Processing (NLP) techniques to evaluate the relevance and similarity of offers to the user's search query. This python flask application is hosted on heroku.

## Features

- Search offers by keywords
- Ranking of offers based on relevance
- Display of search results with similarity scores

  All the other necessary details are listed in file  https://github.com/hritvikgupta/fetch-assignment/blob/main/Documentation.txt

## Installation

Before you can run the application, ensure you have Python installed on your system.

To get started, clone this repository to your local machine: 

```bash
git clone https://your-repository-link
cd your-repository-directory

Install the required Python packages:
pip install -r requirements.txt

To start the application, run the following command in your terminal:
flask run

Either if above doesn't work just run python app.py and it run the application on local terminal for output to be displayed.
```
More Instructions to run locally is on: https://github.com/hritvikgupta/fetch-assignment/blob/main/Instructions.txt
The application will start running on http://localhost:5000. Navigate to this address in your web browser to use the application.

```bash
In getDataset.py
Rename the variable if you are running from local system
brand = pd.read_csv("ADD BRAND CSV FILE PATH") 
categories = pd.read_csv("ADD CATEGORY CSV FILE PATH")
offers = pd.read_csv("ADD OFFERS CSV FILE PATH")

```

## How It Works
1. Data Preparation
  Upon initialization, the application loads the datasets and creates a TF-IDF matrix to understand the context of offers.

2. Search Algorithm
  When a user submits a query, the application performs a case-insensitive search across categories, brands, and retailers to find relevant offers.

3. Similarity Scoring
  The application calculates similarity scores using both TF-IDF cosine similarity and spaCy's semantic similarity to rank the offers.

## Technologies Used
1. Flask for the web framework
2. Pandas for data manipulation
3. NumPy for numerical operations
4. Scikit-learn for machine learning utilities
5. spaCy for advanced NLP operations

## File Structure
1. app.py - The main Flask application file with route definitions.
2. helper.py - Contains the GetOffers class with NLP and search functionality.
3. getDataset.py - Script to load datasets of brands, categories, and offers.
4. templates/ - Folder containing the HTML templates.

Acknowledgements
Thanks for giving me the opportunity to work on this assignment. I look forward to you positive feedback.


