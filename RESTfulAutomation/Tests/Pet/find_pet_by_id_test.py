from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

class TestFindPetById(unittest.TestCase):

    pet_endpoint = get_config_data('PET_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_lenght = get_config_data('MAX_LENGTH')

    def setUp(self):
        self.pet_id = generate_random_number(self.max_number)
        self.name = generate_random_name()
        self.category_id = generate_random_number(self.max_number)
        self.category_name = generate_random_animal()
        self.photo_url_one = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))
        self.tags_id = generate_random_number(self.max_number)
        self.tags_name = generate_random_string(self.max_lenght)
        self.status = 'available'

        body = {
            'id': self.pet_id,
            'name': self.name,
            'category': {
                'id': self.category_id,
                'name': self.category_name
            },
            'photoUrls': [self.photo_url_one],
            'tags': [{
                'id': self.tags_id,
                'name': self.tags_name
            }],
            'status': self.status
        }

        post_request_api(self.pet_endpoint, body)

    def test_find_pet_by_id(self):
        response = get_request_api(self.pet_endpoint + '/{}'.format(self.pet_id))
        
        assert(response.status_code == 200)
        assert(get_xml_element_value('id', response) == str(self.pet_id))
        assert(get_xml_element_value('name', response) == self.name)
        assert(get_xml_element_value('category/id', response) == str(self.category_id))
        assert(get_xml_element_value('category/name', response) == self.category_name)
        assert(get_xml_element_value('photoUrls/photoUrl', response) == self.photo_url_one)
        assert(get_xml_element_value('tags/tag/id', response) == str(self.tags_id))
        assert(get_xml_element_value('tags/tag/name', response) == self.tags_name)
        assert(get_xml_element_value('status', response) == self.status)

    def test_find_pet_by_id_not_found(self):
        not_found_id = 999999
        
        response = get_request_api(self.pet_endpoint + '/{}'.format(not_found_id),
                                   res_content_type='json')
        
        assert(response.status_code == 404)
        assert(response.text == 'Pet not found')

    def test_find_pet_by_id_bad_request(self):
        wrong_id = generate_random_string_with_numbers(self.max_number)

        response = get_request_api(self.pet_endpoint + '/{}'.format(wrong_id))
        
        assert(response.status_code == 400)
