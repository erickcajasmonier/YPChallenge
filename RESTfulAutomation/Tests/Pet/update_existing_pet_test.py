from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

class TestUpdateExistingPet(unittest.TestCase):

    pet_endpoint = get_endpoint_data('PET_ENDPOINT')
    max_number = get_endpoint_data('MAX_NUMBER')
    max_lenght = get_endpoint_data('MAX_LENGTH')

    def setUp(self):
        self.pet_id = generate_random_number(self.max_number)

        body = {
            'id': self.pet_id,
            'name': generate_random_name(),
            'category': {
                'id': generate_random_number(self.max_number),
                'name': generate_random_animal()
            },
            'photoUrls': ['https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))],
            'tags': [{
                'id': generate_random_number(self.max_number),
                'name': generate_random_string(self.max_lenght)
            }],
            'status': 'available'
        }

        post_request_api(self.pet_endpoint, body)

    def test_update_existing_pet(self):
        name = generate_random_name()
        category_id = generate_random_number(self.max_number)
        category_name = generate_random_animal()
        photo_url_one = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))
        photo_url_two = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))
        tags_id = generate_random_number(self.max_number)
        tags_name = generate_random_string(self.max_lenght)

        body = {
            'id': self.pet_id,
            'name': name,
            'category': {
                'id': category_id,
                'name': category_name
            },
            'photoUrls': [photo_url_one, photo_url_two],
            'tags': [{
                'id': tags_id,
                'name': tags_name
            }],
            'status': 'available'
        }

        response = put_request_api(self.pet_endpoint, body)
        
        assert(response.status_code == 200)
        assert(get_xml_element_value('id', response) == str(self.pet_id))
        assert(get_xml_element_value('name', response) == name)
        assert(get_xml_element_value('category/id', response) == str(category_id))
        assert(get_xml_element_value('category/name', response) == category_name)
        assert(get_xml_element_values('photoUrls/photoUrl', response)[0] == photo_url_one)
        assert(get_xml_element_values('photoUrls/photoUrl', response)[1] == photo_url_two)
        assert(get_xml_element_value('tags/tag/id', response) == str(tags_id))
        assert(get_xml_element_value('tags/tag/name', response) == tags_name)
        assert(get_xml_element_value('status', response) == 'available')

    def test_update_not_existing_pet(self):
        bad_id = 9999999

        body = {
            'id': bad_id,
            'name': generate_random_name(),
            'category': {
                'id': generate_random_number(self.max_number),
                'name': generate_random_animal()
            },
            'photoUrls': ['https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))],
            'tags': [{
                'id': generate_random_number(self.max_number),
                'name': generate_random_string(self.max_lenght)
            }],
            'status': 'unavailable'
        }

        response = put_request_api(self.pet_endpoint, body, res_content_type='json')
        
        assert(response.status_code == 404)
        assert(response.text == 'Pet not found')

    def test_update_existing_pet_bad_request(self):
        body = {
            'id': generate_random_string_with_numbers(self.max_number),
            'name': generate_random_name(),
            'category': {
                'id': generate_random_number(self.max_number),
                'name': generate_random_animal()
            },
            'photoUrls': ['https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))],
            'tags': [{
                'id': generate_random_number(self.max_number),
                'name': generate_random_string(self.max_lenght)
            }],
            'status': 'unavailable'
        }

        response = put_request_api(self.pet_endpoint, body)
        
        assert(response.status_code == 400)
