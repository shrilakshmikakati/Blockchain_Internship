import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mineBlock(self, difficulty):
        target = '0' * difficulty
        attempts = 0
        start_time = time.time()

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()
            attempts += 1

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Block mined! Nonce: {self.nonce}")
        print(f"Hash: {self.hash}")
        print(f"Attempts needed: {attempts}")
        print(f"Time taken: {elapsed:.4f} seconds")

if __name__ == "__main__":
    block = Block(1, time.time(), "Some transaction data", "0")
    difficulty = 4  
    
    print("Mining block...")
    block.mineBlock(difficulty)
