from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

import matplotlib.pyplot as plt
'''
# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('chromedriver.exe')

# Run Selenium with ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.simplyhired.com/search?q=software+engineer&l=New+York%2C+NY&job=GuNt4GJc2YBrfsww0U6mjHEOwza-HhqkZHos7BIg1YMXJZRybiyawA')

# Handle cookies statement
def handle_cookies():
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        ).click()
    except Exception as e:
        print(f"Cookies statement not found or could not be clicked: {e}")

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.XPATH, "//div[@id='onetrust-policy-text']"))
        )
    except Exception as e:
        print(f"Cookie banner did not disappear: {e}")

# Wait for listings
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "css-obg9ou"))
)

# Scroll page to load more listings
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for new load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "css-obg9ou"))
    )
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

job_listings = []

def scrape_listings():
    # Get all listings
    listings = driver.find_elements(By.CLASS_NAME, "css-obg9ou")
    print(f"Number of listings found: {len(listings)}")

    for listing in listings:
        try:
            job_title_element = listing.find_element(By.CSS_SELECTOR, 'a.chakra-button.css-1djbb1k')
            company_element = listing.find_element(By.CSS_SELECTOR, "span.css-lvyu5j span[data-testid='companyName']")
            location_element = listing.find_element(By.CLASS_NAME, "css-1t92pv")

            title = job_title_element.text
            company = company_element.text
            location = location_element.text

            qualifications = [] # initialize qualifications

            try:
                # click listing and scrape words under "Qualifications" as Skills and any dollar amount in the listing as Salary
                job_title_element.click()
                WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "css-p3sbg2"))
                )

                qualifications_elements = driver.find_elements(By.CLASS_NAME, "css-p3sbg2")
                qualifications = [elem.text for elem in qualifications_elements]

            except Exception as e:
                print(f"Error clicking: {e}")

            job_listings.append({
                'title': title,
                'company': company,
                'location': location,
                'qualifications': qualifications
            })

        except Exception as e:
            print(f"Error processing listing: {e}")


while True:
    scrape_listings()

    try:
        # Locate "Next Page" button
        next_button = driver.find_element(By.CSS_SELECTOR, "#__next > div > main > div > div.css-17iqsqz > div > div > div.css-2jn6zr > div > div.css-15g2oxy > div.css-ukpd8g > nav > a.chakra-link.css-1puj5o8")

        # Print the button text to verify it's correct
        print(f"Next button found: {next_button.text}")

        # Click if exists
        if next_button:
            click_success = False
            for attempt in range(3):  # Try clicking up to 3 times
                try:
                    driver.execute_script("arguments[0].click();", next_button)
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "css-obg9ou"))
                    )
                    click_success = True
                    break
                except Exception as e:
                    print(f"Attempt {attempt + 1} to click 'Next' button failed: {e}")

            if not click_success:
                break
        else:
            break

    except Exception as e:
        print(f"No more pages or error: {e}")
        break

# repeat for second site
driver.get("https://www.glassdoor.com/Job/jobs.htm?sc.keyword=software engineer&locT=C&locName=Los Angeles")
def scrape_listings2(already_scraped_titles):
    # Get all listings
    listings = driver.find_elements(By.CLASS_NAME, "JobCard_trackingLink__HMyun")
    print(f"Number of listings found: {len(listings)}")

    for listing in listings:
        try:
            job_title_element = listing.find_element(By.CSS_SELECTOR, '#job-title-1009665124978')
            company_element = listing.find_element(By.CSS_SELECTOR, "#job-employer-1009665124978 > div.EmployerProfile_employerInfo___kmLv.EmployerProfile_employerWithLogo__xgrWU > div > span")
            location_element = listing.find_element(By.CSS_SELECTOR, "#job-location-1009665124978")
            salary_element = listing.find_element(By.CLASS_NAME, "JobCard_salaryEstimate__QpbTW")

            title = job_title_element.text
            company = company_element.text
            location = location_element.text
            salary = salary_element.text
            print(f"Salary: {salary}")

            qualifications = [] # initialize qualifications

            job_listings.append({
                'title': title,
                'company': company,
                'location': location,
                'qualifications': qualifications,
                'salary': salary
            })
            already_scraped_titles.add(title)

        except Exception as e:
            print(f"Error processing listing: {e}")

already_scraped_titles = set()

while True:
    scrape_listings2(already_scraped_titles)

    try:
        # Locate "Load More" button
        load_more_button = driver.find_element(By.CSS_SELECTOR, "#left-column > div.JobsList_wrapper__EyUF6 > div > div > button")

        # Print the button text to verify it's correct
        print(f"Load more found: {load_more_button.text}")

        # Click if exists
        if load_more_button:
            click_success = False
            for attempt in range(3):  # Try clicking up to 3 times
                try:
                    driver.execute_script("arguments[0].click();", load_more_button)
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "JobCard_trackingLink__HMyun"))
                    )
                    click_success = True
                    break
                except Exception as e:
                    print(f"Attempt {attempt + 1} to click 'Load More' button failed: {e}")

            if not click_success:
                break
        else:
            break

    except Exception as e:
        print(f"No more pages or error: {e}")
        break


driver.quit()

# Convert listings to DataFrame
job_listings_df = pd.DataFrame(job_listings)
print(job_listings_df.head())
total_rows = len(job_listings_df)
print(f"Total rows before preprocessing: {total_rows}")

job_listings_df.to_csv('job_listings.csv', index=False)
print("Job Listings have been saved to job_listings.csv")
'''
# -------------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Read the preprocessed CSV file
job_listings_df = pd.read_csv('job_listings_preprocessed.csv')

# Step 2: Feature Engineering
def extract_skills(qualifications):
    skills = []
    for qual in qualifications:
        if any(keyword in qual for keyword in ['experience', 'years', 'mid-level', 'senior']):
            continue
        skills.append(qual)
    return skills

def extract_experience(qualifications):
    for qual in qualifications:
        if any(keyword in qual for keyword in ['experience', 'years', 'mid-level', 'senior']):
            return qual
    return "Not Specified"

job_listings_df['required_skills'] = job_listings_df['qualifications'].apply(extract_skills)
job_listings_df['experience_level'] = job_listings_df['qualifications'].apply(extract_experience)

# Step 3: Encode Categorical Features and Skills
def encode_features(df):
    vectorizer = CountVectorizer(tokenizer=lambda x: x, preprocessor=lambda x: x)
    skills_matrix = vectorizer.fit_transform(df['required_skills'])
    skills_df = pd.DataFrame(skills_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    df = pd.concat([df.reset_index(drop=True), skills_df.reset_index(drop=True)], axis=1)
    df = pd.get_dummies(df, columns=['title', 'location', 'experience_level'], drop_first=True)
    df.drop(columns=['required_skills'], inplace=True)
    return df

encoded_df = encode_features(job_listings_df)
X = encoded_df.drop(columns=['company', 'qualifications'])
y = job_listings_df['title']  # Make sure to use the original dataframe to access 'title'

# Step 4: Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Scale the Data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 6: Train RandomForestClassifier to Determine Feature Importance
rf_clf = RandomForestClassifier()
rf_clf.fit(X_train_scaled, y_train)

# Step 7: Feature Importance
feature_importance = rf_clf.feature_importances_
features = X.columns

importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Step 8: Visualization
# Feature Importance Visualization
plt.figure(figsize=(12, 6))
sns.barplot(data=importance_df.head(10), x='Importance', y='Feature')
plt.title('Top 10 Important Features in Job Roles')
plt.show()

print(importance_df.head(10))  # Print top 10 important features
