有个想法最近在写代码，通过随机生成地址，与BTC网络的有余额地址做匹配，匹配上了记录下来，这概率极低 1/2^256....但是如果谁有闲置的服务器和时间，挂着呗，又有什么损失呢，万一猜到了巨鲸 哈哈...
近期我会根据这思路更新出代码，号召全网挂这呗 哈哈。

1. 随机生成私钥->公钥->地址

2. 通过BTC区块的交易地址找出有B的地址

3. 通过bloom filter匹配海量的地址，如果找到保存下私钥和地址



代码依赖：
sys
time 
urllib
hashlib
base58
requests
secrets
secp256k1

https://github.com/bitcoin-core/secp256k1.git