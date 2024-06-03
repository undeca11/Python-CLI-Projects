from os import path, urandom
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode

class FernetEncrypter:
    def __init__(self, password: bytes, filepath: Path, salt_path = path.join(path.dirname(__file__), 'salt.fernet')) -> None:
        self.password = password
        self.filepath = filepath
        self.salt_path = salt_path
        self.p = Path(self.salt_path)
        if path.exists(self.salt_path) != True:
            self.p.write_bytes(urandom(16))
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
        self.filename, self.extension = path.splitext(self.filepath)
        self.extension = self.extension.encode()
        self.p = Path(self.filepath)
        self.data = self.p.read_bytes()
        self.data = self.data + self.extension
        self.p.write_bytes(self.f.encrypt(self.data))
        self.target = Path(self.filepath.replace(self.extension.decode(),'.fernet'))
        self.p.rename(self.target)
        self.filepath = self.target

    def decrypt(self):
        self.p = Path(self.filepath)
        self.data = self.p.read_bytes()
        try:
            self.data = self.f.decrypt(self.data).decode()
        except InvalidToken:
            print("InvalidToken Error")
        else:
            self._old_extension = self.data[self.data.rfind('.'):]
            self.data = self.data[:self.data.rfind('.')].encode()
            self.p.write_bytes(self.data)
            self.target = Path(str(self.filepath).replace('.fernet',self._old_extension))
            self.p.rename(self.target)
            self.filepath = self.target