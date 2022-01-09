from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_user import create_user

class TestDeleteUser(unittest.TestCase):

    user_endpoint = get_config_data('USER_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        user_data = create_user(self.max_number, self.max_length)
        self.username = user_data['username']
        password = user_data['password']
        user_login_endpoint = get_config_data('USER_ENDPOINT') + '/login'
        get_request_api(user_login_endpoint +
                                   '?username={}&password={}'.format(self.username, password))

    def test_delete_user(self):
        response = delete_request_api(self.user_endpoint + '/{}'.format(self.username))

        assert(response.status_code == 200)

        response = get_request_api(self.user_endpoint + '/{}'.format(self.username))
        
        assert(response.status_code == 404)
        assert(response.text == 'User not found')

    @pytest.mark.skip(reason="Endpoint is not working for invalid username - 400")
    def test_delete_user_invalid_username(self):
        wrong_username = generate_random_string_with_numbers(self.max_length)
        response = delete_request_api(self.user_endpoint + '/{}'.format(wrong_username))

        assert(response.status_code == 400)
        assert(response.text == 'User not found')
