import random

# --- ฟังก์ชันสุ่มตำแหน่ง text_array และ wordlist ---
def shuffle_textarray_and_wordlist(text_array, wordlist):
    all_indexes = [f"{i:02}" for i in range(100)]
    reserved_code = "55"
    
    flat_text_items = []
    for i, row in enumerate(text_array):
        for j, item in enumerate(row):
            flat_text_items.append(((i, j), item))

    # --- แยก / ออกมาก่อนเพื่อให้ได้ code 55 ---
    slash_item = None
    rest_text_items = []
    for coords, item in flat_text_items:
        if item == "/":
            slash_item = (coords, item)
        else:
            rest_text_items.append((coords, item))

    if not slash_item:
        raise ValueError("ไม่พบเครื่องหมาย '/' ใน text_array")

    # --- เตรียม Map โดยล็อก "/" ที่ code 55 ---
    new_text_map = {reserved_code: slash_item[1]}

    # เอารหัสที่เหลือหลังจากจอง 55
    available_indexes = [i for i in all_indexes if i != reserved_code]
    random.shuffle(available_indexes)

    # --- Map ตัวอื่นใน text_array ---
    for idx, (coords, item) in zip(available_indexes, rest_text_items):
        new_text_map[idx] = item

    # --- จัดการ wordlist ---
    word_indexes = available_indexes[len(rest_text_items):len(rest_text_items) + len(wordlist)]
    new_wordlist_map = {}
    for idx, word in zip(word_indexes, wordlist):
        key = list(word.keys())[0]
        new_wordlist_map[key] = idx

    return new_text_map, new_wordlist_map


# --- ฟังก์ชันเข้ารหัส ---
def compare_text_with_map(text_map, word_map, long_text):
    result_bits = ""

    while len(long_text) > 0:
        matched = False

        # ตรวจจาก word_map
        for word, code in word_map.items():
            if long_text.startswith(word):
                result_bits += code
                long_text = long_text[len(word):]
                matched = True
                break
        if matched:
            continue

        # ตรวจจาก text_map
        for code, item in text_map.items():
            if isinstance(item, list):
                for variant in item:
                    if long_text.startswith(variant):
                        result_bits += code
                        long_text = long_text[len(variant):]
                        matched = True
                        break
            else:
                if long_text.startswith(item):
                    result_bits += code
                    long_text = long_text[len(item):]
                    matched = True
                    break

        if not matched:
            break

    return result_bits

def otp10en(text_map, word_map, long_text):
    rx = compare_text_with_map(text_map, word_map, long_text)
    while len(rx) % 4 != 0:
        rx += '55'  # เติม padding

    return " ".join(rx[i:i + 4] for i in range(0, len(rx), 4))

# --- ฟังก์ชันถอดรหัส ---
def reverse_with_map(text_map, word_map, enc):
    enc = enc.replace(' ', '')
    enc_n = [enc[i:i + 2] for i in range(0, len(enc), 2)]
    txt = ""

    inverse_text = {k: v for k, v in text_map.items()}
    inverse_word = {v: k for k, v in word_map.items()}

    for e in enc_n:
        if e in inverse_word:
            txt += inverse_word[e]
        elif e in inverse_text:
            item = inverse_text[e]
            if isinstance(item, list):
                txt += item[0]
            else:
                txt += item
        else:
            pass  # ถ้าไม่เจอ รหัสนี้อาจเป็น padding '55'

    return txt

def otp10de(text_map, word_map, enc):
    return reverse_with_map(text_map, word_map, enc)

# --- ข้อมูลตั้งต้น ---
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

# --- สลับตำแหน่งไม่ให้ซ้ำกัน ---
new_text_map, new_wordlist_map = shuffle_textarray_and_wordlist(text_array, wordlist)

def get_current_text_map():
    return new_text_map

# --- ตัวอย่างการใช้งาน ---
message = "ผ่านแนวพื้นที่"
encoded = otp10en(new_text_map, new_wordlist_map, message)
decoded = otp10de(new_text_map, new_wordlist_map, encoded)
print("New text array",new_text_map)
print("New Worlist",new_wordlist_map)
print("ข้อความต้นฉบับ:", message)
print("เข้ารหัสแล้ว:", encoded)
print("ถอดรหัสกลับ:", decoded)
