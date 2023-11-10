import requests
from bs4 import BeautifulSoup
import csv

# Function to perform web scraping
def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: extracting all the links on the page
        links = [link.get('href') for link in soup.find_all('a')]
        return links
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Function to perform API request
def fetch_api_data(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        return None

# Function to save data to CSV file
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write header if needed
        # writer.writerow(['Column1', 'Column2', ...])
        for row in data:
            writer.writerow([row])

if __name__ == "__main__":
    # URL of the website to scrape
    website_url = 'https://example.com'
    # API endpoint to fetch data
    api_url = 'https://api.example.com/data'

    # Perform web scraping
    scraped_links = scrape_website(website_url)

    # Perform API request
    api_data = fetch_api_data(api_url)

    # Save the data to CSV files
    if scraped_links:
        save_to_csv(scraped_links, 'scraped_links.csv')

    if api_data:
        save_to_csv(api_data, 'api_data.csv')
