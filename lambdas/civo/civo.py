import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):   
    # Define the base URL and starting page number
    base_url = 'https://www.civo.com/blog'
    page_num = 1

    # Create an empty list to store the full URLs of all the links
    full_links = []

    while True:
        # Construct the URL for the current page
        url = f'{base_url}?page={page_num}'

        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the div containing the links
        div = soup.select_one('body > main > div.container > div > div:nth-child(1) > div > div')

        # Extract all the links within the div and add them to the full_links list
        links = div.find_all('a')
        full_links += [f'https://www.civo.com{link.get("href")}' for link in links]

        # Check if there are no blog posts on this page (i.e., we've reached the last page)
        if len(links) == 0:
            break

        # Increment the page number and continue to the next page
        page_num += 1

    # Print the full URLs of all the links
    for link in full_links:
        print(link)
    return(full_links)
