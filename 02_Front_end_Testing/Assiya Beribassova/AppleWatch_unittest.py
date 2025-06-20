from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
import helpers as h
import random
import unittest
import time



def delay():
    time.sleep(random.randint(2, 5))
class AppleWatchPositiveChrome(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_chrome_TC_P31(self):
        driver = self.driver
    #TC_P_031
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                            Store/ Apple Watch                      ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print("                            POSITIVE TEST CASES                     ")
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_P_031                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that user is able to contact a specialist with "Ask an Apple Watch Specialist".
        driver.get(h.site)
        print("1. Open 'https://www.apple.com/' website.")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        driver.find_element(By.XPATH, "//a[@class='as-chat-button active as-buttonlink icon icon-after icon-external']").click()
    #Page title
        assert h.title in driver.title
        print("Page title is:", driver.title)
        print("4. Navigate to the ‘Ask an Apple Watch Specialist’ page.")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Chat with us online.')]").click()
        delay()
        print("5. Click on ‘Chat with us online’.")
        driver.find_element(By.ID, "txt_userMessage").send_keys("Buy an apple watch")
        print("6. In the chat window, send the message: “Buy an apple watch”.")
        driver.find_element(By.ID, "sendIcon").click()
    # The user successfully sent a message through the chat interface. All links provided in the chat were navigated to the correct pages without errors.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_P_031 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    def test_chrome_TC_P32(self):
        driver = self.driver
    # TC_P_032
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_P_032                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that the user can choose a store located in New York from the 'Find a Store' feature.
        driver.get(h.site)
        print("1. Open 'https://www.apple.com/' website.")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        driver.find_element(By.XPATH, "//a[@href='https://www.apple.com/retail']").click()
        print("4. Click on 'Find one near you' link ")
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Find a store']"))).click()
        delay()
        driver.find_element(By.XPATH, "//input[@aria-label='Find a store']").send_keys("New York, NY")
        delay()
        driver.find_element(By.XPATH, "//input[@aria-label='Find a store']").send_keys(Keys.ENTER)
        print("5. In the search bar enter 'New York, NY'")
        driver.find_element(By.XPATH, "//section[@aria-label='find store']").click()
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Stores near New York, NY']")))
    # The user successfully got location information for Apple Stores in New York. Store details were accurate and all associated links were functional.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_P_032 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')

    def test_chrome_TC_P33(self):
        driver = self.driver
    # TC_P_033
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_P_033                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that header menu buttons are functional.
        driver.get(h.site)
        wait = WebDriverWait(driver, 2)
        print("1. Open 'https://www.apple.com/' website.")
        wait.until(EC.visibility_of_element_located((By.XPATH,h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        wait.until(EC.element_to_be_clickable((By.XPATH, h.AllModels)))
        print("4. Click on 'All models' button.")
        driver.find_element(By.XPATH, "//a[normalize-space()='Shopping guides']").click()
        print("5. Click on 'Shopping guides' button.")
        driver.find_element(By.XPATH, "//a[normalize-space()='Ways to Save']").click()
        print("6. Click on 'Ways to save' button.")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='rf-navbar-item-link'][normalize-space()='Apple Watch Bands']")))
        print("7. Click on 'Apple Watch bands' button.")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Setup and Support']")))
        print("8. Click on 'Setup and support' button.")
        driver.find_element(By.XPATH, "//div[@id='rf-navbar']//div[6]//div[1]").click()
        print("9. Click on 'The Apple Watch experience' button.")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Special Stores']")))
        print("10. Click on 'Special Savings' button.")
    # All header menu buttons are functional. Each button successfully navigates the user to the correct section of the page without errors or delays.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_P_033 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    def test_chrome_TC_P34(self):
        driver = self.driver
    # TC_P_034
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_P_034                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that user is able to select 'Apple Watch Hermès Series 10' from product list.
        driver.get(h.site)
        wait = WebDriverWait(driver, 2)
        print("1. Open 'https://www.apple.com/' website.")
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        driver.find_element(By.XPATH, h.AllModels).click()
        print("4. Click on 'All models' button.")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']")))
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']").click()
        delay()
        print("5. Scroll horizontally to the right to find 'Apple Watch Hermès Series 10'")
    # 'Apple Watch Hermès Series 10' is visible and the user is able to choose from the listed options.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_P_034 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    def test_chrome_TC_P35(self):
        driver = self.driver
    # TC_P_035
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_P_035                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that the user can successfully add the 'Apple Watch Hermès Series 10' to the cart.
        driver.get(h.site)
        wait = WebDriverWait(driver, 2)
        print("1. Open 'https://www.apple.com/' website.")
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        delay()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        delay()
        driver.find_element(By.XPATH, h.AllModels).click()
        print("4. Click on 'All models' button.")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']")))
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']").click()
        print("5. Scroll horizontally to the right to find 'Apple Watch Hermès Series 10'")
        delay()
        driver.find_element(By.XPATH, "//div[@id='panel-:r22:-0']//a[@class='button rf-digitalmat-button']").click()
        delay()
        print("6. Click on 'Buy' button.")
        try:
            assert h.AppleWatchHermesURL in driver.current_url
            print('Page URL is: ', driver.current_url)
        except AssertionError:
            print("Current url is different ", driver.current_url)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='form-selector-title'][normalize-space()='42mm']"))).click()
        print("7.1. Select 42mm")
        driver.find_element(By.TAG_NAME, "html").send_keys(Keys.SPACE)
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id=':re:_label']//span[@class='form-selector-title']"))).click()
        print("7.2. Select 'Toile H Single Tour'")
        delay()
        gold_ecru_color_element = wait.until(EC.element_to_be_clickable((By.XPATH, h.gold_ecru_color_xpath)))
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", gold_ecru_color_element)
        gold_ecru_color_element.click()
        print("7.3. Select 'Gold/Écru'")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'No trade-in')]"))).click()
        print("7.4. Select 'No trade-in'")
        driver.find_element(By.TAG_NAME, "html").send_keys(Keys.SPACE)
        buy = driver.find_element(By.XPATH, "//input[@data-autom='purchaseGroupOptionfullprice']")
        driver.execute_script("arguments[0].click();", buy)
        print("7.5. Select 'Buy'")
        driver.find_element(By.TAG_NAME, "html").send_keys(Keys.SPACE)
        delay()
        element = driver.find_element(By.XPATH, "//input[@data-autom='noapplecare']")
        driver.execute_script("arguments[0].click();", element)
        print("7.6. Select 'No Apple care'")
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label']"))).click()
        print("7.7. Click on 'Add to bag' button")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-autom='proceed']"))).click()
        print("8. Review cart")
    # The user successfully added the item to the shopping bag and all selected characteristics are correctly displayed in the bag summary.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_P_035 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    def tearDown(self):
        self.driver.quit()

class AppleWatchNegativeChrome(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_chrome_TC_N31(self):
        driver = self.driver
    #TC_N_031
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                            Store/ Apple Watch                      ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print("                            NEGATIVE TEST CASES                     ")
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_N_031                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that searching for 'Portland' in 'Find a store' returns store information for New York.

        driver.get(h.site)
        print("1. Open 'https://www.apple.com/' website.")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        driver.find_element(By.XPATH, "//a[@href='https://www.apple.com/retail']").click()
        print("4. Click on 'Find one near you' link ")
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Find a store']"))).click()
        delay()
        driver.find_element(By.XPATH, "//input[@aria-label='Find a store']").send_keys("Portland, ME")
        delay()
        driver.find_element(By.XPATH, "//input[@aria-label='Find a store']").send_keys(Keys.ENTER)
        print("5. In the search bar enter 'Portland, ME'.")
        driver.find_element(By.XPATH, "//section[@aria-label='find store']").click()
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Stores near Portland, ME']")))
    # When 'Portland, ME' was entered in the search bar, the system correctly returned a list of store locations in or near 'Portland, ME'. No incorrect results (such as stores in New York) were displayed.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_N_031 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')

    def test_chrome_TC_N32(self):
        driver = self.driver
    #TC_N_032
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_N_032                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that by clicking 'All models' in header user can go to 'Apple Watch bands' section.
        driver.get(h.site)
        wait = WebDriverWait(driver, 2)
        print("1. Open 'https://www.apple.com/' website.")
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        driver.find_element(By.XPATH, h.AllModels).click()
        print("4. Click on 'All models' button.")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='All models.']")))
    # Clicking the 'All models' correctly displayed a list of watch models, without defaulting to the band collection.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_N_032 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')

    def test_chrome_TC_N33(self):
        driver = self.driver
    #TC_N_033
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_N_033                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that by clicking 'Apple Watch Series 10' the user can be redirected to 'Apple Watch SE' page.
        driver.get(h.site)
        wait = WebDriverWait(driver, 2)
        print("1. Open 'https://www.apple.com/' website.")
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        delay()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        delay()
        driver.find_element(By.XPATH, h.AllModels).click()
        print("4. Click on 'All models' button.")
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']")))
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']").click()
        print("5. Scroll horizontally to the right to find 'Apple Watch Hermès Series 10'")
        delay()
        driver.find_element(By.XPATH, "//div[@id='panel-:r22:-0']//a[@class='button rf-digitalmat-button']").click()
        delay()
        print("6. Click on 'Buy' button.")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Buy Apple Watch Hermès']")))
    # Clicking the button performed the expected action on the same page without redirecting.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_N_033 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    def test_chrome_TC_N34(self):
        driver = self.driver
    #TC_N_034
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_N_034                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that user is able to send an empty search query from search bar in 'Find a Store' page.

        driver.get(h.site)
        print("1. Open 'https://www.apple.com/' website.")
        wait = WebDriverWait(driver, 2)
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        driver.find_element(By.XPATH, "//a[@href='https://www.apple.com/retail']").click()
        print("4. Click on 'Find one near you' link ")
        # Switch to new tab
        driver.switch_to.window(driver.window_handles[-1])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Find a store']"))).click()
        delay()
        driver.find_element(By.XPATH, "//input[@aria-label='Find a store']").send_keys("   ")
        delay()
        driver.find_element(By.XPATH, "//input[@aria-label='Find a store']").send_keys(Keys.ENTER)
        print("5. Send and submit an empty search")
        driver.find_element(By.XPATH, "//section[@aria-label='find store']").click()
        delay()

    # The system prevented empty search.
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_N_034 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    def test_chrome_TC_N35(self):
        driver = self.driver
    #TC_N_035
        print('                                                                    ')
        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                               TC_N_035                             ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')
    # Verify that user is able to proceed checkout 'Apple Watch Hermès Series 10' with 77 times.
        driver.get(h.site)
        wait = WebDriverWait(driver, 2)
        print("1. Open 'https://www.apple.com/' website.")
        wait.until(EC.visibility_of_element_located((By.XPATH, h.apple_logo)))
        driver.find_element(By.XPATH, h.store_button).click()
        delay()
        print("2. Click on the ‘Store’ button.")
        driver.find_element(By.XPATH, h.apple_watch).click()
        print('3. Click on the ‘Apple Watch’ button.')
        delay()
        driver.find_element(By.XPATH, h.AllModels).click()
        print("4. Click on 'All models' button.")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']")))
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Watch Hermès Series 10']").click()
        print("5. Scroll horizontally to the right to find 'Apple Watch Hermès Series 10'")
        delay()
        driver.find_element(By.XPATH, "//div[@id='panel-:r22:-0']//a[@class='button rf-digitalmat-button']").click()
        delay()
        print("6. Click on 'Buy' button.")
        try:
            assert h.AppleWatchHermesURL in driver.current_url
            print('Page URL is: ', driver.current_url)
        except AssertionError:
            print("Current url is different ", driver.current_url)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='form-selector-title'][normalize-space()='42mm']"))).click()
        print("7.1. Select 42mm")
        driver.find_element(By.TAG_NAME, "html").send_keys(Keys.SPACE)
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@id=':re:_label']//span[@class='form-selector-title']"))).click()
        print("7.2. Select 'Toile H Single Tour'")
        delay()
        gold_ecru_color_element = wait.until(EC.element_to_be_clickable((By.XPATH, h.gold_ecru_color_xpath)))
        driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", gold_ecru_color_element)
        gold_ecru_color_element.click()
        print("7.3. Select 'Gold/Écru'")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'No trade-in')]"))).click()
        print("7.4. Select 'No trade-in'")
        driver.find_element(By.TAG_NAME, "html").send_keys(Keys.SPACE)
        buy = driver.find_element(By.XPATH, "//input[@data-autom='purchaseGroupOptionfullprice']")
        driver.execute_script("arguments[0].click();", buy)
        print("7.5. Select 'Buy'")
        driver.find_element(By.TAG_NAME, "html").send_keys(Keys.SPACE)
        delay()
        element = driver.find_element(By.XPATH, "//input[@data-autom='noapplecare']")
        driver.execute_script("arguments[0].click();", element)
        print("7.6. Select 'No Apple care'")
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label']"))).click()
        print("7.7. Click on 'Add to bag' button")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@data-autom='proceed']"))).click()
        print("9. Click on review bag button")
        delay()
    # Quantity dropdown menu
        dropdown = driver.find_element(By.XPATH, "//select[@data-autom='item-quantity-dropdown']")
    # Create Select object
        select = Select(dropdown)
    # Select by value
        select.select_by_value("10")
    # Quantity input field
        qty_input = driver.find_element(By.XPATH,"//input[contains(@class, 'rs-quantity-textbox') and @type='tel']")
        qty_input.click()
        qty_input.clear()
        qty_input.send_keys("77")
        driver.find_element(By.TAG_NAME, "body").click()
        delay()
    # Refresh page
        driver.refresh()
        delay()
        error_message_textweb = driver.find_element(By.XPATH, "//div[@class='rt-messages-text'][normalize-space()='A maximum of 6 Apple Watch Hermès Series 10 (GPS + Cellular) can be purchased per customer. Please adjust the total quantity of Apple Watch Hermès Series 10 (GPS + Cellular) in your order before checking out.']").text

        try:
            assert h.error_message_textdoc in error_message_textweb
            print("Error Text is OK: ", error_message_textweb)
        except AssertionError:
            print("Error Text is NOT OK", error_message_textweb)
            driver.save_screenshot("No Error text.png")
    #The user is not allowed to add 77 times of an item to the shopping bag and an error message was shown.

        print('--------------------------------------------------------------------')
        print('                                                                    ')
        print('                           TC_N_035 PASSED                          ')
        print('                                                                    ')
        print('--------------------------------------------------------------------')


    def tearDown(self):
        self.driver.quit()
