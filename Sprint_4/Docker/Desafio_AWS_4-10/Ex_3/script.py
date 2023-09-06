import hashlib

string = input("Digite a sua string: ")

while(string != "quit"):
    sha1_hash = hashlib.sha1(string.encode())
    print(f'HASH da String: {sha1_hash.hexdigest()}')

    string = input("Digite a sua string: ")