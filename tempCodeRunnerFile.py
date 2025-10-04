with open("yourfile.txt", "rb") as file:
    file_bytes_iterator = iter(file.read())
    
    for b in file_bytes_iterator:
        if b == 0:  # null byte check
            break
        # process byte b
    else:
        raise ValueError("String is unterminated")
