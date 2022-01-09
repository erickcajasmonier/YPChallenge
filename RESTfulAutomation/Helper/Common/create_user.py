from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

def create_user(max_number, max_length):
    user_endpoint = get_config_data('USER_ENDPOINT')
    full_name = generate_random_name().split()

    user_dict = {
        'user_id': generate_random_number(max_number),
        'username': full_name[0] + full_name[1],
        'first_name': full_name[0],
        'last_name': full_name[1],
        'email': full_name[0] + "email.com",
        'password': generate_random_string_with_numbers(max_length),
        'phone': str(generate_random_phone_number()),
        'user_status': 1
    }

    body = {
        'id': user_dict['user_id'],
        'username': user_dict['username'],
        'firstName': user_dict['first_name'],
        'lastName': user_dict['last_name'],
        'email': user_dict['email'],
        'password': user_dict['password'],
        'phone': user_dict['phone'],
        'userStatus': user_dict['user_status']
    }

    post_request_api(user_endpoint, body, res_content_type='json')

    return user_dict
