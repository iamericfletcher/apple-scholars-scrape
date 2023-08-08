from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

URL = "https://machinelearning.apple.com/work-with-us#scholars"
driver = webdriver.Chrome()
driver.get(URL)


# Function to scrape scholar details
def scrape_scholars(year):
    scholars_data = []

    # Click the year tab
    if year != "2023":  # Skip clicking the 2023 button if it's already active
        year_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[text()='{year}']"))
        )
        # Use JavaScript to force a click
        driver.execute_script("arguments[0].click();", year_tab)
        time.sleep(2)  # Wait for the content to load

    # Get all scholars for the year
    scholars = driver.find_elements(By.CSS_SELECTOR, ".styles_opportunitiesFlex__aBHYU > div")

    for scholar in scholars:
        name = scholar.find_element(By.CSS_SELECTOR, "h3").text
        institution = scholar.find_element(By.CSS_SELECTOR, ".typography-body-reduced-tight").text

        # For research, target the second div with the class typography-body-reduced-tight
        try:
            research = scholar.find_elements(By.CSS_SELECTOR, ".typography-body-reduced-tight")[1].text
        except IndexError:  # If there's no second element, set research to N/A
            research = "N/A"

        try:
            # Click the 'Read Bio' button
            bio_button = scholar.find_element(By.CSS_SELECTOR, ".btn.btn-link.typography-body-reduced-tight button")
            bio_button.click()

            # Wait for the modal's content to become present and extract bio
            bio = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".styles_scholars-modal__Ahg4D p.text-left.typography-body"))
            ).text

            # Wait for the close button to become clickable and then close the modal
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".styles_scholars-modal__Ahg4D .modal-close"))
            )
            close_button.click()

            time.sleep(2)  # Wait for the modal to close completely

        except:
            bio = "N/A"

        scholars_data.append({
            "Year": year,
            "Name": name,
            "Institution": institution,
            "Research": research,
            "Bio": bio
        })

    return scholars_data


# Scrape data only for the year 2023 - for testing
# years = ["2023"]
# Scrape data for each year
years = ["2023", "2022", "2021", "2020"]
all_data = {}
for year in years:
    all_data[year] = scrape_scholars(year)

driver.quit()

# Print the scraped data
for year, scholars in all_data.items():
    print(f"\n{year} Apple Scholars in AI/ML:\n")
    for scholar in scholars:
        print(f"Year: {scholar['Year']}")
        print(f"Name: {scholar['Name']}")
        print(f"Institution: {scholar['Institution']}")
        print(f"Research: {scholar['Research']}")
        print(f"Bio: {scholar['Bio']}\n")


def export_to_excel(data):
    # Convert the nested dictionary to a flat list of dictionaries
    rows = []
    for year, scholars in data.items():
        for scholar in scholars:
            rows.append(scholar)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(rows)

    # Export the DataFrame to an Excel file
    df.to_excel("apple_scholars_data.xlsx", index=False)


export_to_excel(all_data)
