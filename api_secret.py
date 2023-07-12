from cryptography.fernet import Fernet
from generate_pass import Generate_pass
import json


generate_pass = Generate_pass()
encryption_key = generate_pass.generate()

class Api_secret:
    def __init__(self):
        self.encryption_key = encryption_key

    def encrypt_api_key(self, api_key):
        f = Fernet(self.encryption_key)
        encrypted_api_key = f.encrypt(api_key.encode()).decode()
        return encrypted_api_key

    def decrypt_api_key(self, encrypted_api_key):
        f = Fernet(self.encryption_key)
        decrypted_api_key = f.decrypt(encrypted_api_key.encode()).decode()
        return decrypted_api_key

    def get_decrypted_api_key(self):

        try:
            with open('api_key.json', 'r') as file:
                data = json.load(file)
                api_key = data["api_key"]

                encrypted_api_key = self.encrypt_api_key(api_key)
                decrypted_api_key = self.decrypt_api_key(encrypted_api_key)

                return decrypted_api_key
        
        except FileNotFoundError:
            print('api_key.json file not found')
            return None
        except json.JSONDecodeError:
            print('Error decofing api_key.json file')
            return None
