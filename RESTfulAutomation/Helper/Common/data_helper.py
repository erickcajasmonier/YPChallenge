import random
import string
from dotenv import load_dotenv
from faker import Faker

fake = Faker()

def initialize_environment():
    load_dotenv()

def generate_random_number(max_number):
    return random.randint(0,max_number)

def generate_random_name():
    return fake.name()

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