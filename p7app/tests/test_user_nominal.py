from flask_testing import LiveServerTestCase
from selenium import webdriver


from .. import app


class TestUser(LiveServerTestCase):

    def create_app(self):
        app.config.from_object('p7app.tests.config')
        return app

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_user_login(self):
        # On ouvre le navigateur avec l'adresse du serveur.
        self.driver.get(self.get_server_url())
        # L'adresse dans l'url doit être celle que l'on attend.
        assert self.driver.current_url == 'http://localhost:5000/'

    def tearDown(self):
        self.driver.quit()