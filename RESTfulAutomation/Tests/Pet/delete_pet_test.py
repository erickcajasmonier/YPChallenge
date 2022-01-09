from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

class TestUpdateExistingPetFormData(unittest.TestCase):

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

    def test_delete_pet(self):
        response = delete_request_api(self.pet_endpoint + '/{}'.format(self.pet_id),
                                      res_content_type='json')
        
        assert(response.status_code == 200)
        assert(response.text == 'Pet deleted')

        response = get_request_api(self.pet_endpoint + '/{}'.format(self.pet_id),
                                   res_content_type='json')
        
        assert(response.status_code == 404)
        assert(response.text == 'Pet not found')

    def test_delete_pet_bad_request(self):
        wrong_id = generate_random_string_with_numbers(self.max_number)

        response = delete_request_api(self.pet_endpoint + '/{}'.format(wrong_id))
        
        assert(response.status_code == 400)
