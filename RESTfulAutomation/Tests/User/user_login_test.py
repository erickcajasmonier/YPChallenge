from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_user import create_user

class TestUserLogin(unittest.TestCase):

    user_login_endpoint = get_config_data('USER_ENDPOINT') + '/login'
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        user_data = create_user(self.max_number, self.max_length)
        self.username = user_data['username']
        self.password = user_data['password']

    def test_login_user(self):
        response = get_request_api(self.user_login_endpoint +
                                   '?username={}&password={}'.format(self.username, self.password))

        assert(response.status_code == 200)
        assert(response.text.startswith('Logged in user session:') is True)

    @pytest.mark.skip(reason="Endpoint is not working for Invalid username/password")
    def test_login_user_invalid_username_password(self):
        wrong_username = generate_random_name() + '2134'
        wrong_password = generate_random_string_with_numbers(self.max_length)

        response = get_request_api(self.user_login_endpoint +
                                   '?username={}&password={}'.format(wrong_username, wrong_password))
        
        assert(response.status_code == 400)
