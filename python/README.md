#python 

cracker.py is a hash dictionary attack were you get a wordlist attempt to crack the secret hash in secret.txt

cracker.py uses argparse to get the type of hash and hashlib to hash the wordlists.

cracker.py creates a list of the wordlist and hash each word and checks if it matches.

how to use:

    python3 cracker.py --type md5


secret.txt contains the word you want to crack.

wordlists.txt contains the potential words that the secret could be.
