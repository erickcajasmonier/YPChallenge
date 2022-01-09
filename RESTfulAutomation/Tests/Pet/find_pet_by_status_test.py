from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet

class TestFindPetByStatus(unittest.TestCase):

    pet_status_endpoint = get_config_data('PET_ENDPOINT') + '/findByStatus?status='
    pet_status_list = ['available', 'pending', 'sold']

    def setUp(self):
        max_number = get_config_data('MAX_NUMBER')
        max_length = get_config_data('MAX_LENGTH')

        for status in self.pet_status_list:
            create_pet(max_number, max_length, status)

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
