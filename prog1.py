import hashlib
import time

# Block class to represent each block in the blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.nonce = nonce

# Blockchain class to represent the entire blockchain
class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.difficulty = difficulty  # Difficulty level (number of leading zeros)
        self.create_genesis_block()

    def create_genesis_block(self):
        """Create the first block in the blockchain, known as the genesis block."""
        genesis_block = Block(0, "0", int(time.time()), "Genesis Block", "", 0)
        genesis_block.hash = self.mine_block(genesis_block)
        self.chain.append(genesis_block)

    def calculate_hash(self, index, previous_hash, timestamp, data, nonce):
        """Calculate SHA-256 hash of the block's content, including the nonce."""
        block_string = f"{index}{previous_hash}{timestamp}{data}{nonce}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    def mine_block(self, block):
        """Mine a block by finding the correct nonce that satisfies the difficulty (leading zeros)."""
        nonce = 0
        while True:
            block_hash = self.calculate_hash(block.index, block.previous_hash, block.timestamp, block.data, nonce)
            if block_hash.startswith('0' * self.difficulty):
                return block_hash, nonce
            nonce += 1

    def add_block(self, data):
        """Add a new block to the blockchain."""
        last_block = self.chain[-1]
        index = last_block.index + 1
        timestamp = int(time.time())
        previous_hash = last_block.hash
        new_block = Block(index, previous_hash, timestamp, data, "", 0)
        new_block.hash, new_block.nonce = self.mine_block(new_block)
        self.chain.append(new_block)

    def display_chain(self):
        """Display the blockchain."""
        for block in self.chain:
            print(f"Block #{block.index} - Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print(f"Data: {block.data}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Previous Hash: {block.previous_hash}")
            print('-' * 50)

# Example usage
if __name__ == "__main__":
    # Create a new blockchain with a difficulty level of 2
    blockchain = Blockchain(difficulty=4)
    n=int(input("Enter the no of blocks: "))
    for i in range(n):
        data=input("enter the data: ")
        blockchain.add_block(data)

    # Add some blocks to the blockchain
    #blockchain.add_block("First Block Data")
    #blockchain.add_block("Second Block Data")
    #blockchain.add_block("Third Block Data")

    # Display the blockchain
    blockchain.display_chain()
``
