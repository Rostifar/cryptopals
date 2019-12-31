# converts hex to decimal
def c_hex_to_dec(c):
    if ord('/') < c < ord(':'):
        return c
    if ord('a') <= c <= ord('f'):
        return c - 55
    raise Exception("hex character is invalid")


def dec_to_c_hex(c):
    if 0 <= c <= 9:
        return chr(48 + c)
    if 10 <= c <= 15:
        return chr(87 + c)
    raise Exception("cannot convert decimal to hex")


# converts decimal to base64
def dec_to_c_b64(c):
    if 0 <= c <= 25:
        return chr(c + 65)
    if 25 < c <= 51:
        return chr(c + 71)
    if 51 < c <= 61:
        return chr(c - 4)
    if c == 62:
        return chr(43)
    if c == 63:
        return chr(47)
    raise Exception("cannot convert decimal to base64")


def c_b64_to_dec(c):
    if ord('A') <= c <= ord('Z'):
        return c - 65
    if ord('a') <= c <= ord('z'):
        return c - 71
    if ord('0') <= c <= ord('9'):
        return c - 4
    if ord(c) == 43:
        return 62
    if ord(c) == 47:
        return 63
    raise Exception("cannot convert decimal to base64")



def hex_str_to_dec(s):
    return [c_hex_to_dec(c) for c in s]


def b64_str_to_dec(s):
    return [c_b64_to_dec(c) for c in s]


# converts hex to base64
def hex_to_b64(s):
    # convert to raw string
    b = list(s.encode())
    b_len = len(b)

    if b_len == 0:
        return ''

    # add zero padding if hex string has odd length
    hex_padded = False
    if b_len % 2 != 0:
        b.insert(0, 0)
        hex_padded = True

    i, bits_proc, idx = 0, 0, 0
    f_mask = 15
    r_mask = 12

    s = []
    while idx < b_len:
        first = 0 if i == 0 and hex_padded else c_hex_to_dec(b[idx]) & f_mask
        rest = c_hex_to_dec(b[idx + 1]) & r_mask if idx + 1 < b_len else -1

        f_shift = 2 if f_mask == 15 else 4
        tmp = first << f_shift

        if f_shift == 2:
            tmp = tmp + (rest >> 2) if rest != -1 else tmp
        else:
            tmp = tmp + rest if rest != -1 else tmp

        s.append(tmp)

        bits_proc += 6
        i += 1

        if i % 2 == 0:
            idx += 2
            f_mask = 15
            r_mask = 12
        else:
            idx += 1
            f_mask = 3
            r_mask = 15

    r = bits_proc % 24
    r = 0 if r == 0 else 24 - r
    s = ''.join([dec_to_c_b64(c) for c in s])

    while r > 0:
        s += '='
        r -= 6
    return s


# inputs string in hex
def xor(s1, s2):
    b1 = hex_str_to_dec(s1.encode())
    b2 = hex_str_to_dec(s2.encode())

    b3 = []
    for i in range(len(b1)):
        b3.append((b1[i] ^ b2[i]) & 15)
    print(b3)
    return ''.join([dec_to_c_hex(c) for c in b3])

