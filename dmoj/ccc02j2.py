while True:
    text_to_convert = input()
    if text_to_convert == 'quit!':
        break
    if len(text_to_convert) > 4 and text_to_convert[-2:] == 'or':
        if text_to_convert[-3] != 'a' and text_to_convert[-3] != 'e' and text_to_convert[-3] != 'i' and text_to_convert[-3] != 'o' and text_to_convert[-3] != 'u' and text_to_convert[-3] != 'y':
            text_to_convert = text_to_convert[:-2]
            text_to_convert+='our'
        else:
            pass
    else:
        pass
    print(text_to_convert)