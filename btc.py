#!/usr/bin/env python3
import sys
import time 
import urllib
from hashlib import *
from base58 import *
import requests
from secp256k1 import PrivateKey
import secrets
bits = secrets.randbits(256)
# 46518555179467323509970270980993648640987722172281263586388328188640792550961
bits_hex = hex(bits)
bits_hex = bits_hex[2:]
if len(bits_hex) < 64:
    bits_hex = '0'+bits_hex
if len(bits_hex) < 64:
    bits_hex = '0'+bits_hex
# 0x66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
private_key = bits_hex
# 66d891b5ed7f51e5044be6a7ebe4e2eae32b960f5aa0883f7cc0ce4fd6921e31
print("private key :", private_key)
key = private_key
#print(bytearray.fromhex(key))

#print(bytearray.fromhex(key).hex())
#key = '7ccca75d019dbae79ac4266501578684ee64eeb3c9212105f7a3bdc0ddb0f27e'
#pub_compressed = '03e9a06e539d6bf5cf1ca5c41b59121fa3df07a338322405a312c67b6349a707e9'
#pub_uncompressed = '04e9a06e539d6bf5cf1ca5c41b59121fa3df07a338322405a312c67b6349a707e94c181c5fe89306493dd5677143a329065606740ee58b873e01642228a09ecf9d'
privkey = PrivateKey(bytes(bytearray.fromhex(key)))
pubkey_ser = privkey.pubkey.serialize()
pubkey_ser_uncompressed = privkey.pubkey.serialize(compressed=False)
print("public key :", pubkey_ser.hex())
print(pubkey_ser_uncompressed.hex())
#assert pubkey_ser == bytes(bytearray.fromhex(pub_compressed))
#assert pubkey_ser_uncompressed == bytes(bytearray.fromhex(pub_uncompressed))
def SHA256D(bstr):
    return sha256(sha256(bstr).digest()).digest()
def ConvertPKHToAddress(prefix, addr):
    data = prefix + addr
    return b58encode(data + SHA256D(data)[:4])
def PubkeyToAddress(pubkey):
    #pubkey = bytearray.fromhex(pubkey_hex)
    #print(pubkey)
    round1 = sha256(pubkey).digest()
    h = new('ripemd160')
    h.update(round1)
    pubkey_hash = h.digest()
    return ConvertPKHToAddress(b'\x00', pubkey_hash)
#pubkey = "044da006f958beba78ec54443df4a3f52237253f7ae8cbdb17dccf3feaa57f3126da0a0909f11998130c2d0e86a485f4e79ee466a183a476c432c68758ab9e630b"
#pubkey=pubkey_ser
#pubkey= sys.argv[1]
#print(len(pubkey))
#print("Address: %s" % PubkeyToAddress(pubkey_ser_uncompressed))
#addr 1EzwoHtiXB4iFwedPr49iywjZn2nnekhoj
addr = PubkeyToAddress(pubkey_ser_uncompressed)
print("btc addr :",addr)
#url="https://blockchain.info/q/addressbalance/" + bytes.decode(addr)
url="https://www.blockchain.com/btc/address/" + bytes.decode(addr)
print(" :", url)
# res=requests.get(url)
# print(res)
# req = urllib.request.urlopen(url)
# res = req.read().decode('utf-8')
# #print(res)
# req.close()
# if int(res) > 0:
#     filename = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
#     fo = open(filename+str(time.time())+".txt", "w")
#     fo.write(key)
#     fo.write("\n")
#     fo.write(addr.decode())
#     fo.write("\n")
#     fo.write(res)
#     fo.write("\n")
#     fo.close()
#begin=`date +%s`; for ((i=0;i<10;i++));do bx="" seed="" |="" bx="" ec-new="" |="" bx="" ec-to-public="" |="" bx="" ec-to-address="" |="" xargs="" -i@="" ./btc_balance="" -addr="" @=""> /dev/null; done; end=`date +%s` ; echo `echo "scale=2;$end-$begin" | bc`