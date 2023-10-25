from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from binascii import hexlify
from typing import Tuple

def nonce_info( cipher )-> Tuple[ bytes, int ]:
  """returns nonce value and nonce length """
  ## BEGIN CODE TO BE CHANGED
  nonce = b''
  nonce_len = 0
  ## END CODE TO BE CHANGED
  return nonce, nonce_len 

print( "================================================" )
print( "====== Alice and Bob Secure Communication ======" )
print( "================================================" )
## secret key shared by Alice and Bob
key = get_random_bytes(16)

## Alice
alice_plaintext = b"secret"
print("Alice plaintext is: %s"%alice_plaintext)
##    - 1. initilaization of the cipher
alice_cipher = AES.new(key, AES.MODE_GCM,\
                       nonce=None, mac_len=16)
##    - 2. encryption, authentication
ciphertext, icv = \
  alice_cipher.encrypt_and_digest(alice_plaintext)

print( "The encrypted message sent by Alice to Bob is:" )
print( f"    - ciphertext: {hexlify( ciphertext, sep=' ' )}" ) 
print( f"    - icv: {hexlify(icv, sep=' ' )}" )
nonce, nonce_len = nonce_info( alice_cipher )
print( f"    - nonce [{nonce_len} bytes ]: {hexlify( nonce, sep=' ' )}" )

## Bob
bob_cipher = AES.new(key, AES.MODE_GCM,\
                     nonce=nonce,\
                     mac_len=16)

bob_plaintext = \
  bob_cipher.decrypt_and_verify(ciphertext, icv)
print("Bob plaintext is: %s"%bob_plaintext)

## secret key shared by Alice and Bob
key = b''
nonce_dict = {
  'nonce_0': b'', \
  'nonce_1': b'', \
  'nonce_2': b'', \
  'nonce_3': b'' }
clear_text = "secret"

def encrypt_and_digest( key:bytes, nonce_dict:dict, clear_text:bytes ) -> dict:
  """ return a dictionary that associates to any nonce label a uplet 
      ( nonce, cipher_text, icv ) corresponding to the cipher_text and icv 
      of the encrypted clear_text
  """
  output_dict = {}
  ## BEGIN CODE TO BE CHANGED


  ## END CODE TO BE CHANGED
  return output_dict


