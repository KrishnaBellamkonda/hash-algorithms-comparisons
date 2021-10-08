# This has all of the dictionaries and constants 
import hashlib
hash_map_dict = {
    "SHA1":hashlib.sha1,
    "SHA256":hashlib.sha256,
    "SHA224":hashlib.sha224,
    "SHA512":hashlib.sha512,
    "SHA3_512":hashlib.sha3_512,
    "SHA_256":hashlib.sha3_256,
    "SHA3_224":hashlib.sha3_224,
    "MD5":hashlib.md5,
    "Blake2b":hashlib.blake2b

}


# Save Paths
FILE_PATH = "./t8.shakespeare.txt"
MEMORY_LOG_PATH = "./memory/"