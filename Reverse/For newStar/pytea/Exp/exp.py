from ctypes import *
def string_to_int_array(text):
    int_array = []
    for char in text:
        int_value = ord(char)
        int_array.extend([(int_value >> 24) & 0xFF, (int_value >> 16) & 0xFF, (int_value >> 8) & 0xFF, int_value & 0xFF])
    return int_array

def int_array_to_string(int_array):
    text = ''.join([chr((int_array[i] << 24) | (int_array[i + 1] << 16) | (int_array[i + 2] << 8) | int_array[i + 3]) for i in range(0, len(int_array), 4)])
    return text

def string_key_to_int_array(key):
    key_int_array = []
    for char in key:
        key_int_array.append(ord(char))
    return key_int_array

def encrypt(v, k):
    a, b, c, d = c_uint32(v[0]), c_uint32(v[1]),c_uint32(v[2]), c_uint32(v[3])
    delta = 0x9e3779b9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]
    sum = c_uint32(0)
    for i in range(32):
        sum.value = sum.value + delta
        a.value += (((b.value << 4) + k0) ^ (b.value + sum.value) ^ ((b.value >> 5) + k1))
        b.value += ((a.value << 4) + k2) ^ (a.value + sum.value) ^ ((a.value >> 5) + k3)
        c.value += (((d.value << 4) + k0) ^ (d.value + sum.value) ^ ((d.value >> 5) + k1))
        d.value += ((c.value << 4) + k2) ^ (c.value + sum.value) ^ ((c.value >> 5) + k3)
    v[0] = a.value
    v[1] = b.value
    v[2] = c.value
    v[3] = d.value
    return v 


def decrypt(v, k):
    a, b, c, d = c_uint32(v[0]), c_uint32(v[1]), c_uint32(v[2]), c_uint32(v[3])
    delta = 0x9e3779b9
    k0, k1, k2, k3 = k[0], k[1], k[2], k[3]

    total = c_uint32(delta * 32)
    for i in range(32):
        b.value -= ((a.value << 4) + k2) ^ (a.value + total.value) ^ ((a.value >> 5) + k3)
        a.value -= ((b.value << 4) + k0) ^ (b.value + total.value) ^ ((b.value >> 5) + k1)
        d.value -= ((c.value << 4) + k2) ^ (c.value + total.value) ^ ((c.value >> 5) + k3)
        c.value -= ((d.value << 4) + k0) ^ (d.value + total.value) ^ ((d.value >> 5) + k1)
        total.value -= delta
    v[0] = a.value
    v[1] = b.value
    v[2] = c.value
    v[3] = d.value
    return v

if __name__ == "__main__":
    int_array = [4290104173, 498681769, 2467793253, 1446958341, 4290104173, 498681769, 3506676220, 3930177928, 4290104173, 498681769, 2119578006, 1735799975, 4290104173, 498681769, 998166288, 1533730069, 4290104173, 498681769, 4038291621, 2403882153, 4290104173, 498681769, 2467793253, 1446958341, 4290104173, 498681769, 3883478681, 1516481470, 4290104173, 498681769, 4038291621, 2403882153, 4290104173, 498681769, 3028035458, 2248133075, 4290104173, 498681769, 1256740478, 3840002295, 4290104173, 498681769, 3506676220, 3930177928, 4290104173, 498681769, 1565438833, 2700198155, 4290104173, 498681769, 3270843981, 1371444109, 4290104173, 498681769, 4038291621, 2403882153, 4290104173, 498681769, 4265779772, 2371730556, 4290104173, 498681769, 2663769111, 401575738, 4290104173, 498681769, 998166288, 1533730069, 4290104173, 498681769, 3506676220, 3930177928, 4290104173, 498681769, 1259602668, 877012692, 4290104173, 498681769, 1565438833, 2700198155, 4290104173, 498681769, 4038291621, 2403882153, 4290104173, 498681769, 2467793253, 1446958341, 4290104173, 498681769, 2999503208, 285984659, 4290104173, 498681769, 4120542045, 3307257413]
    key_str = "Sloth"
    key = string_key_to_int_array(key_str)

    grouped_elements = [int_array[i:i + 4] for i in range(0, len(int_array), 4)]

    for i in range(len(grouped_elements)):
        group = grouped_elements[i]
        processed_group = decrypt(group, key)
        grouped_elements[i] = processed_group

    decrypted_data = [val for group in grouped_elements for val in group]
    decrypted_text = int_array_to_string(decrypted_data)
    print(f"XSCTF{{{decrypted_text}}}")


