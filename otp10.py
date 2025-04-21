def compare_text_with_array(text_array, long_text):
    result_bits = ""
    while len(long_text) >= 0:
        checkfind = 0
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

# ตัวอย่างการใช้งาน
#text_array = [['สวัสดี', 'ลาก่อน'], ['รัก', 'คุณ']]


'''
text_array = [["E","H", "ฟ", "๖", "บริเวณ", "-", "G", "๗", "S", "B"],
["อ","X", "P", "K", "N", "ื", "ฉ", "Y", "เ", "O"],
["ชณ",",","ทธฑฒ","ทวน", "ป", "ความถี่", "พิกัด", "ย่อ", "L", "๘"],
["๑","พภ","0","ึ", "A", "ดฎ", "ิ", "ข", "I", "W"],
["M","ะ","T","ฝ", ".", "ี", "C", "๊", "Z", "ก"],
["้","นณ","ฮ","ซ", "แ", "/", "ลฤ", "๙", "สศษ", "F"],
["ว","J","พื้นที่","๓", "๋", "คฆ", "วรรค", "ู", "า", "โ"],
["ยญ","R","ผ่าน","Q", "เพื่อ", "V", "๕", "บ", "U", "ไ"],
["ห","่","ั","๒", "ถฐ", "์", "รฦฬ", "D", "ง", "ม"],
["ุ","ตฏ","๔","จ", "ๆ", "ผ", "ำ", "( - )", "็", "ั้"]]
'''

text_array = [["E","H", "ฟ", "๖", "บริเวณ", "-", "G", "๗", "S", "B"],
["อ","X", "P", "K", "N", "ื", "ฉ", "Y", "เ", "O"],
[["ช","ณ"],",",['ท','ธ','ฑ','ฒ'],"ทวน", "ป", "ความถี่", "พิกัด", "ย่อ", "L", "๘"],
["๑",["พ","ภ"],"0","ึ", "A", ["ด","ฎ"], "ิ", "ข", "I", "W"],
["M","ะ","T","ฝ", ".", "ี", "C", "๊", "Z", "ก"],
["้",["น","ณ"],"ฮ","ซ", "แ", "/", ["ล","ฤ"], "๙", ["ส","ศ","ษ"], "F"],
["ว","J","พื้นที่","๓", "๋", ["ค","ฆ"], " ", "ู", "า", "โ"],
[["ย","ญ"],"R","ผ่าน","Q", "เพื่อ", "V", "๕", "บ", "U", ["ไ","ใ"]],
["ห","่","ั","๒", ["ถ","ฐ"], "์", ["ร","ฦ","ฬ"], "D", "ง", "ม"],
["ุ",["ต","ฏ"],"๔","จ", "ๆ", "ผ", "ำ", "( - )", "็", "ั้"]]

def otp10en(long_text):
    rx = compare_text_with_array(text_array, long_text)
    return " ".join(rx[i:i+4] for i in range(0, len(rx), 4))
#print(otp10('พื้นที่ที่มึงจะต้องกินข้าววรรคสัศใช่ไหม'))