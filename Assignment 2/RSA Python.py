from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

kp = RSA.generate (3072)
PublicKey = kp.publickey()

print(f"Generated Public Key: (n={hex(PublicKey.n)}, e={hex(PublicKey.e)})")

PublicKP = PublicKey.exportKey()

print (PublicKP.decode('ascii'))

print(f"Generated Private Key: (n={hex(PublicKey.n)}, d={hex(kp.d)})")

PrivateKP = kp.exportKey()

print (PrivateKP.decode('ascii'))

f=open('string file','r')
string==f.readline()

string = b'This is just a Text for Testing the code'

enc = PKCS1_OAEP.new(PublicKey)

eresult = enc.encrypt(string)

print ("Generated Encrypted Form:", binascii.hexlify(eresult))

dc = PKCS1_OAEP.new(kp)

dresult = dc.decrypt(eresult)

print("Generated Decrypted Form is:", dresult)
