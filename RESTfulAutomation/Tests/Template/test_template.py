import os
import requests
from Helper.Common.helper import *

class TestTemplate(unittest.TestCase):

    def setUp(self):
        initialize_environment()

    def test_template(self):
        print(generateRandomName())
        assert (os.getenv('DEFAULT_URL')) == 'https://www.google.com'