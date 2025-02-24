#!/usr/bin/env python3
"""
Script to fetch publications from PubMed and store them as YAML for a Hydejack site.
"""

import os
import sys
import yaml
from datetime import datetime
from Bio import Entrez, Medline

# Configuration
PUBMED_QUERY = os.environ.get('PUBMED_QUERY', 'YOUR_NAME[Author]')  # Default to author search
PUBMED_EMAIL = os.environ.get('PUBMED_EMAIL', 'your.email@example.com')
MAX_RESULTS = 100  # Maximum number of results to fetch
OUTPUT_FILE = '_data/publications.yml'  # Path to save the YAML file

def fetch_pubmed_records(query, max_count=MAX_RESULTS):
    """Fetch records from PubMed based on the query."""
    Entrez.email = PUBMED_EMAIL
    
    # Search PubMed
    search_handle = Entrez.esearch(db="pubmed", term=query, retmax=max_count)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    
    id_list = search_results["IdList"]
    if not id_list:
        print(f"No results found for query: {query}")
        return []
    
    # Fetch details for each article
    fetch_handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text")
    records = list(Medline.parse(fetch_handle))
    fetch_handle.close()
    
    return records

def format_publication(record):
    """Format a PubMed record as a dictionary for YAML."""
    publication = {
        'title': record.get('TI', 'No Title'),
        'authors': record.get('AU', []),
        'journal': record.get('JT', 'No Journal'),
        'year': record.get('DP', 'No Date')[:4],  # Extract year from date
        'pmid': record.get('PMID', ''),
        'doi': record.get('LID', '').replace(' [doi]', '') if 'LID' in record else '',
        'url': f"https://pubmed.ncbi.nlm.nih.gov/{record.get('PMID', '')}/",
    }
    
    # Clean up and validate
    if not publication['doi'] and 'AID' in record:
        for aid in record['AID']:
            if aid.endswith('[doi]'):
                publication['doi'] = aid.replace(' [doi]', '')
                break
    
    # Extract abstract if available
    if 'AB' in record:
        publication['abstract'] = record['AB']
    
    return publication

def main():
    """Main function to fetch and save PubMed records."""
    print(f"Fetching publications for query: {PUBMED_QUERY}")
    records = fetch_pubmed_records(PUBMED_QUERY)
    
    if not records:
        print("No publications found. Exiting.")
        return
    
    print(f"Found {len(records)} publications")
    
    # Format publications
    publications = [format_publication(record) for record in records]
    
    # Sort by year (descending)
    publications.sort(key=lambda x: x['year'], reverse=True)
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    # Save as YAML
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(publications, f, allow_unicode=True, sort_keys=False)
    
    print(f"Saved {len(publications)} publications to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
