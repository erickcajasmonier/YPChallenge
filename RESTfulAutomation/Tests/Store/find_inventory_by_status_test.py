from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet
from Helper.Common.create_order import create_order

class TestFindInventoryByStatus(unittest.TestCase):

    store_inventory_endpoint = get_config_data('STORE_ENDPOINT') + '/inventory'
    status_list = ['approved', 'placed', 'delivered']

    def setUp(self):
        for status in self.status_list:
            self._create_new_pet_order(status)

    def test_find_inventory_by_approved(self):
        actual_response = self._get_actual_status_response()
        order_data = self._create_new_pet_order(self.status_list[0])
        order_quantity = order_data['quantity']

        response = get_request_api(self.store_inventory_endpoint, res_content_type='json')
        json_response = response.json()

        assert(response.status_code == 200)
        assert((actual_response['approved'] + order_quantity) == json_response['approved'])

    def test_find_inventory_by_placed(self):
        actual_response = self._get_actual_status_response()
        order_data = self._create_new_pet_order(self.status_list[1])
        order_quantity = order_data['quantity']

        response = get_request_api(self.store_inventory_endpoint, res_content_type='json')
        json_response = response.json()

        assert(response.status_code == 200)
        assert((actual_response['placed'] + order_quantity) == json_response['placed'])

    def test_find_inventory_by_delivered(self):
        actual_response = self._get_actual_status_response()
        order_data = self._create_new_pet_order(self.status_list[2])
        order_quantity = order_data['quantity']

        response = get_request_api(self.store_inventory_endpoint, res_content_type='json')
        json_response = response.json()

        assert(response.status_code == 200)
        assert((actual_response['delivered'] + order_quantity) == json_response['delivered'])

    def _create_new_pet_order(self, status):
        max_number = get_config_data('MAX_NUMBER')
        max_length = get_config_data('MAX_LENGTH')

        created_pet = create_pet(max_number, max_length)
        pet_id = created_pet['pet_id']
        return create_order(max_number, pet_id, status)

    def _get_actual_status_response(self):
        response = get_request_api(self.store_inventory_endpoint, res_content_type='json')
        return response.json()
