from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_user import create_user

class TestFindUserByUsername(unittest.TestCase):

    user_endpoint = get_config_data('USER_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        user_data = create_user(self.max_number, self.max_length)
        self.user_id = user_data['user_id'],
        self.username = user_data['username'],
        self.first_name = user_data['first_name'],
        self.last_name = user_data['last_name'],
        self.email = user_data['email'],
        self.password = user_data['password'],
        self.phone = user_data['phone'],
        self.user_status = user_data['user_status']

    def test_find_user_by_username(self):
        response = get_request_api(self.user_endpoint + '/{}'.format(self.username[0]))

        assert(response.status_code == 200)
        assert(get_xml_element_value('id', response) == str(self.user_id[0]))
        assert(get_xml_element_value('username', response) == self.username[0])
        assert(get_xml_element_value('firstName', response) == self.first_name[0])
        assert(get_xml_element_value('lastName', response) == self.last_name[0])
        assert(get_xml_element_value('email', response) == self.email[0])
        assert(get_xml_element_value('password', response) == self.password[0])
        assert(get_xml_element_value('phone', response) == self.phone[0])
        assert(get_xml_element_value('userStatus', response) == str(self.user_status))

    def test_find_user_by_invalid_username(self):
        wrong_username = generate_random_name() + '2134'

        response = get_request_api(self.user_endpoint + '/{}'.format(wrong_username))
        
        assert(response.status_code == 404)
        assert(response.text == 'User not found')
