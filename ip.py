from selenium import webdriver
from bs4 import BeautifulSoup
import re

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# Define the URL to scrape
url = "https://myip.ms/browse/blacklist/Blacklist_IP_Blacklist_IP_Addresses_Live_Database_Real-time"  
# Open the URL
driver.get(url)

# Get the page source
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Print page text to verify content
page_text = soup.get_text()
print("Page Text:", page_text[:500])  # Print first 500 characters for inspection

# Use regular expressions to find IP addresses
ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
matches = ip_pattern.findall(page_text)

# Print the matched IP addresses
if matches:
    print("Matches found:", matches)
else:
    print("No IP addresses found.")

# Close the driver
driver.quit()
