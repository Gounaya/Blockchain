import hashlib #for encryption
import json #to format out blockx
import time


class Blockchain(object):

    def __init__(self, arg):
        self.chain = [] #chain that we'll add blocks to / my block-chain
        self.pending_transactions = [] #transaction before before the approve will be here.
        self.new_block(previous_hash="The Times 03/Jan/2009.", proof=100) #to add each block to the chain


    #Create a new block Json object with informations, after that we reset the pending list and add the block to the chain.
    def new_block(self, proof, previous_hash=None):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof, #
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    # To get the last element add in the chain 
    @property
    def last_block(self):

        return self.chain[-1]
