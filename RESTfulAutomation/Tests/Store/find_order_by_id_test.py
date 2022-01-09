from Helper.Common.data_helper import *
from Helper.Common.request_helper import *
from Helper.Common.create_pet import create_pet
from Helper.Common.create_order import create_order

class TestFindOrderById(unittest.TestCase):

    store_order_endpoint = get_config_data('STORE_ENDPOINT') + '/order'

    def setUp(self):
        order_data = self._create_new_pet_order()
        self.order_id = order_data['id']
        self.pet_id = order_data['pet_id'],
        self.quantity = order_data['quantity'],
        self.ship_date = order_data['ship_date'].replace('+00:00', 'Z'),
        self.status = order_data['status'],
        self.complete = order_data['complete']

    def test_find_order_by_id(self):
        response = get_request_api(self.store_order_endpoint + '/{}'.format(self.order_id))

        assert(response.status_code == 200)
        assert(get_xml_element_value('id', response) == str(self.order_id))
        assert(get_xml_element_value('petId', response) == str(self.pet_id[0]))
        assert(get_xml_element_value('quantity', response) == str(self.quantity[0]))
        assert(get_xml_element_value('shipDate', response) == self.ship_date[0])
        assert(get_xml_element_value('status', response) == self.status[0])
        assert(get_xml_element_value('complete', response) == str(self.complete).lower())

    def test_find_order_by_id_not_found(self):
        wrong_id = 999999999
        response = get_request_api(self.store_order_endpoint + '/{}'.format(wrong_id))

        assert(response.status_code == 404)
        assert(response.text == 'Order not found')

    def test_find_order_by_id_bad_request(self):
        bad_format_id = 'wqf234432d'
        response = get_request_api(self.store_order_endpoint + '/{}'.format(bad_format_id))

        assert(response.status_code == 400)

    def _create_new_pet_order(self, status = 'approved'):
        max_number = get_config_data('MAX_NUMBER')
        max_length = get_config_data('MAX_LENGTH')

        created_pet = create_pet(max_number, max_length)
        pet_id = created_pet['pet_id']
        return create_order(max_number, pet_id, status)
