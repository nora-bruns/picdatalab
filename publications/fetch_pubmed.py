import requests
import xml.etree.ElementTree as ET
import json

# Define the search term and PubMed API URL
SEARCH_TERM = "machine learning"
PUBMED_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

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
        year_elem = article.find(".//PubDate/Year")

        title = title_elem.text if title_elem is not None else "No title available"
        year = year_elem.text if year_elem is not None else "Unknown"

        # Group articles by year
        if year not in articles_by_year:
            articles_by_year[year] = []
        
        articles_by_year[year].append({"id": pmid, "title": title})

    # Save to a JSON file
    with open("docs/pubmed.json", "w", encoding="utf-8") as f:
        json.dump(articles_by_year, f, indent=4)

    print("PubMed data updated successfully.")
else:
    print("No articles found.")
