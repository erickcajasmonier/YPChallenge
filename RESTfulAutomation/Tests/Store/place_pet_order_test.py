from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet

class TestPlacePetOrder(unittest.TestCase):

    store_order_endpoint = get_config_data('STORE_ENDPOINT') + '/order'
    max_number = get_config_data('MAX_NUMBER')
    max_length = get_config_data('MAX_LENGTH')

    def setUp(self):
        created_pet = create_pet(self.max_number, self.max_length)
        self.pet_id = created_pet['pet_id']

    def test_place_pet_order(self):
        id = generate_random_number(self.max_number)
        quantity = generate_random_number(self.max_number)
        ship_date = get_date()
        status = 'approved'
        complete = True

        body = {
            'id': id,
            'petId': self.pet_id,
            'quantity': quantity,
            'shipDate': ship_date,
            'status': status,
            'complete': complete
        }

        response = post_request_api(self.store_order_endpoint, body, res_content_type='json')
        assert(response.status_code == 200)
        assert(body == response.json())

    def test_place_pet_order_invalid_input(self):
        id = generate_random_number(self.max_number)
        quantity = generate_random_number(self.max_number)
        ship_date = get_date()
        status = 'approved'
        complete = True

        body = {
            'id': id,
            'petId': self.pet_id,
            'quantity': quantity,
            'shipDate': ship_date,
            'status': status,
            'complete': complete
        }

        response = put_request_api(self.store_order_endpoint, body,
                                   req_body_type='xml', res_content_type='json')
        assert(response.status_code == 405)

    def test_place_pet_order_bad_request(self):
        id = generate_random_number(self.max_number)
        pet_id = generate_random_string_with_numbers(self.max_length)
        quantity = generate_random_number(self.max_number)
        ship_date = get_date()
        status = 'approved'
        complete = True

        body = {
            'id': id,
            'petId': pet_id,
            'quantity': quantity,
            'shipDate': ship_date,
            'status': status,
            'complete': complete
        }

        response = post_request_api(self.store_order_endpoint, body, res_content_type='json')
        assert(response.status_code == 400)
