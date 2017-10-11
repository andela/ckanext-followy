import  unittest
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FollowyTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'/usr/local/lib/geckodriver')
        self.addCleanup(self.browser.quit)


    def test_create_dataset_and_follow(self):
        self.browser.get('http://localhost:5000')
        login = self.browser.find_element_by_link_text("Log in")
        login.click()
        username = self.browser.find_element_by_id("field-login")
        password = self.browser.find_element_by_id("field-password")
        login_Btn = self.browser.find_elements_by_class_name("btn-primary")[0]
        username.send_keys("ghost")
        password.send_keys("ghostmode")
        login_Btn.click()
        assert 'http://localhost:5000/dashboard' in self.browser.current_url
        datasets = self.browser.find_element_by_link_text("Datasets")
        datasets.click()
        assert 'http://localhost:5000/dataset' in self.browser.current_url
        add_dataset = self.browser.find_element_by_link_text("Add Dataset")
        search_dataset = self.browser.find_elements_by_class_name("search")
        assert add_dataset != None 
        assert search_dataset != None
        add_dataset.click()
        assert 'http://localhost:5000/dataset/new' in self.browser.current_url
        title = self.browser.find_element_by_id("field-title")
        assert title != None
        description = self.browser.find_element_by_id("field-notes")
        assert description != None
        visibility = self.browser.find_element_by_id("field-private")
        visibility != None
        next_page = self.browser.find_elements_by_class_name("btn-primary")[0]
        assert next_page != None
        time.sleep(5)
        title_text = "".join( [random.choice(string.ascii_letters) for i in range(8)] )
        title.send_keys(title_text)
        time.sleep(5)
        description_text = "".join( [random.choice(string.ascii_letters) for i in range(20)] )
        description.send_keys(description_text)
        next_page.click()
        dataset_url = self.browser.find_element_by_name("url")
        assert dataset_url != None
        url_text = "".join( [random.choice(string.ascii_letters) for i in range(12)] )
        dataset_url.send_keys(url_text)
        finish_btn = self.browser.find_elements_by_class_name("btn-primary")[0]
        assert finish_btn != None
        finish_btn.click()
        activity_stream = self.browser.find_elements_by_class_name("icon-time")
        assert activity_stream != None
        manage_btn = self.browser.find_elements_by_class_name("icon-wrench")
        assert manage_btn != None
        follow_btn = self.browser.find_elements_by_class_name("btn-success")[0]
        assert follow_btn != None
        follow_btn.click()
        success_message = self.browser.find_elements_by_class_name("alert-success")
        assert success_message != None
        time.sleep(4)        


    def test_following_dataset(self):
        self.browser.get('http://localhost:5000')
        login = self.browser.find_element_by_link_text("Log in")
        login.click()
        username = self.browser.find_element_by_id("field-login")
        password = self.browser.find_element_by_id("field-password")
        login_Btn = self.browser.find_elements_by_class_name("btn-primary")[0]
        username.send_keys("ghost")
        password.send_keys("ghostmode")
        login_Btn.click()
        assert 'http://localhost:5000/dashboard' in self.browser.current_url
        follow = self.browser.find_element_by_link_text("Following")
        assert follow != None
        follow.click()
        time.sleep(4)
        dropdown_menu = self.browser.find_elements_by_class_name("dropdown-toggle")[0]
        assert dropdown_menu != None
        time.sleep(4)        
        dropdown_menu.click()
        profile = self.browser.find_element_by_link_text("Profile")
        assert profile != None
        options = self.browser.find_element_by_link_text("Options")
        assert options != None
        logout = self.browser.find_element_by_link_text("Logout")
        assert logout != None
        profile.click()
        datasets = self.browser.find_element_by_link_text("Datasets")
        assert datasets != None
        activity_stream = self.browser.find_element_by_link_text("Activity Stream")
        assert activity_stream != None
        data_requests = self.browser.find_element_by_link_text("Data Requests")
        assert data_requests != None
        following = self.browser.find_element_by_link_text("Following")
        assert following != None
        following.click()
        time.sleep(4)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
    