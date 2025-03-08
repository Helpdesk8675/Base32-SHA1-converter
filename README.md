# Base32-SHA1-converter

This script is a command-line utility that generates a Base32-encoded SHA-1 hash of a specified input file. It utilizes the hashlib library to compute the SHA-1 hash and the base64 library to encode the hash in Base32 format. The script accepts two command-line arguments:

-i or --input: The path to the input file that you want to hash.

-o or --output: The path to the output file where the Base32-encoded hash will be written.

Upon execution, the script reads the input file in binary mode, computes the SHA-1 hash, encodes it in Base32, and writes the resulting hash to the specified output file. It also provides feedback in the console indicating that the hash has been successfully written to the output file. This utility is useful for file integrity verification, data deduplication, or any application where a unique identifier for file content is needed.
