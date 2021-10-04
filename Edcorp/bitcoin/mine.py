from hashlib import sha256

MAX_NONCE = 100000000000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find! Reached maximum nonce which was set to {MAX_NONCE}")

if __name__ == '__main__':
    transactions = ''' Esson->Frost->Edcorp-50'''
    difficulty = 4
    new_hash = mine(5, transactions, '0000000d408656121119dc9ba376a06414c603104b9e3901e0d32bf12ce4a2dd', 7)
    print(new_hash)
    '''next hash = 0000000ffb0c5f31205bc45d28c17434819a4404c1b60aa8b2e2861e29447616 at nonce 7713613'''
    