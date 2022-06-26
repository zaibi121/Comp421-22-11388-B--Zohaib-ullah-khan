Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from Crypto.Cipher import AES
import base64


class Win32Crypto:
    #
    # key = 32 bytes ,  0<number(int)<128
    def __init__(self, key: bytes, number: int):
        self.key = key
        self.number = number

    #
    #
    @staticmethod
    def __byte_xor(data: bytes, number: int) -> bytes:
        return bytes([b ^ number for b in data])

    #
    #
    def encrypt(self, data):
        try:
            cipher = AES.new(self.key, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(data)
            base64_nonce = (base64.b64encode((cipher.nonce)).replace(b'=', b''))  # 22 byte(s)
            base64_tag = (base64.b64encode((tag)).replace(b'=', b''))  # 22 byte(s)
            data = base64_nonce + base64_tag + ciphertext
            return True, Win32Crypto.__byte_xor(data, self.number)
        except:
            return False, b''

    #
    #
    def decrypt(self, data):
        if len(data) > 43:
            try:
                data = Win32Crypto.__byte_xor(data, self.number)
                base64_nonce = data[0:22] + b'=='
                base64_tag = data[22:44] + b'=='
                ciphertext = data[44:]
                tag = base64.b64decode(base64_tag)
                nonce = base64.b64decode(base64_nonce)
                cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
                res = cipher.decrypt_and_verify(ciphertext, tag)
                return True, res
            except:
                return False, b''
        else:
            return False, b''