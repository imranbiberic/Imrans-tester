import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

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

    # Test 1
    def test_computer(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Dator & Surfplatta']").click()
        actual = self.driver.find_element(By.XPATH,'//*[@id="header-drop-down-menu"]/div/div[1]/div/div/h1').text
        expected = 'Dator & Surfplatta'
        self.assertEqual(expected,actual)

    # Test 2
    # Imran Biberic



    def tearDown(self):
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()