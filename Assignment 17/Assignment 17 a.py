'''
Use any one of the library and compress and decompress the file
'''
import zlib

# To see the original string length
string = b'This is the original string that will be compressed.'
print(len(string))

# To compress the string
com_string = zlib.compress(string)
print(len(com_string))

# To decompress the string
print(zlib.decompress(com_string))

zlib.crc32(string)