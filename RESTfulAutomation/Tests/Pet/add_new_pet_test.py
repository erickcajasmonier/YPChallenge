from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

class TestAddNewPet(unittest.TestCase):

    pet_endpoint = get_config_data('PET_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def test_add_new_available_pet_to_store(self):
        id = generate_random_number(self.max_number)
        name = generate_random_name()
        category_id = generate_random_number(self.max_number)
        category_name = generate_random_animal()
        photo_url_one = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_length))
        photo_url_two = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_length))
        tags_id = generate_random_number(self.max_number)
        tags_name = generate_random_string(self.max_length)

        body = {
            'id': id,
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

        response = post_request_api(self.pet_endpoint, body)
        
        assert(response.status_code == 200)
        assert(get_xml_element_value('id', response) == str(id))
        assert(get_xml_element_value('name', response) == name)
        assert(get_xml_element_value('category/id', response) == str(category_id))
        assert(get_xml_element_value('category/name', response) == category_name)
        assert(get_xml_element_values('photoUrls/photoUrl', response)[0] == photo_url_one)
        assert(get_xml_element_values('photoUrls/photoUrl', response)[1] == photo_url_two)
        assert(get_xml_element_value('tags/tag/id', response) == str(tags_id))
        assert(get_xml_element_value('tags/tag/name', response) == tags_name)
        assert(get_xml_element_value('status', response) == 'available')

    def test_add_new_unavailable_pet_to_store(self):
        id = generate_random_number(self.max_number)
        name = generate_random_name()
        category_id = generate_random_number(self.max_number)
        category_name = generate_random_animal()
        photo_url_one = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_length))
        tags_id = generate_random_number(self.max_number)
        tags_name = generate_random_string(self.max_length)

        body = {
            'id': id,
            'name': name,
            'category': {
                'id': category_id,
                'name': category_name
            },
            'photoUrls': [photo_url_one],
            'tags': [{
                'id': tags_id,
                'name': tags_name
            }],
            'status': 'unavailable'
        }

        response = post_request_api(self.pet_endpoint, body)
        
        assert(response.status_code == 200)
        assert(get_xml_element_value('id', response) == str(id))
        assert(get_xml_element_value('name', response) == name)
        assert(get_xml_element_value('category/id', response) == str(category_id))
        assert(get_xml_element_value('category/name', response) == category_name)
        assert(get_xml_element_value('photoUrls/photoUrl', response) == photo_url_one)
        assert(get_xml_element_value('tags/tag/id', response) == str(tags_id))
        assert(get_xml_element_value('tags/tag/name', response) == tags_name)
        assert(get_xml_element_value('status', response) == 'unavailable')

    @pytest.mark.skip(reason="Endpoint is not working for Invalid input - 405")
    def test_add_new_pet_to_store_invalid_input(self):
        body = {
            'id': generate_random_string_with_numbers(self.max_number),
            'name': generate_random_name(),
            'category': {
                'id': generate_random_number(self.max_number),
                'name': generate_random_animal()
            },
            'photoUrls': ['https://www.{}.com'.format(generate_random_string_with_numbers(self.max_length))],
            'tags': [{
                'id': generate_random_number(self.max_number),
                'name': generate_random_string(self.max_length)
            }],
            'status': 'available'
        }

        response = post_request_api(self.pet_endpoint, body, 'xml')
        
        assert(response.status_code == 405)

    def test_add_new_pet_to_store_bad_request(self):
        body = {
            'id': generate_random_number(self.max_number),
            'name': generate_random_name(),
            'category': {
                'id': generate_random_number(self.max_number),
                'name': generate_random_animal()
            },
            'photoUrls': ['https://www.{}.com'.format(generate_random_string_with_numbers(self.max_length))],
            'tags': [{
                'id': generate_random_number(self.max_number),
                'name': generate_random_string(self.max_length)
            }],
            'status': 'available'
        }

        response = post_request_api(self.pet_endpoint, body, 'xml')
        
        assert(response.status_code == 400)
