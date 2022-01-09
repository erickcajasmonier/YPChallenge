from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_user import create_user

class TestUserLogout(unittest.TestCase):

    user_logout_endpoint = get_config_data('USER_ENDPOINT') + '/logout'

    def setUp(self):
        max_number = get_config_data('MAX_NUMBER')
        max_length = get_config_data('MAX_LENGTH')
        user_data = create_user(max_number, max_length)
        username = user_data['username']
        password = user_data['password']
        user_login_endpoint = get_config_data('USER_ENDPOINT') + '/login'
        get_request_api(user_login_endpoint +
                                   '?username={}&password={}'.format(username, password))

    def test_logout_user(self):
        response = get_request_api(self.user_logout_endpoint)

        assert(response.status_code == 200)
        assert(response.text == 'User logged out')
