from blockchain.blockexplorer import *

wallets = []
depth = 4

class Scraper():

  txs = []

  def __init__(self, txid, depth):
    self.getInputs(txid)
    self.txs.append({'addresses': self.addresses, 'hash': txid})
    self.__main__(txid, depth)

  def __main__(self, txid, depth):
    
    print self.txs

    if(depth == 0): return

    self.depth = depth - 1
    self.getInputs(txid)

    for x in self.inputs:
      self.getTxs(x.address, txid)
    
    self.__main__(self.hash, self.depth)

  def getInputs(self, txid):
    self.inputs = get_tx(txid).inputs
    self.addresses = list(map(lambda x: x.address, self.inputs))

  def getTxs(self, address, txid):
    txs = get_address(address).transactions
    tx = filter(lambda x: x.hash != txid, txs)[0]
    self.hash = tx.hash
    self.tx = list(map(lambda x: x.address, tx.inputs))
    self.txs.append({'addresses': self.tx, 'mainAddress': address, 'hash': tx.hash})
    
s = Scraper('2f7e8182090f2cfaf0c5c20e609f6fbfb3d84b3e1d504a21c70aa21f0d993fe8', 4)