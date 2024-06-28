def bin_to_dec(binary_string):
    decimal_value = 0
    for i, bit in enumerate(reversed(binary_string)):
        if bit == '1':
            decimal_value += 2 ** i
    return decimal_value

def dec_to_bin(number):
    if number == 0:
        return '0'
    
    binary_string = ''
    while number > 0:
        binary_string = str(number % 2) + binary_string
        number //= 2
    
    return binary_string

def telephone_cipher(message):
    encoder_dict = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'
    }
    
    result = ''
    for char in message.upper():
        if char.isalpha():
            if len(result) > 0 and result[-1] == encoder_dict[char][0]:
                result += '_'
            result += encoder_dict[char]
    return result

def telephone_decipher(telephone_string):
    decipher_dict = {
        "0": " ", '2': 'A', '22': 'B', '222': 'C',
        '3': 'D', '33': 'E', '333': 'F', '4': 'G',
        '44': 'H', '444': 'I', '5': 'J', '55': 'K',
        '555': 'L', '6': 'M', '66': 'N', '666': 'O',
        '7': 'P', '77': 'Q', '777': 'R', '7777': 'S',
        '8': 'T', '88': 'U', '888': 'V', '9': 'W',
        '99': 'X', '999': 'Y', '9999': 'Z'
    }
    result = ''
    current_digit = ''
    for char in telephone_string:
        if char.isdigit():
            if current_digit and current_digit[0] != char:
                result += decipher_dict.get(current_digit, '')
                current_digit = char
            else:
                current_digit += char
        else:  # For non-digit characters (like spaces)
            if current_digit:
                result += decipher_dict.get(current_digit, '')
                current_digit = ''
            if char == '0':
                result += ' '
    if current_digit:
        result += decipher_dict.get(current_digit, '')
    return result
    
