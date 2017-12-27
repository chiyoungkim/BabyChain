import hashlib as hasher
import datetime as date

# Block class

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        hash_val = sha.hexdigest()
        return hash_val

# Create genesis

def create_genesis_block():
    # Manual block with index 0, arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block. Hello world!", "0")

# Create next block

def create_next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Append blocks

def append_n_blocks(n, blockchain, data_string):
    last_block = blockchain[-1]
    for i in range(0,n):
        next_block = create_next_block(last_block)
        blockchain.append(next_block)
        last_block = next_block
        next_block.data = data_string + str(next_block.index)

# Reconciliation

def reconciliation(chain_1, chain_2):
    if len(chain_1) > len(chain_2):
        return chain_1
    elif len(chain_2) > len(chain_1):
        return chain_2
    else:
        if chain_1[-1].timestamp > chain_2[-1].timestamp:
            return chain_2
        else:
            return chain_1

# Output blockchain

def output(blockchain):
    for block in blockchain:
        # print str(block).split(" ")[-1][0:-2]
        print block.data

# Wait

def wait():
    return raw_input('\n')

################################################################################

print "Create Genesis Block"
blockchain = [create_genesis_block()]
last_block = blockchain[0]
standard_string = "Block "

output(blockchain)

wait()

# Append some blocks

print "Append some blocks"
append_n_blocks(10, blockchain, standard_string)
output(blockchain)

wait()

# Show unscrupulous guy hacking blockchain

hackchain = blockchain[0:5]

print "Add more transactions"
append_n_blocks(5, blockchain, standard_string)

wait()

print "Unscrupulous hacker"
append_n_blocks(5, hackchain, "Hacked block ")

wait()

# Show contents of blockchain

print "\"Original\" blockchain"
output(blockchain)

wait()

print "Hacked blockchain"
output(hackchain)

wait()

# Choose longest blockchain to be master blockchain--reconciliation

print "Reconciliation"
new_blockchain = reconciliation(blockchain, hackchain)
output(new_blockchain)
blockchain = new_blockchain[1:]
wait()

# Append

print "Append more transactions"
append_n_blocks(5, blockchain, standard_string)
output(blockchain)
