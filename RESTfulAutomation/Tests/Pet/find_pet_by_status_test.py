from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

class TestUpdateExistingPetFormData(unittest.TestCase):

    pet_endpoint = get_endpoint_data('PET_ENDPOINT')
    pet_status_endpoint = pet_endpoint + '/findByStatus?status='
    pet_status_list = ['available', 'pending', 'sold']

    def setUp(self):
        max_number = get_endpoint_data('MAX_NUMBER')
        max_lenght = get_endpoint_data('MAX_LENGTH')

        for status in self.pet_status_list:
            body = {
                'id': generate_random_number(max_number),
                'name': generate_random_name(),
                'category': {
                    'id': generate_random_number(max_number),
                    'name': generate_random_animal()
                },
                'photoUrls': ['https://www.{}.com'.format(generate_random_string_with_numbers(max_lenght))],
                'tags': [{
                    'id': generate_random_number(max_number),
                    'name': generate_random_string(max_lenght)
                }],
                'status': status
            }

            post_request_api(self.pet_endpoint, body)

    def test_find_pet_by_available_status(self):
        available_status = self.pet_status_list[0]

        response = get_request_api(self.pet_status_endpoint + available_status)
        
        assert(response.status_code == 200)
        for pet_status in get_xml_element_values('item/status', response):
            assert(pet_status == available_status)

    def test_find_pet_by_pending_status(self):
        pending_status = self.pet_status_list[1]

        response = get_request_api(self.pet_status_endpoint + pending_status)
        
        assert(response.status_code == 200)
        for pet_status in get_xml_element_values('item/status', response):
            assert(pet_status == pending_status)

    def test_find_pet_by_sold_status(self):
        sold_status = self.pet_status_list[2]

        response = get_request_api(self.pet_status_endpoint + sold_status)
        
        assert(response.status_code == 200)
        for pet_status in get_xml_element_values('item/status', response):
            assert(pet_status == sold_status)

    def test_find_pet_by_status_bad_request(self):
        wrong_status = 34953

        response = get_request_api(self.pet_status_endpoint + str(wrong_status))
        
        assert(response.status_code == 400)
