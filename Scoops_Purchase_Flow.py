
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


time.sleep(5)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        cls.driver.set_page_load_timeout(10)
        cls.driver.get("https://hangar-qa-dot-development-dot-dh-dev-242811.uc.r.appspot.com/app/gifts")
 # Select scoops box
        wait = WebDriverWait(cls.driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app-content']/div[1]/div[1]/div[2]/div[1]/react-framed-checkbox[2]/div[1]/div[1]"))).click()

 
# Fill out the form - To
        cls.driver.set_page_load_timeout(10)
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_shipping_first_name_0']").send_keys("QATEST1")
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_shipping_last_name_1']").send_keys("QATEST1")
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_shipping_postal_code_2']").send_keys("11222")
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_shipping_email_3']").send_keys("jessica.vargas@daily-harvest.com")

# Click on Gift Delivery Method - Email
        wait = WebDriverWait(cls.driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='app-content']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/ng-form[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]"))).click()
        
# Fill out the form  - From 
        cls.driver.set_page_load_timeout(10)
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_sender_first_name_0']").send_keys("QATEST2")
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_sender_last_name_1']").send_keys("QATEST2")
        cls.driver.find_element_by_xpath("//input[@id='formly_2_input-bootstrap_sender_email_8']").send_keys("jessica.vargas@daily-harvest.com")

  # to switch to frame with frame name      
    @classmethod
    def testIframe(cls):
        time.sleep(5)
        wait = WebDriverWait(cls.driver, 50).until
       
        write_on_iframe = wait(EC.element_to_be_clickable((By.XPATH, "//*[@id='stripe-payment-fields']/div/iframe")))
        #time.sleep(5)
        write_on_iframe.send_keys('4242 4242 4242 4242')
        #time.sleep(5)
        write_on_iframe.send_keys('02/23')
        #time.sleep(5)
        write_on_iframe.send_keys('111')
        #time.sleep(5)
        write_on_iframe.send_keys('11222')
        #time.sleep(5)
        write_on_iframe.send_keys(Keys.ENTER)
        time.sleep(5)

 # Click on Place your Order Button
        wait = WebDriverWait(cls.driver, 30)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Place your order')]"))).click()


# Verify that the purchase was successful
        wait = WebDriverWait(cls.driver, 30)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Gift box purchase complete!')]")))
        assert element.text == 'Gift box purchase complete!'
        if element.text == 'Gift box purchase complete!': print "Succesfull Purchase"
        time.sleep(5)

 # Click on KEEP BROWSING CTA in order to check if it is linking as expected - Purchase confrimation Page
       


       
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()








