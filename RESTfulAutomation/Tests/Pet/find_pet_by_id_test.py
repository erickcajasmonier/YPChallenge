from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet

class TestFindPetById(unittest.TestCase):

    pet_endpoint = get_config_data('PET_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        created_pet = create_pet(self.max_number, self.max_length)
        self.pet_id = created_pet['pet_id']
        self.name = created_pet['name']
        self.category_id = created_pet['category_id']
        self.category_name = created_pet['category_name']
        self.photo_url_one = created_pet['photo_url_one']
        self.tags_id = created_pet['tags_id']
        self.tags_name = created_pet['tags_name']
        self.status = created_pet['status']

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
