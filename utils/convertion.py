def hex_str_to_int(str):
    return int(str, 16)

def int_to_hex_str(str):
    pass

def get_word_bytes(word):
    result = []

    if isinstance(word, int):
        for _ in range(4):
            mask = (word >> 8) << 8
            curr_byte = word ^ mask
            word = word >> 8

            result.insert(0, curr_byte)
        
        return result
    
    if isinstance(word, str):
        for char in word:
            result.append(ord(char))
        
        return result