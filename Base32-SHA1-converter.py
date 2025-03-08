import hashlib
import base64
import argparse

def sha1_base32(file_path):
    # Create a SHA1 hash object
    sha1 = hashlib.sha1()
    
    # Read the file in binary mode and update the hash
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    
    # Get the hexadecimal digest of the hash
    sha1_digest = sha1.digest()
    
    # Encode the SHA1 digest in Base32
    base32_encoded = base64.b32encode(sha1_digest)
    
    return base32_encoded.decode('utf-8')

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Generate Base32-encoded SHA1 hash of a file.')
    parser.add_argument('-i', '--input', required=True, help='Input file path')
    parser.add_argument('-o', '--output', required=True, help='Output file path')

    args = parser.parse_args()

    # Generate the hash
    base32_hash = sha1_base32(args.input)

    # Write the output to the specified file
    with open(args.output, 'w') as output_file:
        output_file.write(base32_hash)

    print(f'SHA1 Base32 hash written to {args.output}')

if __name__ == '__main__':
    main()
