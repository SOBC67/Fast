import math
thai_alphabet = [
    'ก', 'ข', 'ค', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ',
    'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท',
    'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม',
    'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห',
    'ฬ', 'อ', 'ฮ'
]


def filterkey(Key):
    thai_vowels = set(["ะ", "า", "ิ", "ี", "ึ", "ื", "ุ", "ู", "เ", "แ", "โ", "ใ", "ไ", "ำ", "ั", "็", "์"])
    thai_tone_marks = set(["่", "้", "๊", "๋"])
    Key = [char for char in Key if char not in thai_vowels and char not in thai_tone_marks]
    return Key

def encrypt_key(Key,value_i):
    Key = filterkey(Key)
    #print(Key)
    alphabet_to_index = {letter: idx + 1 for idx, letter in enumerate(thai_alphabet)}

    replaced_key = [alphabet_to_index[char] for char in Key]

    indexed_values = list(enumerate(replaced_key))

    sorted_indexed_values = sorted(indexed_values, key=lambda x: x[1])

    value_i = value_i.replace(' ','')

    c = 0
    x = 0
    while len(Key)*c < len(value_i):
        c += 1
        x = len(Key)*c - len(value_i)

    value_i += 'ฮ'*x
    value_v = math.floor(len(value_i)/len(Key))

    cutline = []
    for i in range(0, len(value_i),len(Key)):
        cutline.append(value_i[i:i + len(Key)])



    encypt = ''
    index_check = 0
    counting = 1
    sorted_value = [0] * len(replaced_key)
    for index, value in sorted_indexed_values:
        sorted_value[index] = counting
        counting += 1
        for i in range(0,value_v):
            encypt += value_i[(index)+(len(Key)*i)]+''
            index_check += 1
            if index_check%5 == 0:
                encypt += ' '
    #while len(encypt) % 5 != 0:
    #   encypt = encypt +"ฮ"
    
    return Key,math.ceil(len(value_i)/5),replaced_key,sorted_value,encypt,cutline

#print(encrypt_key("กินข้าวกินหรือยัง","กินแล้วกินอีก"))

def decrypt_key(Key,value_i):
    Key = filterkey(Key)

    alphabet_to_index = {letter: idx + 1 for idx, letter in enumerate(thai_alphabet)}

    replaced_key = [alphabet_to_index[char] for char in Key]

    indexed_values = list(enumerate(replaced_key))

    sorted_indexed_values = sorted(indexed_values, key=lambda x: x[1])

    value_i = value_i.replace(' ','')

    c = 0
    x = 0
    while len(Key)*c < len(value_i):
        c += 1
        x = len(Key)*c - len(value_i)


    value_v = math.floor(len(value_i)/len(Key))


    decrypts = list(range((len(value_i))))

    #print(decrypts)
    start = 0
    counting = 1
    sorted_value = [0] * len(replaced_key)
    for index,value in sorted_indexed_values:
        sorted_value[index] = counting
        counting += 1
        for i in range(0,value_v):
            #print((index)+(len(Key)*i))
            decrypts[(index)+(len(Key)*i)] = value_i[start]
            start+=1
    cutline = []
    for i in range(0, len(value_i),len(Key)):
        cutline.append(''.join(decrypts[i:i + len(Key)]))

    return Key,math.ceil(len(value_i)/5),replaced_key,sorted_value,''.join(decrypts),cutline
    #return ''.join(decrypts)