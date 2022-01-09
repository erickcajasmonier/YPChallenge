from Helper.Common.data_helper import *
from Helper.Common.request_helper import *

def create_order(max_number, pet_id, status = 'approved', complete = True):
    store_order_endpoint = get_config_data('STORE_ENDPOINT') + '/order'

    order_dict = {
        'id': generate_random_number(max_number),
        'pet_id': pet_id,
        'quantity': generate_random_number(max_number),
        'ship_date': get_date(),
        'status': status,
        'complete': complete
    }

    body = {
        'id': order_dict['id'],
        'petId': order_dict['pet_id'],
        'quantity': order_dict['quantity'],
        'shipDate': order_dict['ship_date'],
        'status': order_dict['status'],
        'complete': order_dict['complete']
    }

    post_request_api(store_order_endpoint, body, res_content_type='json')

    return order_dict