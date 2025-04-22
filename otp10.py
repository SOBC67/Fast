# Dictionary สำหรับแมปคำเฉพาะกับรหัส
wordlist = [
    {"บริเวณ": "04"},
    {"ทวน": "23"},
    {"ความถี่": "25"},
    {"พิกัด": "26"},
    {"ย่อ": "27"},
    {"พื้นที่": "62"},
    {"ผ่าน": "72"},
    {"เพื่อ": "74"},
]

# ตารางตัวอักษร/คำที่ใช้สำหรับการเข้ารหัสและถอดรหัส
text_array = [
    [["E", "e"], ["H", "h"], "ฟ", ["6", "๖"], "บริเวณ", "-", ["G", "g"], ["7", "๗"], ["S", "s"], ["B", "b"]],
    ["อ", ["X", "x"], ["P", "p"], ["K", "k"], ["N", "n"], "ื", "ฉ", ["Y", "y"], "เ", ["O", "o"]],
    [["ช", "ณ"], ",", ['ท', 'ธ', 'ฑ', 'ฒ'], "ทวน", "ป", "ความถี่", "พิกัด", "ย่อ", ["L", "l"], ["8", "๘"]],
    [["1", "๑"], ["พ", "ภ"], ["0", "๐"], "ึ", ["A", "a"], ["ด", "ฎ"], "ิ", "ข", ["I", "i"], ["W", "w"]],
    [["M", "m"], "ะ", ["T", "t"], "ฝ", ".", "ี", ["C", "c"], "๊", ["Z", "z"], "ก"],
    ["้", ["น", "ณ"], "ฮ", "ซ", "แ", "/", ["ล", "ฤ"], ["9", "๙"], ["ส", "ศ", "ษ"], ["F", "f"]],
    ["ว", ["J", "j"], "พื้นที่", ["3", "๓"], "๋", ["ค", "ฆ"], " ", "ู", "า", "โ"],
    [["ย", "ญ"], ["R", "r"], "ผ่าน", ["Q", "q"], "เพื่อ", ["V", "v"], ["5", "๕"], "บ", ["U", "u"], ["ไ", "ใ"]],
    ["ห", "่", "ั", ["2", "๒"], ["ถ", "ฐ"], "์", ["ร", "ฦ", "ฬ"], ["D", "d"], "ง", "ม"],
    ["ุ", ["ต", "ฏ"], ["4", "๔"], "จ", "ๆ", "ผ", "ำ", "( - )", "็", "ั้"]
]


def compare_text_with_array(text_array, long_text):
    result_bits = ""

    while len(long_text) >= 0:
        checkfind = 0

        # ตรวจสอบจาก wordlist ก่อน
        for item in wordlist:
            for key, value in item.items():
                if long_text.startswith(key):
                    result_bits += value
                    long_text = long_text[len(key):]

        # ตรวจสอบจาก text_array
        for ta, ka in enumerate(text_array):
            for w, k in enumerate(ka):
                if isinstance(k, list):
                    for kk in k:
                        if long_text.startswith(kk):
                            result_bits += str(ta) + str(w)
                            long_text = long_text[len(kk):]
                            checkfind = 1
                            break
                elif long_text.startswith(k):
                    result_bits += str(ta) + str(w)
                    long_text = long_text[len(k):]
                    checkfind = 1

        if checkfind == 0:
            break

    return result_bits


def reverse_this(text_array, enc):
    enc = enc.replace(' ', '')
    enc_n = [enc[i:i + 2] for i in range(0, len(enc), 2)]
    txt = ''

    for e in enc_n:
        item = text_array[int(e[0])][int(e[1])]
        if isinstance(item, list):
            txt += item[0]
        else:
            txt += item

    return txt


def otp10en(long_text):
    rx = compare_text_with_array(text_array, long_text)

    # ถ้าหาร 4 ไม่ลงตัว ให้เติม '55' ต่อท้ายจนกว่าจะครบ
    while len(rx) % 4 != 0:
        rx += '55'

    return " ".join(rx[i:i + 4] for i in range(0, len(rx), 4))


def otp10de(long_text):
    return reverse_this(text_array, long_text)


# ตัวอย่างการใช้งาน:
# encoded = otp10en('ผ่านแนวพื้นที่')
# print(encoded)
# decoded = otp10de(encoded)
# print(decoded)
