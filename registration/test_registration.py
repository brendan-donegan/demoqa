from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import testtools
from testtools.matchers import (
    Equals
)

USERNAME_TEXTFIELD = 'user_login'
EMAIL_TEXTFIELD = 'user_email'
SUBMIT_BUTTON = 'wp-submit'
MESSAGE = 'p.message'
ERRORS = 'login_error'


class RegistrationPage:
    pass


class RegistrationPageTestCase(testtools.TestCase):

    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome("/home/brendand/chromedriver")
        self.driver.get("http://store.demoqa.com/wp-login.php?action=register")

    def tearDown(self):
        super().tearDown()
        self.driver.close()

    def test_title_correct(self):
        self.assertThat(self.driver.title, Equals("ONLINE STORE ‹ Registration Form"))

    def test_valid_username_and_email(self):
        # Enter username
        username_text = self.driver.find_element_by_id(USERNAME_TEXTFIELD)
        username_text.send_keys("bartholemew")
        # Enter email
        email_text = self.driver.find_element_by_id(EMAIL_TEXTFIELD)
        email_text.send_keys("bart@email.com")
        import pdb; pdb.set_trace()
        # Click submit button
        submit_button = self.driver.find_element_by_id(SUBMIT_BUTTON)
        submit_button.click()
        # Check messages
        registration_message = self.driver.find_element_by_css_selector(MESSAGE)
        self.assertThat(registration_message.text, Equals('message'))

    def test_no_username_and_email_entered(self):
        # Click submit button without entering anything
        submit_button = self.driver.find_element_by_id(SUBMIT_BUTTON)
        submit_button.click()
        # Check messages
        error_messages = self.driver.find_element_by_css_selector(ERRORS)
        self.assertThat(error_messages.text, Contains(
            "Please enter a username."
        ))
        self.assertThat(error_messages.text, Contains(
            "Please type your email address."
        ))

    def test_valid_username_and_invalid_email(self):
        # Enter username
        username_text = self.driver.find_element_by_id(USERNAME_TEXTFIELD)
        username_text.send_keys("homer")
        # Enter email
        email_text = self.driver.find_element_by_id(EMAIL_TEXTFIELD)
        email_text.send_keys("homer/email.com")
        import pdb; pdb.set_trace()
        # Click submit button
        submit_button = self.driver.find_element_by_id(SUBMIT_BUTTON)
        submit_button.click()
        # Check messages
        error_messages = self.driver.find_element_by_css_selector(ERRORS)
        self.assertThat(error_messages.text, Contains(
            "The email address isn’t correct."
        ))
