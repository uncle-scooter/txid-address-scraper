import unittest
from blockchain.blockexplorer import *

addresses = []

def init(txid):
  inputs = getInputsByHash(txid)
  inputAddresses = list(map(lambda x: x.address, inputs))
  print findTxByAddressAndHash(inputAddresses[0], txid)
  # getOutputAddressByHash(txid, value.address)

def getOutputAddressByHash(txid, address):
    tx = get_tx(txid)
    print tx.outputs[0].address
    print tx.outputs[1].address
    print address

    output = list(filter(lambda output: output.address == address, tx.outputs))
    print output
    # value = reduce(lambda x, y: x.value+y.value, tx.outputs)
    # print value
    # output = list(filter(lambda output: output.value == value, tx.outputs))
    # print output
    # if(len(output) > 0): return output[0]

def findTxByAddressAndHash(address, txid):
  txs = getAddress(address).transactions
  tx = filter(lambda x: x.hash == txid, txs)[0]
  value = reduce(lambda x, y: x.value+y.value, tx.inputs).value
  print value
  
  # if(txs):
  #   print txs[0].hash
  #   print txs[1].hash
  #   # output = list(filter(lambda tx: tx.value == tx, txs))
  #   # if(output): print (output.inputs)
  # else: return [] 

def getInputsByAddress(address):
  txs = getAddress(address).transactions
  if(txs):
    output = list(filter(lambda tx: getOutputAddressByHash(tx.hash, address), txs))[0]
    if(output): return (output.inputs)
  else: return []
       
def getInputsByHash(txid):
    tx = get_tx(txid)
    return tx.inputs
      
def getAddress(address):
  return get_address(address)



    
# getOutputAddressByHash('2f7e8182090f2cfaf0c5c20e609f6fbfb3d84b3e1d504a21c70aa21f0d993fe8', '3076084')
# getInputsByHash('828ef3b079f9c23829c56fe86e85b4a69d9e06e5b54ea597eef5fb3ffef509fe')
# findTxByAddressAndValue('3QwizKRQFgLerbBAwzXsAzgfGorHoBCUWV', '3076084')

init('2f7e8182090f2cfaf0c5c20e609f6fbfb3d84b3e1d504a21c70aa21f0d993fe8')
