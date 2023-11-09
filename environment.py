from dotenv import load_dotenv
import os

class Environment:    
    def __init__(self):
        load_dotenv()

    def get_username(self):
        return os.getenv('USERNAME')

    def get_password(self):
        return os.getenv('PASSWORD')
