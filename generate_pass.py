from cryptography.fernet import Fernet

class Generate_pass:

    def generate(self):
        pass_secret = Fernet.generate_key()
        return pass_secret
