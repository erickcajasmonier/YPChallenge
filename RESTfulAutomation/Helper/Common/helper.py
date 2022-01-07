import unittest
from dotenv import load_dotenv
from faker import Faker

fake = Faker()

def initialize_environment():
    load_dotenv()

def generateRandomName():
    return fake.name()