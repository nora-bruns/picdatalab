import requests
import xml.etree.ElementTree as ET
import json
import os

# Define the search term and PubMed API URL
SEARCH_TERM = "machine learning"
PUBMED_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Define output directory in the root (publications/)
OUTPUT_DIR = "publications"
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure directory exists

# Define parameters for searching PubMed
params = {
    "db": "pubmed",
    "term": SEARCH_TERM,
    "retmode": "json",
    "retmax": 10  # Number of articles to fetch
}

# Fetch article IDs
response = requests.get(PUBMED_URL, params=params)
data = response.json()
article_ids = data["esearchresult"]["idlist"]

# Dictionary to store articles grouped by year
articles_by_year = {}

# Fetch article details if IDs are found
if article_ids:
    efetch_params = {
        "db": "pubmed",
        "id": ",".join(article_ids),
        "retmode": "xml"
    }
    article_data = requests.get(EFETCH_URL, params=efetch_params).text

    # Parse XML response
    root = ET.fromstring(article_data)
    
    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text
        title_elem = article.find(".//ArticleTitle")
        year_elem = article.find(".//PubDate/Year
