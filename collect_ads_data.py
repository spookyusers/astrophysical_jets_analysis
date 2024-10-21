import ads
import os

# Set up the ADS API token
os.environ['ADS_DEV_KEY'] = 'MwBqze0JeTuhIWaC5DsC1ymsKC5kRWDj16gyM5p7'

# Query ADS for papers related to black hole masses and jet lengths
query = ads.SearchQuery(q="black hole mass jet length", fl=["title", "author", "year", "bibcode", "abstract"], rows=10)

# Gather information on the papers found
papers_data = []
for paper in query:
    papers_data.append({
        "Title": paper.title[0] if paper.title else "No Title",
        "Authors": ", ".join(paper.author) if paper.author else "Unknown Authors",
        "Year": paper.year,
        "Bibcode": paper.bibcode,
        "Abstract": paper.abstract if paper.abstract else "No Abstract"
    })

# Output the results to the console for now
for paper in papers_data:
    print(f"Title: {paper['Title']}")
    print(f"Authors: {paper['Authors']}")
    print(f"Year: {paper['Year']}")
    print(f"Bibcode: {paper['Bibcode']}")
    print(f"Abstract: {paper['Abstract'][:200]}...")  # Show only first 200 characters of the abstract
    print("-----")

# Optional: You could save this data to a CSV for further review if needed
import pandas as pd

df = pd.DataFrame(papers_data)
df.to_csv("ads_black_hole_papers.csv", index=False)
print("Data collection complete. Saved to ads_black_hole_papers.csv")

