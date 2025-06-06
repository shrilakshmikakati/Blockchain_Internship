import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.mine_block()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty=4):
        prefix_str = '0' * difficulty
        while True:
            self.hash = self.compute_hash()
            if self.hash.startswith(prefix_str):
                break
            else:
                self.nonce += 1
        return self.hash

    def __str__(self):
        return (f"Block {self.index}:\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n"
                f"Nonce: {self.nonce}\n")

def create_blockchain():
    blockchain = []

    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    blockchain.append(genesis_block)

    block1 = Block(1, time.time(), "Block 1 Data", blockchain[-1].hash)
    blockchain.append(block1)

    block2 = Block(2, time.time(), "Block 2 Data", blockchain[-1].hash)
    blockchain.append(block2)

    return blockchain

def display_blockchain(blockchain):
    for block in blockchain:
        print(block)

def validate_blockchain(blockchain):
    for i in range(1, len(blockchain)):
        if blockchain[i].previous_hash != blockchain[i - 1].hash:
            return False
    return True

if __name__ == "__main__":
    blockchain = create_blockchain()
    print("Blockchain:")
    display_blockchain(blockchain)
