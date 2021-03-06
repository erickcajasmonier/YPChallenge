import os
import random
import string
import yaml
from dotenv import load_dotenv
from faker import Faker
from datetime import date, datetime, timedelta

fake = Faker()

def initialize_environment():
    load_dotenv()

def get_config_data(endpoint):
    dirname = os.path.dirname(__file__)
    file_path = os.path.join(dirname, '../../setup_config.yml')
    parsed_yaml_file = yaml.load(open(file_path), Loader=yaml.FullLoader)
    return parsed_yaml_file[endpoint]

def get_image_path(image_file_name):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, '../Images/' + image_file_name)

def generate_random_number(max_number):
    return random.randint(0, max_number)

def generate_random_name():
    return fake.name()

def generate_random_phone_number():
    return fake.phone_number()

def generate_random_string(lenght):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    return str("".join(random.choice(string.ascii_letters) for x in range(lenght)))

def generate_random_string_with_numbers(lenght):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return str("".join(random.choice(string.ascii_letters) for x in range(lenght)))

def generate_random_animal():
    animal_list = ['Dog', 'Cat', 'Parrot', 'Butterfly', 'Hog', 'Bird', 'Rooster',
                   'Turtle', 'Axolotl', 'Cuttlefish', 'Bat', 'Snake', 'Bandicoot',
                   'Raptor']
    return random.choice(animal_list)

def get_date(days_from_now = 0):
    date_time = datetime.now() + timedelta(days=days_from_now)
    return str(date_time).replace(' ', 'T')[:-3] + '+00:00'