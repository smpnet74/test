import requests
from bs4 import BeautifulSoup

base_url = "http://www.pulumi.com/blog"
page_num = 1
links = []

while True:
    # Construct the URL for the current page
    if page_num == 1:
        url = base_url
    else:
        url = f"{base_url}/page/{page_num}/"

    # Send a GET request to the current page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the <h1> tag with class "no-anchor"
    h1_tag = soup.find("h1", class_="no-anchor")

    # Break the loop if we've found the 404 page
    if h1_tag and h1_tag.text.strip() == "404":
        break

    # Find all the <a> tags that have an href attribute starting with "/blog/"
    page_links = soup.find_all("a", href=lambda href: href and href.startswith("/blog/"))

    # Filter out links that have author, tag, or page in the URL
    filtered_links = []
    for link in page_links:
        url = link["href"]
        if "author" not in url and "tag" not in url and "page" not in url:
            filtered_links.append(f"http://www.pulumi.com{url}")

    # Remove duplicates from the list of links and append to the master list
    unique_links = list(set(filtered_links))
    links.extend(unique_links)

    # Increment the page number for the next iteration
    page_num += 1

# Remove links that are 6 characters long
final_links = [link for link in links if len(link) != 27]

# Print the final list of links
print("Final links:")
for link in final_links:
    print(link)
