import unittest
from blockchain.blockexplorer import *

addresses = []

def scrapeHash(txid):
  inputs = []
  getOutputAddressesByHash(txid)
  for inp in getInputsByHash(txid):
    addresses.append(inp.address)
    inputs += getInputsByAddress(inp.address)
  scrapeInputs(inputs)

def scrapeInputs(inputs):
  res = []
  if(len(inputs) > 0 ):
    print(len(inputs))
    for inp in inputs:
      try: res += getInputsByAddress(inp.address, inp.value)
      except: pass
    scrapeInputs(res)
  print('final'+ str(len(inputs)))

def getOutputAddressesByHash(txid, address):
    tx = get_tx(txid)
    output = list(filter(lambda output: output.address == address, tx.outputs))
    if(len(output) > 0): return output[0]

def findOutput(address, output):
  print 1
    
def getInputsByAddress(address):
  txs = getAddress(address).transactions
  if(txs):
    inputs = []
    output = list(filter(lambda tx: getOutputAddressesByHash(tx.hash, address), txs))[0]
    if(output): print (output.hash)

      # for output in tx.outputs:
      #   if output.address == address:
      #     inputs += tx.inputs
    return inputs
  else:
    return []
       
def getInputsByHash(txid):
    tx = get_tx(txid)
    return tx.inputs
      
def getAddress(address):
  return get_address(address)

    
# getOutputAddressesByHash('828ef3b079f9c23829c56fe86e85b4a69d9e06e5b54ea597eef5fb3ffef509fe')
# getInputsByHash('828ef3b079f9c23829c56fe86e85b4a69d9e06e5b54ea597eef5fb3ffef509fe')

getInputsByAddress('1ByLSV2gLRcuqUmfdYcpPQH8Npm8cccsFg')

