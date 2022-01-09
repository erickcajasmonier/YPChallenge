import requests
from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

def create_pet(max_number, max_length, status = 'available'):
    pet_endpoint = get_config_data('PET_ENDPOINT')

    pet_dict = {
        'pet_id': generate_random_number(max_number),
        'name': generate_random_name(),
        'category_id': generate_random_number(max_number),
        'category_name': generate_random_animal(),
        'photo_url_one': 'https://www.{}.com'.format(generate_random_string_with_numbers(max_length)),
        'tags_id': generate_random_number(max_number),
        'tags_name': generate_random_string(max_length),
        'status': status
    }

    body = {
                'id': pet_dict['pet_id'],
                'name': pet_dict['name'],
                'category': {
                    'id': pet_dict['category_id'],
                    'name': pet_dict['category_name']
                },
                'photoUrls': [pet_dict['photo_url_one']],
                'tags': [{
                    'id': pet_dict['tags_id'],
                    'name': pet_dict['tags_name']
                }],
                'status': pet_dict['status']
            }

    post_request_api(pet_endpoint, body)

    return pet_dict