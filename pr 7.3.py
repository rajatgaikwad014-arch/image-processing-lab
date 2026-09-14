def lzw_compress(uncompressed):
    """Compress a list of integers using LZW."""
    # Build the dictionary.
    dict_size = 256
    dictionary = {bytes([i]): i for i in range(dict_size)}
    w = b""
    compressed = []

    for k in uncompressed:
        c = bytes([k])
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    if w:
        compressed.append(dictionary[w])
    return compressed
def lzw_decompress(compressed):
    """Decompress LZW output."""
    dict_size = 256
    dictionary = {i: bytes([i]) for i in range(dict_size)}

    w = bytes([compressed.pop(0)])
    result = bytearray(w)

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[:1]
        else:
            raise ValueError("Bad compressed k: %s" % k)
        result += entry

        dictionary[dict_size] = w + entry[:1]
        dict_size += 1
        w = entry
    return list(result)
