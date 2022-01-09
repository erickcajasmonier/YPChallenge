from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet

class TestCreateNewUser(unittest.TestCase):

    user_endpoint = get_config_data('USER_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def test_create_new_user(self):
        full_name = generate_random_name().split()
        self.user_id = generate_random_number(self.max_number)
        self.username = full_name[0] + full_name[1]
        self.first_name = full_name[0]
        self.last_name = full_name[1]
        self.email = full_name[0] + "email.com"
        self.password = generate_random_string_with_numbers(self.max_length)
        self.phone = str(generate_random_phone_number())
        self.user_status = 1

        body = {
            'id': self.user_id,
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'userStatus': self.user_status
        }

        response = post_request_api(self.user_endpoint, body, res_content_type='json')

        assert(response.status_code == 200)
        assert(body == response.json())

    def test_create_new_user_invalid_input(self):
        full_name = generate_random_name().split()

        body = {
            'id': generate_random_number(self.max_number),
            'username': full_name[0] + full_name[1],
            'firstName': full_name[0],
            'lastName': full_name[1],
            'email': full_name[0] + "email.com",
            'password': generate_random_string_with_numbers(self.max_length),
            'phone': str(generate_random_phone_number()),
            'userStatus': 1
        }

        response = put_request_api(self.user_endpoint, body, res_content_type='json')
        
        assert(response.status_code == 405)

    def test_create_new_user_bad_request(self):
        full_name = generate_random_name().split()

        body = {
            'id': generate_random_string_with_numbers(self.max_length),
            'username': full_name[0] + full_name[1],
            'firstName': full_name[0],
            'lastName': full_name[1],
            'email': full_name[0] + "email.com",
            'password': generate_random_string_with_numbers(self.max_length),
            'phone': str(generate_random_phone_number()),
            'userStatus': 1
        }

        response = post_request_api(self.user_endpoint, body, res_content_type='json')
        
        assert(response.status_code == 400)
