#!/usr/bin/python3
import hashlib
import sys
import base64
import binascii
import argparse


def hashathon(source, output, print_all=False):
    md4_result = hashlib.new('md4').hexdigest()
    md5_result = hashlib.md5(source).hexdigest()
    sha1_result = hashlib.sha1(source).hexdigest()
    sha224_result = hashlib.sha224(source).hexdigest()
    sha256_result = hashlib.sha256(source).hexdigest()
    sha384_result = hashlib.sha384(source).hexdigest()
    sha512_result = hashlib.sha512(source).hexdigest()

    results_map = {'md4': md4_result, 'md5': md5_result,
                   'sha1': sha1_result, 'sha224': sha224_result,
                   'sha256': sha256_result, 'sha384': sha384_result,
                   'sha512': sha512_result}

    key_list = list(results_map.keys())
    key_list.sort()
    for item in key_list:
        if print_all:
            print(item + ': ' + results_map[item])
        if output in results_map[item]:
            print('found match in ' + item + '!')
            print(results_map[item])


def hexify(output, encoding):
    if encoding == 'b64':
        bytestring = base64.b64decode(output)
        unicode_string = str(binascii.hexlify(bytestring), 'utf-8')
        return unicode_string
    elif encoding == 'hex':
        return output

    return None


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--print_all', help='print results of all hashes.', action='store_true')
    parser.add_argument('key', help='the key to be hashed, probably a username.')
    parser.add_argument('hash', help='the result of hashing the key.')
    parser.add_argument('encoding', help='the encoding of the hash. either b64 or hex.')
    return parser.parse_args()


def main():
    parsed_args = parse_args()

    key = parsed_args.key
    hashed = parsed_args.hash
    encoding = parsed_args.encoding

    hexified = hexify(hashed, encoding)
    if not hexified:
        print('encoding not recognized. acceptable options include: b64, hex')
        quit()
    print('as hex: ' + hexified)
    hashathon(str.encode(key), hexified, parsed_args.print_all)


if __name__ == '__main__':
    main()
