from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_user import create_user

class TestUpdateUser(unittest.TestCase):

    user_endpoint = get_config_data('USER_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        user_data = create_user(self.max_number, self.max_length)
        self.username = user_data['username'],

    def test_update_user(self):
        full_name = generate_random_name().split()
        user_id = generate_random_number(self.max_number)
        first_name = full_name[0]
        last_name = full_name[1]
        email = full_name[0] + "email.com"
        password = generate_random_string_with_numbers(self.max_length)
        phone = str(generate_random_phone_number())
        user_status = 0

        body = {
            'id': user_id,
            'username': self.username[0],
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'password': password,
            'phone': phone,
            'userStatus': user_status
        }

        response = put_request_api(self.user_endpoint + '/{}'.format(self.username[0]), body, res_content_type='json')
        json_response = response.json()

        assert(response.status_code == 200)
        assert(json_response['id'] == user_id)
        assert(json_response['username'] == self.username[0])
        assert(json_response['firstName'] == first_name)
        assert(json_response['lastName'] == last_name)
        assert(json_response['email'] == email)
        assert(json_response['password'] == password)
        assert(json_response['phone'] == phone)
        assert(json_response['userStatus'] == user_status)

    def test_update_user_bad_request(self):
        full_name = generate_random_name().split()
        user_id = generate_random_string_with_numbers(self.max_length)
        first_name = full_name[0]
        last_name = full_name[1]
        email = full_name[0] + "email.com"
        password = generate_random_string_with_numbers(self.max_length)
        phone = str(generate_random_phone_number())
        user_status = 0

        body = {
            'id': user_id,
            'username': self.username,
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'password': password,
            'phone': phone,
            'userStatus': user_status
        }

        response = put_request_api(self.user_endpoint + '/{}'.format(self.username[0]), body, res_content_type='json')
        
        assert(response.status_code == 400)
