from base64 import b16decode, b64encode;

def hex_to_b64 ():
    print('Input hex:')
    data_hex = input()
    data_b64 = b64encode(b16decode(data_hex, casefold=True))
    print('b64:')
    print(data_b64)

hex_to_b64()
    

