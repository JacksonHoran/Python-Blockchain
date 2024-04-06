import hashlib
class single_block:
    def __init__(self, transaction):
        self.transaction = transaction
        self.hash = hashlib.sha256(transaction.encode('utf-8')).hexdigest()
        self.previous_hash = 0


class blockchain:
    def __init__(self):
        self.chain = []

    def create_new_block(self, transaction):
        block = single_block(transaction)
        if len(self.chain) > 0:
            block.previous_hash = self.chain[-1].hash
        self.chain.append(block)

    def print_blockchain(self):
        for block in self.chain:
            print(' Transaction: ', block.transaction)
            print(' Hash: ', block.hash)
            print(' Previous Hash: ', block.previous_hash)
            print('')
        

Blockchain = blockchain()
Blockchain.create_new_block('Zaine pays Jackson $10')
Blockchain.create_new_block('Jackson pays Jayne $20')
Blockchain.create_new_block('Jayne pays Jackson $10')
Blockchain.create_new_block('Jackson pays Zaine $10')
Blockchain.create_new_block('Jayne pays Jackson $10')
Blockchain.print_blockchain()