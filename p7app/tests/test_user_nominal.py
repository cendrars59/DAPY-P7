from flask_testing import LiveServerTestCase
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from flask import url_for
from .nominal_data_set import data
from .. import app


class TestUser(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('p7app.tests.config')
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()

    def enter_text_field(self, selector, text):
        # Selecting the text area.
        text_field = self.get_el(selector)
        # Clear text if already exit.
        text_field.clear()
        # Adding text to submit.
        text_field.send_keys(text)

    def tearDown(self):
        self.driver.quit()

    def get_el(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def submits_form(self):
        # Entering request text to submit
        self.enter_text_field('#request', data['input'])
        # Clicking on submission button
        self.get_el('#submit').click()

    def test_user_nominal(self):
        # Opening browser and set Server URL as entry point.
        self.driver.get(self.get_server_url())
        # Checking that the URL is as expected.
        assert self.driver.current_url == 'http://localhost:5000/'
        self.submits_form()
        # Waiting for the redirection is ended.
        delay = 5 #seconds
        #self.wait.until(lambda driver: '?' in self.driver.current_url)
        #assert self.driver.current_url == '/result'
