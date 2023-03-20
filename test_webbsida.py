import unittest
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service("C:\Drivers\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://www.netonnet.se/")
        self.driver.find_element(By.XPATH,'//*[@id="cookiebannerShowSettingsButton"]/div/div[1]/button').click()

    # Test 1: Test som verifierar att länken "Dator & Surfplatta" öppnas upp på korrekt sätt med samma rubrik.
    def test_computer_tablet(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Dator & Surfplatta']").click()
        expected = 'Dator & Surfplatta'
        actual = self.driver.find_element(By.XPATH, '//*[@id="header-drop-down-menu"]/div/div[1]/div/div/h1').text
        self.assertEqual(expected, actual)

    # (TA BORT TIME.SLEEP) Test 2: Test som verifierar att länken "Kundvagn" är tom. 
    def test_shopping_cart(self):
        time.sleep(3)
        self.driver.find_element(By.ID, 'shopping-cart-icon-bg').click()
        time.sleep(3)
        expected = 'Kundvagnen är tom'
        actual = self.driver.find_element(By.XPATH, '//*[@id="emptyCartMessage"]').text
        self.assertEqual(expected, actual)

    # (TA BORT TIME.SLEEP) Test 3: Navigera till "Mina sidor" och därefter till "E-postadress" och logga in. Verifiera att man har loggat in på korrekt sätt. 
    def test_login_page(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="topLogin"]/span').click()
        time.sleep(3)
        self.driver.find_element(By.ID,"EmailRadio").click()
        self.driver.find_element(By.ID,'loginEmail').send_keys("imran_biberic@hotmail.com")
        self.driver.find_element(By.ID,"loginPassword").send_keys("ECUtbildning123!")
        self.driver.find_element(By.XPATH,'//*[@id="LoginForm"]/form/div[3]/div[2]/div/div/div[1]/button').click()
        time.sleep(3) 
        expected = 'Logga ut'
        actual = self.driver.find_element(By.XPATH, '//*[@id="desktop-header-menu"]/li[4]/a/span').text
        self.assertEqual(expected, actual)

    # Test 4: Navigera till länken "Hitta Lagershop & Öppettider" och verifiera att "Malmö Svågertorp Lagershop" adress är: Nornegatan 5.
    def test_address(self):
        self.driver.find_element(By.CSS_SELECTOR, "#desktop-header-menu > li:nth-child(4) > a > span").click()
        self.driver.execute_script("scrollBy(0, 1500)")
        self.driver.find_element(By.CSS_SELECTOR, "#__next > main > div > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-4.css-76wze3 > div:nth-child(13) > div > div.MuiCardMedia-root.css-pqdqbj > a > img").click()
        expected = 'Nornegatan 5'
        actual = self.driver.find_element(By.CSS_SELECTOR, "#__next > main > div > div > div > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-6.css-wwiify > div > p:nth-child(2)").text
        self.assertEqual(expected, actual)
        
    # Test 5: Navigera till Apple iPad via sökfältet och verifiera att produkten har lagts i kassan med rätt pris på korrekt sätt
    def test_apple_ipad(self):
        search = self.driver.find_element(By.CSS_SELECTOR, "#search-form > div > div > input.form-control.searchInput")
        search.send_keys('Apple iPad (9th gen) 10,2" 64GB Wi-Fi Space Grey')
        search.send_keys(Keys.RETURN)
        self.driver.execute_script("scrollBy(0,200)")
        self.driver.find_element(By.XPATH, '//*[@id="productList"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="BuyButton_ProductPageStandard_1020736"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="insuranceCollapse"]/div/div[1]/div[2]/div/div/a[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="accessoriesModalActionBtns"]/a[2]').click()
        
        expected_page_title = "NetOnNet - Kassan"
        actual_page_title = self.driver.title
        self.assertEqual(expected_page_title, actual_page_title)
        
        expected_product = 'Apple iPad (9th gen) 10,2" 64GB Wi-Fi Space Grey'
        actual_product = self.driver.find_element(By.XPATH, '//*[@id="cartListContent"]/div[1]/div/form/div[1]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/a').text
        self.assertEqual(expected_product, actual_product)
        
        expected_price = "3 980:-"
        actual_price = self.driver.find_element(By.XPATH, '//*[@id="cartListContent"]/div[1]/div/form/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/span').text
        self.assertEqual(expected_price, actual_price)




    def tearDown(self):
        self.driver.delete_all_cookies()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# 