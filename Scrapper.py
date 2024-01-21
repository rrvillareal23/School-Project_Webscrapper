import requests
import os
from bs4 import BeautifulSoup

# Define the target URL
url = 'https://casl.website/'

# Send an HTTP GET request to the URL
page = requests.get(url)

# Check if the request was successful (status code 200)
if page.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Extract and print the page title
    page_title = soup.title.string
    print("page-title:")
    print(page_title)
    
    # Extract and print page links (URLs)
    links = soup.find_all('a', href=True)
    print("\npage-links URLs:")
    for link in links:
        newlink = link['href']
        print(newlink)
    
    # Extract and download images found on the page
    images = soup.find_all('img')
    print("\nimages found on the page:")
    for eachImage in images:
        img_url = eachImage['src']
        if not img_url.startswith('http'):
            img_url = url + img_url
        
        img_name = os.path.basename(img_url)
        try:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"Downloaded: {img_name}")
            else:
                print(f"Failed to download: {img_name}")
        except Exception as error:
            print(f"Error downloading {img_name}: {str(error)}")

    # Save the extracted data to a .txt file
    with open('extracted_data.txt', 'w') as txt_file:
        txt_file.write(f"Page Title: {page_title}\n\n")
        txt_file.write("Page Links:\n")
        for link in links:
            txt_file.write(link['href'] + '\n')
        
        txt_file.write("\nImages:\n")
        for eachImage in images:
            txt_file.write(eachImage['src'] + '\n')

    print("Data has been saved to 'extracted_data.txt'.")

else:
    print(f"Failed to retrieve the page. Status code: {page.status_code}")

print("\nScript Complete")
