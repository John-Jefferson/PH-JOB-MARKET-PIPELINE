from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keywords
import time

def jobStreetScraper(countOfApplications):
    links = []
    pageCount = 1
    driver = webdriver.Chrome()
    df = []
    #GETTING ALL THE LINKS
    while len(links) < countOfApplications:
        driver.get(f"https://ph.jobstreet.com/data-jobs?page={pageCount}")

        wait = WebDriverWait(driver, 15)

        # wait for job links directly
        job_links = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a[href*='/job/']")
            )
        )
        hrefs = [job.get_attribute("href") for job in job_links]

        for h in hrefs:
            if len(links) >= countOfApplications:
                break
            links.append(h)
        pageCount+=1
    print(links)    
    print(len(links))

    for link in links:
        driver.get(link)

        #JOB TITLE
        title = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "h1[data-automation='job-detail-title']")
            )
        )
        print(title.text)

        #JOB LOCATION
        location = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-automation='job-detail-location'] a")
            )
        )
        print(location.text)

        #JOB CLASSIFICATION
        classificaiton = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-automation='job-detail-classifications'] a")
            )
        )
        print(classificaiton.text)

        #JOB WORK TYPE
        work_type = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-automation='job-detail-work-type'] a")
            )
        )
        print(work_type.text)
        print("PARAGRAPHS NA")
        paragraphs = driver.find_element(By.CSS_SELECTOR, "[data-automation='jobAdDetails']")
        text = paragraphs.text
        print(text)

        df.append({
        "title":            keywords.comparison(title.text, keywords.jobTitles),
        "work_type":        work_type.text,
        "location":         location.text,
        "description":      text,
        "skills":           keywords.comparison(text, keywords.skills),
        "qualifications":   keywords.comparison(text, keywords.qualifications),
        "seniority_level":  keywords.comparison((title.text + " " + text), keywords.Seniority_Level)[0],
        "work_setup":       keywords.comparison((title.text + " " + text), keywords.Work_Setup)[0],
        "link":             link
        })
    return df