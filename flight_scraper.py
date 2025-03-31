from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def get_flight_prices():
    # Setup Chrome with stealth options
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--start-maximized")  # Avoid bot detection

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open the flight website
        driver.get("https://flight.easemytrip.com/FlightList/Index?srch=DEL-Delhi-India|BOM-Mumbai-India|24/04/2025&px=1-0-0&cbn=0&ar=undefined&isow=true&isdm=true&lang=en-us&_gl=1*12484q2*_gcl_au*NjI4MjU1MDIxLjE3NDM0NDU0NTQ.*_ga*MTg5MjkyMjkwNC4xNzQzNDQ1NDU1*_ga_328ZMQHY8M*MTc0MzQ0NTQ1NC4xLjEuMTc0MzQ0NTQ1OC41Ni4wLjA.&IsDoubleSeat=false&CCODE=IN&curr=INR&apptype=B2C")
        time.sleep(5)  # Allow time for page to load

        # Extract flight prices using a better XPath
        prices = driver.find_elements(By.XPATH, "//span[contains(@id, 'spnPrice')]")

        if prices:
            for i, price in enumerate(prices[:10], 1):  # Limit to first 10 prices
                print(f"Flight {i}: ₹{price.text.strip()}")
        else:
            print("No prices found.")
    finally:
        driver.quit()

# Run the function
get_flight_prices()
