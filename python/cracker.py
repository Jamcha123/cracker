import argparse
import hashlib
import base64

def choices(hash:str, types: str): #what hash type you chose
    match(types):
        case "sha256" | "SHA256":
            return hashlib.sha256(hash).hexdigest() 
        case "sha512" | "SHA512":
            return hashlib.sha512(hash).hexdigest()
        case "sha384" | "SHA384":
            return hashlib.sha384(hash).hexdigest()
        case "sha1" | "SHA1":
            return hashlib.sha1(hash).hexdigest()
        case "md5" | "MD5":
            return hashlib.md5(hash).hexdigest()
        case _:
            return ValueError("not a vaild hash")

def cracker(hash: str, plain: str, types: str): #hash is the hash you want to crack, type is the hash type like sha256
    plain = str(plain).encode("utf-8") #wordlist words need to be encoded
    if hash == choices(plain, types):
        return True
    return False

def main(filename: str, hash: str, type: str):
    f1, f2 = open(filename, "r"), open(hash, "r")
    
    wordlist = str(f1.read()).split("\n") # wordlist splits the wordlists.txt seperates every word after the newline
    hashes = str(f2.read()) #hashes gets the hash from the hash.txt
    if len(hashes.split("\n")) > 1 or len(hashes.split(" ")) > 1:
        return ValueError("can't have more than one hash in hash.txt file")
    f1.close()
    f2.close() 

    for x in wordlist:
        target = cracker(hashes, x, type)
        if target == True:
            return hashes + " is " + x
    return "couldn't crack hash, maybe try another hash type"

parser = argparse.ArgumentParser(prog="hash cracker", description="hash cracker is like hashcat you enter a type and it can crack it")
parser.add_argument("-t", "--type") # enter a type like md5 or sha256

args = parser.parse_args()
print(main("wordlists.txt", "secret.txt", args.type)) #wordlists.txt and hash.txt is already entered, just enter the type