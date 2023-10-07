import base64

keys = 'Flag{This_a_Flag}'
flag = "flag{Ju2t_4n_3x4mple_RCa}"
def do_something(enc='', key=''):
    enc += '\0'
    s_box = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s_box[i] + ord(key[i % len(key)])) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    i = j = 0
    res = []
    for s in enc:
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        t = (s_box[i] + s_box[j]) % 256
        k = s_box[t]
        res.append(chr(ord(s) ^ k))

    res_str = ''
    for i in res:
        # print(i, end="")
        res_str += i
    return res_str


res = do_something(flag, keys)
res = base64.b64encode(res.encode()).decode()
print(res)

# res = wq3CocO5wqXDtEotBDA6XsKrw7DDvsOxw54fOjrCpMO/b8OcwrfCgMOi