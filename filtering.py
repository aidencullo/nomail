def filter_out_encodings(str):
    return [x for x in str if x[1] != 'utf-8']

def decode(str):
    if isinstance(str, bytes):
        return str.decode()
    return str

def first_five(str):
    return ' '.join(str.split()[:5])

def filter_header(message_array):
    filtered_message_array = filter_out_encodings(message_array)
    message = filtered_message_array[0][0]
    message = decode(message)
    message = message.strip()
    message = first_five(message)
    return message
