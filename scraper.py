from blockchain.blockexplorer import *

# TXID Scraper
# Requires:
# - TXID: Hash for Bitcoin Transaction
# - depth: Number of steps in chain to traverse and scrape 
class Scraper():

  # Main List of Txs
  txs = []

  # Initialize Scraper
  def __init__(self, txid, depth):
    self.depth = depth
    self.__main__(txid, depth)

  def __main__(self, txid, depth):

    hashes = []
    inputs = []
    
    if(depth == 0): return
    
    # Handles initial Tx Input
    if type(txid) is str:
      inputs = list(map(lambda x: x.address, self.getInputs(txid)))
      for x in inputs:
        hashes.append({'hash': txid, 'inputs': inputs})

    # Handles previos output data
    if type(txid) is list:
      for tx in txid:
        inputs += tx['inputs']
        txHash = tx['hash']
        for x in inputs:
          hashes.append(self.getTxs(x, txHash))
 
    self.txs += hashes
    self.decreaseDepth() # Decreases depth for recursion
    self.__main__(hashes, self.depth) # Repeat process with new data and higher depth

  # Traverse up-chain
  def decreaseDepth(self):
    self.depth = self.depth - 1

  # Low-level input gathering from TX
  def getInputs(self, txid):
    return get_tx(txid).inputs
    
  # Gather data on input and hash
  def getTxs(self, address, txid):
    txs = get_address(address).transactions
    tx = list(filter(lambda x: x.hash != txid, txs))[0]
    return {'hash': tx.hash, 'inputs': list(map(lambda x: x.address, tx.inputs))}
    
  # Final Retrieval for list of Txs
  def getResults(self):
    return self.txs

