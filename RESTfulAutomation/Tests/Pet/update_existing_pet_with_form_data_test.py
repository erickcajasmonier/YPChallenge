from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

class TestUpdateExistingPetFormData(unittest.TestCase):

    pet_endpoint = get_endpoint_data('PET_ENDPOINT')
    max_number = get_endpoint_data('MAX_NUMBER')
    max_lenght = get_endpoint_data('MAX_LENGTH')

    def setUp(self):
        self.pet_id = generate_random_number(self.max_number)
        self.category_id = generate_random_number(self.max_number)
        self.category_name = generate_random_animal()
        self.photo_url_one = 'https://www.{}.com'.format(generate_random_string_with_numbers(self.max_lenght))
        self.tags_id = generate_random_number(self.max_number)
        self.tags_name = generate_random_string(self.max_lenght)

        body = {
            'id': self.pet_id,
            'name': generate_random_name(),
            'category': {
                'id': self.category_id,
                'name': self.category_name
            },
            'photoUrls': [self.photo_url_one],
            'tags': [{
                'id': self.tags_id,
                'name': self.tags_name
            }],
            'status': 'unavailable'
        }

        post_request_api(self.pet_endpoint, body)

    def test_update_existing_pet_form_data(self):
        name = generate_random_name()
        status = 'available'

        response = post_request_api(self.pet_endpoint + '/{}?name={}&status={}'.format(self.pet_id, name, status),
                                    res_content_type='json')
        json_response = response.json()
        
        assert(response.status_code == 200)
        assert(json_response['id'] == self.pet_id)
        assert(json_response['name'] == name)
        assert(json_response['category']['id'] == self.category_id)
        assert(json_response['category']['name'] == self.category_name)
        assert(json_response['photoUrls'][0] == self.photo_url_one)
        assert(json_response['tags'][0]['id'] == self.tags_id)
        assert(json_response['tags'][0]['name'] == self.tags_name)
        assert(json_response['status'] == status)

    def test_update_not_existing_pet_form_data(self):
        bad_id = 9999999
        name = generate_random_name()
        status = 'available'

        response = post_request_api(self.pet_endpoint + '/{}?name={}&status={}'.format(bad_id, name, status),
                                    res_content_type='json')
        
        assert(response.status_code == 404)
        assert(response.text == 'Pet not found')

    def test_update_existing_pet_bad_request_form_data(self):
        id = generate_random_string_with_numbers(self.max_number)
        name = generate_random_name()
        status = 'available'

        response = post_request_api(self.pet_endpoint + '/{}?name={}&status={}'.format(id, name, status),
                                    res_content_type='json')
        
        assert(response.status_code == 400)
