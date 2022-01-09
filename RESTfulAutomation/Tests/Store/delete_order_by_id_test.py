from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet
from Helper.Common.create_order import create_order

class TestDeleteOrderById(unittest.TestCase):

    store_order_endpoint = get_config_data('STORE_ENDPOINT') + '/order'

    def setUp(self):
        order_data = self._create_new_pet_order()
        self.order_id = order_data['id']

    def test_delete_order_by_id(self):
        response = delete_request_api(self.store_order_endpoint + '/{}'.format(self.order_id))

        assert(response.status_code == 200)
        
        response = get_request_api(self.store_order_endpoint + '/{}'.format(self.order_id))

        assert(response.status_code == 404)
        assert(response.text == 'Order not found')

    def test_delete_order_by_id_bad_request(self):
        bad_format_id = 'wqf234432d'
        response = delete_request_api(self.store_order_endpoint + '/{}'.format(bad_format_id))

        assert(response.status_code == 400)

    def _create_new_pet_order(self, status = 'approved'):
        max_number = get_config_data('MAX_NUMBER')
        max_length = get_config_data('MAX_LENGTH')

        created_pet = create_pet(max_number, max_length)
        pet_id = created_pet['pet_id']
        return create_order(max_number, pet_id, status)
