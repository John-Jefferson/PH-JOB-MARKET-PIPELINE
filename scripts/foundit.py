from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keywords

def founditScraper(countOfApplications):
    links = []
    pageCount = 1
    driver = webdriver.Chrome()
    df = []
    wait = WebDriverWait(driver, 15)
    #GETTING ALL THE LINKS
    while len(links) < countOfApplications:
        driver.get(f"https://www.foundit.com.ph/search/data-jobs?start=1&limit={countOfApplications}&query=data&queryDerived=true")

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
        print("=========")
        driver.get(link)
        title = wait.until(
            EC.presence_of_all_elements_located(
                (By.ID, "jdPageTitle")
            )
        )
        print(title.text)
        cards = driver.find_elements(By.CSS_SELECTOR, ".flex.items-center.gap-2")
        print(cards[1].text)
        print(cards[2].text)
        description = driver.find_element(By.CSS_SELECTOR, "div[class *= 'break-words text-[13px] leading-6']")
        print(description.text)
        location = driver.find_element(By.ID, "jdPageJobLocation")
        print("############ ", location)
        more_info = driver.find_elements(By.CSS_SELECTOR, ".text-content-primary.cursor-pointer")

        industry = more_info[1]
        print(link)
        job_type = more_info[3].text if len(more_info) > 3 else ""
        print(industry.text)
        print(job_type)

        df.append({
        "title":            keywords.comparison(title.text, keywords.jobTitles),
        "work_type":        job_type,
        "location":         location,
        "description":      description.text,
        "skills":           keywords.comparison(description.text, keywords.skills),
        "qualifications":   keywords.comparison(description.text, keywords.qualifications),
        "seniority_level":  keywords.comparison((title.text + " " + description.text), keywords.Seniority_Level)[0],
        "work_setup":       keywords.comparison((title.text + " " + description.text), keywords.Work_Setup)[0],
        "link":             link
        })
    return df