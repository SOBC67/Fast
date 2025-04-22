def compare_text_with_array(text_array, long_text):
    result_bits = ""
    while len(long_text) >= 0:
        checkfind = 0
        for item in wordlist:
            for key, value in item.items():
                if long_text.find(key) == 0:
                    result_bits += value
                    long_text = long_text[len(key):]

        for ta,ka in enumerate(text_array):
            for w,k in enumerate(ka):
                if isinstance(k, list):
                    if len(k) > 1:
                        #print(k)
                        for ww,kk in enumerate(k):
                            if long_text.find(kk) == 0:
                                result_bits += str(ta)+str(w)
                                #print(ta,end='')
                                #print(w,end='')
                                #print(kk)
                                long_text = long_text[len(kk):]
                                checkfind = 1
                elif long_text.find(k) == 0:
                    result_bits += str(ta)+str(w)
                    #print(ta,end='')
                    #print(w,end='')
                    #print(k)
                    long_text = long_text[len(k):]
                    checkfind = 1
        if checkfind == 0:
            break
    return result_bits


def reverse_this(text_array,enc):
    enc = enc.replace(' ','')
    enc_n = (" ".join(enc[i:i+2] for i in range(0, len(enc), 2))).split(' ')
    txt = ''
    for e in enc_n:
        #print(e)
        #print(,end='')
        xs = ''
        x = text_array[int(e[0])][int(e[1])]
        if isinstance(x,list):
            txt += x[0]
        else:
            txt += x
    return txt
# ตัวอย่างการใช้งาน
#text_array = [['สวัสดี', 'ลาก่อน'], ['รัก', 'คุณ']]

wordlist = [{"บริเวณ":"04"},{"ทวน":"23"},{"ความถี่":"25"},{"พิกัด":"26"},{"ย่อ":"27"},{"พื้นที่":"62"},{"ผ่าน":"72"},{"เพื่อ":"74"}]

text_array = [["E","H", "ฟ", ["6","๖"], "บริเวณ", "-", "G", ["7","๗"], "S", "B"],
["อ","X", "P", "K", "N", "ื", "ฉ", "Y", "เ", "O"],
[["ช","ณ"],",",['ท','ธ','ฑ','ฒ'],"ทวน", "ป", "ความถี่", "พิกัด", "ย่อ", "L", ["8","๘"]],
[["1","๑"],["พ","ภ"],["0","๐"],"ึ", "A", ["ด","ฎ"], "ิ", "ข", "I", "W"],
["M","ะ","T","ฝ", ".", "ี", "C", "๊", "Z", "ก"],
["้",["น","ณ"],"ฮ","ซ", "แ", "/", ["ล","ฤ"], ["9","๙"], ["ส","ศ","ษ"], "F"],
["ว","J","พื้นที่",["3","๓"], "๋", ["ค","ฆ"], " ", "ู", "า", "โ"],
[["ย","ญ"],"R","ผ่าน","Q", "เพื่อ", "V", ["5","๕"], "บ", "U", ["ไ","ใ"]],
["ห","่","ั",["2","๒"], ["ถ","ฐ"], "์", ["ร","ฦ","ฬ"], "D", "ง", "ม"],
["ุ",["ต","ฏ"],["4","๔"],"จ", "ๆ", "ผ", "ำ", "( - )", "็", "ั้"]]

#print(reverse_this(text_array,"7980 5058 5182 7758 5190 5166 5824 4476 6679 8050 4982 7766 3156 4486 4476 6622 8251 2245 1889 1581 1058 8281 88"))
def otp10de(long_text):
    return reverse_this(text_array,long_text)
def otp10en(long_text):
    rx = compare_text_with_array(text_array, long_text)
    return " ".join(rx[i:i+4] for i in range(0, len(rx), 4))
#print(otp10en('ผ่านแนวพื้นที่'))
#print(otp10de(otp10en('ผ่านแนวพื้นที่')))