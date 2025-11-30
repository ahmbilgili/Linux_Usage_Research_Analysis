import requests
import time
import pandas as pd
import datetime
import calendar
import csv

# --- CONFIGURATION ---
# Optional: Add your GitHub Personal Access Token here to increase rate limits.
# If left empty, the script runs slower to respect anonymous limits (approx 10 req/min).
# With a token, you can do ~30 req/min.
GITHUB_TOKEN = "" 

KEYWORD = "linux"
START_YEAR = 2015  # GitHub launched in 2008
END_YEAR = datetime.date.today().year
CURRENT_MONTH = datetime.date.today().month

# Limit how many detailed repos to fetch per month to save time.
# GitHub Search API caps results at 1000 total.
MAX_RESULTS_PER_MONTH = 100 

def get_repo_details_for_month(year, month, token=None):
    """
    Queries GitHub Search API for repos created in a specific month
    containing the keyword. Returns a list of dicts with repo details.
    """
    url = "https://api.github.com/search/repositories"
    
    _, last_day = calendar.monthrange(year, month)
    start_date = f"{year}-{month:02d}-01"
    end_date = f"{year}-{month:02d}-{last_day}"
    
    # Query syntax: keyword + created range
    query = f"{KEYWORD} created:{start_date}..{end_date}"
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'

    all_repos = []
    page = 1
    per_page = 100 # Max allowed by API per request
    
    while len(all_repos) < MAX_RESULTS_PER_MONTH:
        params = {
            'q': query,
            'sort': 'stars', # Sort by stars to get the most relevant ones first
            'order': 'desc',
            'per_page': per_page,
            'page': page
        }

        try:
            response = requests.get(url, params=params, headers=headers)
            
            # Handle Rate Limiting
            if response.status_code in [403, 429]:
                print(f"\nRate limit hit for {start_date}. Waiting 60 seconds...")
                time.sleep(60)
                continue

            if response.status_code == 200:
                data = response.json()
                items = data.get('items', [])
                
                if not items:
                    break # No more results
                
                for item in items:
                    all_repos.append({
                        'Year': year,
                        'Month': month,
                        'Date': f"{year}-{month:02d}",
                        'Name': item.get('full_name'),
                        'Stars': item.get('stargazers_count', 0),
                        # Note: In Search API, watchers_count usually matches stars. 
                        # Real 'subscribers' requires individual calls per repo.
                        'Watchers': item.get('watchers_count', 0), 
                        'URL': item.get('html_url')
                    })
                    
                    if len(all_repos) >= MAX_RESULTS_PER_MONTH:
                        break
                
                page += 1
                # Respect Rate Limits between pages
                if not GITHUB_TOKEN:
                    time.sleep(6.5)
                else:
                    time.sleep(2)
            else:
                print(f"\nError fetching {start_date}: {response.status_code} - {response.text}")
                break
                
        except Exception as e:
            print(f"\nConnection error for {start_date}: {e}")
            break
            
    return all_repos

def main():
    print(f"--- Starting GitHub Monthly Repo Search for '{KEYWORD}' ---")
    print(f"Timeframe: {START_YEAR} to {END_YEAR}")
    print(f"Fetching details for top {MAX_RESULTS_PER_MONTH} repos per month (sorted by stars).")
    
    if not GITHUB_TOKEN:
        print("WARNING: No GITHUB_TOKEN provided. This will be slow.")
    
    results = []

    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, 13):
            # Stop if we reach the future
            if year == END_YEAR and month > CURRENT_MONTH:
                break
                
            print(f"Querying {year}-{month:02d}...", end=" ", flush=True)
            
            repos = get_repo_details_for_month(year, month, GITHUB_TOKEN)
            
            if repos:
                print(f"Fetched {len(repos)} repos.")
                results.extend(repos)
            else:
                print("No repos found or error.")

            # Sleep between months to be safe
            if not GITHUB_TOKEN:
                time.sleep(2) 
    idx = 0
    
    with open("github_repos_stars_watchers.csv", "w") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Year", "Month", "Day", "Name", "Stars", "Watchers", "URL"])
        for element in results:
            values = element.values()
            writer.writerow(values)

if __name__ == "__main__":
    main()