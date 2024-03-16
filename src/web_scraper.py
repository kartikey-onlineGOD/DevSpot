import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def scrape_devpost(link):
    # Send a GET request to the provided link
    print("Entered")
    response = requests.get(link)
    print(response.status_code)

    # Extract project title
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title_elem = soup.find('h1')
        title = title_elem.get_text(strip=True) if title_elem else None

        description = ''
        details_container = soup.find(id='app-details-left')
        if details_container:
            for heading in details_container.find_all('h2'):
                description += heading.get_text(strip=True) + '\n'
                next_element = heading.find_next_sibling()
                while next_element and next_element.name != 'h2':
                    if next_element.name == 'p':
                        description += next_element.get_text(strip=True) + '\n'
                    next_element = next_element.find_next_sibling()


        project_details = {'title': title, 'description': description.strip()}

        return project_details
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None
