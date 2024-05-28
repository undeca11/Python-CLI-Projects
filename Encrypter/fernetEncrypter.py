import os
import pathlib
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode
from secrets import token_hex

class fernetEncrypter:
    def __init__(self, password, filepath: str) -> None:
        self.filepath = filepath
        self.password = password.encode()
        self.saltFilepath = os.path.join(os.path.dirname(__file__), 'salt.fernet')
        self.p = pathlib.Path(self.saltFilepath)
        if os.path.exists(self.saltFilepath) != True:
            self.p.write_bytes(os.urandom(16))
        self.salt = self.p.read_bytes()
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=480000,
        )
        self.key = urlsafe_b64encode(self.kdf.derive(self.password))
        self.f = Fernet(self.key)
    
    def encrypt(self):
        self.filename, self.extension = os.path.splitext(self.filepath)
        self.extension = self.extension.encode()
        self.p = pathlib.Path(self.filepath)
        self.data = self.p.read_bytes()
        self.data = self.data + self.extension
        self.p.write_bytes(self.f.encrypt(self.data))
        self.target = pathlib.Path(self.filepath.replace(self.extension.decode(),'.fernet'))
        self.p.rename(self.target)
        self.filepath = self.target

    def decrypt(self):
        self.p = pathlib.Path(self.filepath)
        self.data = self.p.read_bytes()
        self.data = self.f.decrypt(self.data).decode()
        self.oldExtension = self.data[self.data.rfind('.'):]
        self.data = self.data[:self.data.rfind('.')].encode()
        self.p.write_bytes(self.data)
        self.target = pathlib.Path(str(self.filepath).replace('.fernet',self.oldExtension))
        self.p.rename(self.target)
        self.filepath = self.target