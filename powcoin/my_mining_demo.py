import hashlib, time

def get_proof(header, nonce):
    preimage = "{0}:{1}".format(header, nonce).encode()
    proof_hex = hashlib.sha256(preimage).hexdigest()
    return int(proof_hex,16)

def mine(header, target):
    nonce = 0
    while get_proof(header, nonce) >= target:
        nonce += 1 # new guess
    return nonce

def mining_demo(header):
    for difficulty_bits in range(1,30):
        target = 2 ** (256 - difficulty_bits)
        start_time = time.time()
        nonce = mine(header, target)
        proof =  get_proof(header,nonce)
        elapsed_time = time.time() - start_time

        target_str = "{target:.0e}"
        elapsed_time_str = "{elapsed_time:.0e}"
        bin_proof_str = "{proof:0256b}"

        print("bits : {0} target: {1} elapsed:{2} proof:{3}".format(difficulty_bits, target_str, elapsed_time_str, bin_proof_str))

if __name__ == "__main__":
    header = "hello"
    mining_demo(header)
