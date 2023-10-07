- **题目名称：** babyTree
- **题目类型：** Crypto
- **题目难度：**简单
- **出题人：** =w=
- **考点：**

1. Merkle Tree

- **描述：** 十年树木，百年树人
- **flag：** flag{3f2807e9-4c33-4b61-bdc2-e2a8274c0f5a}
- **Writeup：**


将 flag 拆成五段，以每一段为叶子节点构造一棵 Merkle Tree，需要注意最后一层应有 8 个叶子节点，直接复制最后一个叶子来填成满二叉树。最后以层次遍历的方式输出所有节点的哈希值，给出的 hash.txt 是不完整的，但可以根据 Merkle Tree 的性质进行验证

uuid.uuid4() 常在远程题中用于生成 flag，用到的字符只有十六进制数 0-f，生成的结构是 8-4-4-4-12

本题除了第一段未知长度是 6，后面 4 段未知长度都是 4，直接爆破就可以了，注意满足 Merkle Tree 的哈希关系，利用这些关系来判断穷举是否正确

参考资料
https://blog.csdn.net/qq_31391601/article/details/127271302
https://zhuanlan.zhihu.com/p/548327495
https://github.com/LiuBoyu/blockchain


```python
import hashlib
import itertools

def Hash(data):
    first = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return hashlib.sha256(first.encode('utf-8')).hexdigest()

hash1 = 'dc810337294d51be2645a291dce9000e22d2bdbcf03caa0a6ccdba1da075db56'
hash4 = 'a4cbf26dc80d2cb96a9945fc7fa59f368ce68eca7edd0018fcaaa7df6994e212'
hash8 = '6e77cce53a24f7536778d05b660d0c67f84a670cb996fcaff10bf16ad8aa2c5d' 
hash10 = 'e1c9e0704e8ad9338080640c651485b5e9efc2ed27389b45c47994c28901e24e'
hash11 = '52aa0cf17bafb10549c059cfdc7887a64b6b04412c152d3f4483a0db2746fad8'
hash5 = Hash(hash10+hash11)
hash2 = Hash(hash4+hash5)

a1 = '3f{}{}{}{}{}{}'
a2 = '{}{}{}{}'
a3 = '{}{}{}{}274c0f5a'
alphabet = '0123456789abcdef'

for comb in itertools.product(alphabet, repeat=6):
    s = 'flag{'+ a1.format(*comb)
    hash = Hash(s)
    if hash == hash8:
        print("1",comb)
        print(hash)
        break

for comb in itertools.product(alphabet, repeat=4):
    s = a2.format(*comb)
    hash = Hash(s)
    if Hash(hash8+hash) == hash4:
        print("2",comb)
        print(hash)
    if hash == hash10:
        print("3",comb)
        print(hash)
    if hash == hash11:
        print("4",comb)
        print(hash)
    s2 = a3.format(*comb) + '}'
    hash12 = Hash(s2)
    hash6 = Hash(hash12+hash12)
    hash3 = Hash(hash6+hash6)
    if Hash(hash2+hash3) == hash1:
        print("5",comb)
        print(hash12)
```
