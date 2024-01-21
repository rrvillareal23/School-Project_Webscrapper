# School-Project_Webscrapper

## Overview
This Python script is designed to perform web scraping on a specified URL (`https://casl.website/`) using the BeautifulSoup library. It extracts and presents information such as the page title, URLs of links, and downloads images found on the page. Additionally, the extracted data is saved to a text file named `extracted_data.txt`.

## Prerequisites
Before running the script, ensure that you have the following installed:
- Python
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage
1. Clone or download the repository containing the script.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the script using the command: `python script_name.py` (replace `script_name` with the actual script filename).

## Script Explanation
The script follows these main steps:

1. Sends an HTTP GET request to the specified URL (`https://casl.website/`).
2. Checks if the request was successful (status code 200).
3. Parses the HTML content of the page using BeautifulSoup.
4. Extracts and prints the page title.
5. Extracts and prints URLs of links found on the page.
6. Downloads images found on the page and saves them locally.
7. Saves the extracted data (page title, links, and images) to a text file (`extracted_data.txt`).
8. Displays a message indicating the completion of the script.

## File Descriptions
- `script_name.py`: The main Python script.
- `extracted_data.txt`: Text file containing the extracted data.

## Notes
- Ensure that the provided URL is accessible and returns a status code of 200.
- Make sure to handle potential errors or exceptions during the script execution.

Feel free to customize the script based on your specific requirements or target websites.
