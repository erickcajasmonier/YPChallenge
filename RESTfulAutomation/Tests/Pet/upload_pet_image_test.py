from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet

class TestUploadPetImage(unittest.TestCase):

    pet_endpoint = get_config_data('PET_ENDPOINT')
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        created_pet = create_pet(self.max_number, self.max_length)
        self.pet_id = created_pet['pet_id']
        self.photo_url_one = created_pet['photo_url_one']

    def test_upload_pet_image(self):
        file = {'media': open(get_image_path('Dog.jpg'), 'rb')}

        response = post_files_request_api(self.pet_endpoint + '/{}/uploadImage'.format(self.pet_id), 
                                          file, req_body_type='octet-stream', res_content_type='json')
        json_response = response.json()
        
        assert(response.status_code == 200)
        assert(json_response['id'] == self.pet_id)
        assert(json_response['photoUrls'][0] == self.photo_url_one)
        assert(json_response['photoUrls'][1].startswith('/tmp/inflector') is True)
        assert(json_response['photoUrls'][1].endswith('.tmp') is True)

    def test_upload_pet_image_pet_not_found(self):
        wrong_pet_id = 9999999999
        file = {'media': open(get_image_path('Dog.jpg'), 'rb')}

        response = post_files_request_api(self.pet_endpoint + '/{}/uploadImage'.format(wrong_pet_id), 
                                          file, req_body_type='octet-stream', res_content_type='json')

        assert(response.status_code == 404)
        assert(response.text == 'Pet not found')
