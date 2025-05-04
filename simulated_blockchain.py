import time
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize the blockchain
        self.current_data = []  # Initialize the list of data (transactions or readings)
        self.create_new_block(proof=100, previous_hash='1')  # Create the genesis block (first block)

    def create_new_block(self, proof, previous_hash=None):
        """
        Creates a new block and adds it to the chain.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': self.current_data,  # The sensor data
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else None
        }
        self.current_data = []  # Clear the current data list after adding to the block
        self.chain.append(block)
        return block

    def add_data(self, corrosion_level, temperature, pressure, maintenance_required):
        """
        Adds new sensor data to the current data.
        """
        self.current_data.append({
            'corrosion_level': corrosion_level,
            'temperature': temperature,
            'pressure': pressure,
            'maintenance_required': maintenance_required,
        })
        print("Data added to blockchain:", self.current_data)  # Print the current data (for debugging)

    def print_blockchain(self):
        """
        Prints the entire blockchain.
        """
        print("\nCurrent Blockchain:")
        for block in self.chain:
            print(f"Block {block['index']}:")
            print(f"  Data: {block['data']}")
            print(f"  Timestamp: {block['timestamp']}")
            print(f"  Proof: {block['proof']}")
            print(f"  Previous Hash: {block['previous_hash']}")
            print("----")

    def hash(self, block):
        """
        Hashes a block to create the block's hash.
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
