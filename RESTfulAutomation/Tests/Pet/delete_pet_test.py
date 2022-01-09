from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet

class TestDeletePet(unittest.TestCase):

    pet_endpoint = get_config_data('PET_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        created_pet = create_pet(self.max_number, self.max_length)
        self.pet_id = created_pet['pet_id']

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
