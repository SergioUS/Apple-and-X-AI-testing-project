import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import helpers as h

# Your BrowserStack credentials
USERNAME = "your_name"
ACCESS_KEY = "your_key"

# Fixture that sets up and tears down a BrowserStack WebDriver session
@pytest.fixture
def driver():
    options = Options()
    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")
    options.set_capability("platformName", "Windows 11")
    options.set_capability("bstack:options", {
        "sessionName": "TC_P_019: Apple Arcade FAQ accessibility with keyboard",
        "buildName": "Build_002_Apple_Tests",
        "userName": USERNAME,
        "accessKey": ACCESS_KEY
    })

    driver = webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )
    yield driver
    driver.quit()

# Actual test case for FAQ accessibility using keyboard
def test_case_019_positive_apple_arcade(driver):
    print("✅ Starting TC_P_019: FAQ accessibility with keyboard")

    # Step 1: Open the Apple Arcade page
    driver.get(h.site)

    # Step 2: Wait for the FAQ section header to be present
    faq_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, h.faq_header))
    )

    # Step 3: Scroll to the FAQ section
    driver.execute_script("arguments[0].scrollIntoView(true);", faq_header)
    time.sleep(1)

    # Step 4: Press TAB to move focus to the first FAQ toggle
    body = driver.find_element(By.TAG_NAME, h.body_tag)
    body.send_keys(Keys.TAB)
    time.sleep(2)

    # Step 5: Get focused FAQ button and expand it with ENTER
    focused = driver.switch_to.active_element
    aria_controls = focused.get_attribute("aria-controls")
    focused.send_keys(Keys.ENTER)
    time.sleep(2)

    # Step 6: Verify the FAQ item expanded
    faq_button = driver.find_element(By.XPATH, h.faq_button_by_aria(aria_controls))
    expanded = faq_button.get_attribute("aria-expanded")

    assert expanded == h.expected_expanded_value, " FAQ item did not expand after ENTER key"
    print("FAQ item expanded successfully")
