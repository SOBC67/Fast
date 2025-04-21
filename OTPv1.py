import random
import math
array_ascii = [
    "009", "010", "032", "033", "034", "035", "036", "037", "038", "039",
    "040", "041", "042", "043", "044", "045", "046", "047", "048", "049",
    "050", "051", "052", "053", "054", "055", "056", "057", "058", "059",
    "060", "061", "062", "063", "064", "065", "066", "067", "068", "069",
    "070", "071", "072", "073", "074", "075", "076", "077", "078", "079",
    "080", "081", "082", "083", "084", "085", "086", "087", "088", "089",
    "090", "091", "092", "093", "094", "095", "096", "097", "098", "099",
    "100", "101", "102", "103", "104", "105", "106", "107", "108", "109",
    "110", "111", "112", "113", "114", "115", "116", "117", "118", "119",
    "120", "121", "122", "123", "124", "125", "126", "128", "160", "161",
    "162", "163", "164", "165", "166", "167", "168", "169", "170", "171",
    "172", "173", "174", "175", "176", "177", "178", "179", "180", "181",
    "182", "183", "184", "185", "186", "187", "188", "189", "190", "191",
    "192", "193", "194", "195", "196", "197", "198", "199", "200", "201",
    "202", "203", "204", "205", "206", "207", "208", "209", "210", "211",
    "212", "213", "214", "215", "216", "217", "224", "225", "226", "227",
    "228", "229", "230", "231", "232", "233", "234", "235", "236", "237",
    "240", "241", "242", "243", "244", "245", "246", "247", "248", "249"
]

Size = 400  # Set the desired size
input_str = "0123456789"  # Replace with your actual input string
#size = 400
def generate_key():
    builder = []
    for j in range(0,Size):
        ch = random.choice(input_str)
        builder.append(ch)
    return ''.join(builder)
def generate_chr():
    for l in range(len(array_ascii)):
        m = random.randint(l, len(array_ascii) - 1)
        array_ascii[m], array_ascii[l] = array_ascii[l], array_ascii[m]  # Swap elements
    return ''.join(array_ascii)
def encrypt_chr(inputx,chrx):
    len_input = len(inputx)
    encrypt_otp = []
    for i in inputx:
        int_x = int(ord(i))
        string_x = ''
        if int_x > 200 : string_x = str(int_x - 3424)
        elif int_x < 10 : string_x = '00'+str(int_x)
        elif int_x < 100 : string_x = '0'+str(int_x)
        else: string_x = str(int_x)
        array_index = chrx.index(string_x)

        row_x = math.floor(array_index/10)
        column_x  =  array_index%10
        total_x = str("0"+str(row_x))if row_x < 10 else str(row_x)
        total_x = total_x+''+str(column_x)
        #print(total_x)
        encrypt_otp.append(total_x)
    return encrypt_otp
def encrypt_key(inputx,enc_chr,keyx):
    len_x_2 = len(inputx)*2
    get_key = keyx[:len_x_2]
    get_key_2 = [keyx[i:i+2] for i in range(0, len(get_key), 2)]
    code_enc = ''
    for i in range(0,len(enc_chr)):
        if int(enc_chr[i]) > int(get_key_2[i]) :
            code_enc += f"{(int(get_key_2[i])+180) - int(enc_chr[i]):003}"
        else:
            code_enc += f"{int(get_key_2[i]) - int(enc_chr[i]):003}"
    return code_enc
def decrypt_key(intputx,keyx):
    len_x_2 = int((len(intputx)/3)*2)
    get_key = keyx[:len_x_2]
    get_key_2 = [keyx[i:i+2] for i in range(0, len(get_key), 2)]
    input_set = [intputx[i:i+3] for i in range(0, len(intputx), 3)]
    code_enc = []
    for i in range(0,len(input_set)):
        if int(input_set[i]) > int(get_key_2[i]) :
            code_enc.append(f"{(int(get_key_2[i])+180) - int(input_set[i]):003}")
        else:
            code_enc.append(f"{int(get_key_2[i]) - int(input_set[i]):003}")
    #print(code_enc)
    return code_enc
def covert_ascii(x):
    asCii = int(x)
    if asCii >= 161:
            asCii += 3424
    font_styles = {
        10: "<LF>",
        13: "<CR>",
        32: "Space",
        38: "&",
        160: "Null",
        150: "–",
        9: "tab"
    }
    if asCii in font_styles:
        return font_styles[asCii]
    else:
        return chr(int(asCii))
def show_table_otp(chrx):
    x = 0
    for i in chrx:
       # print(covert_ascii(i),end='\t')
        #test
        writetxt_text(covert_ascii(i)+' ')
        x = x+1
        #print() if x%10 == 0 else print('',end='')
        writetxt_text('\n') if x%10 == 0 else print('',end='')
def getChrformChrX(chr_input,chrx):
    index_set = int(chr_input)*3
    return covert_ascii(chrx[index_set:index_set+3])
def writetxt_text(x):
    with open("output.txt", "a", encoding="utf-8") as file:
        file.write(x)
def interface_en(inputx,chrx,keyx):
    enc_chr = encrypt_chr(inputx,[chrx[i:i+3] for i in range(0, len(chrx), 3)])
    enc_total = encrypt_key(inputx,enc_chr,keyx)
    return " ".join(enc_total[i:i+6] for i in range(0, len(enc_total), 6))
    #return " ".join(enc_total[i:i+4] for i in range(0, len(enc_total), 4))
def interface_de(inputx,chrx,keyx):
    inputx = inputx.replace(' ','')
    x = decrypt_key(inputx,keyx)
    result_decrypt = ''
    for i in x:
        result_decrypt += getChrformChrX(i,chrx)
    return result_decrypt.replace("Space",' ')
def interface_get_char_table(chrx):
    chrx_c = [chrx[i:i+3] for i in range(0, len(chrx), 3)]
    return_variable = []
    for i in chrx_c:
        #print(covert_ascii(i))
        return_variable.append(covert_ascii(i))
    return return_variable
def interface_get_key_table(keyx):
    return_variable = []
    c = 0
    textx = ''
    for i in keyx:
        c += 1
        textx += str(i)
        if c%4 == 0:
            return_variable.append(textx)
            textx =''
    return return_variable    
#fortest
def setup():
    chrx = '069046072174249195070094179105043124122210209193059118063035170183041119116190098205092057242102050169047171246198100224061060048207086040107240228042075191213232049103096089037033093077192097217032055206163114082056200034106185039244226161112109203164165167058088236173229184052243188078053176108085123051248241182076233081071121201045245225168235062101214181237074091177038084197115234208120095194196044126087104204212172189110113079202067036065178111187180066009230227247160128199216125215186099090175073054166162010083064068117211231080'
    inputx = 'ประเภทที่2 รักษาพยาบาลและส่งกลับทางสายแพทย์'
    enc_chr = encrypt_chr(inputx,[chrx[i:i+3] for i in range(0, len(chrx), 3)])
    show_table_otp([chrx[i:i+3] for i in range(0, len(chrx), 3)])
    #print(enc_chr)
    key_chr = '0457155166322896743560482670678545111820730466449708907934627590451710270326602229352736924338912073362897087759416179777278980024724440144407837466625994660649692712996782307587071489323520809242355484505732066273767048662276216399491337050917252418252547177340805698538463362135670363260791164067405674640514996728081398394209288931535585974342059763130833274597304158867642352088021656371069421111'
    enc_total = encrypt_key(inputx,enc_chr,key_chr)
    print(" ".join(enc_total[i:i+4] for i in range(0, len(enc_total), 4)))

    x = decrypt_key(enc_total,key_chr)
    for i in x:
        getChrformChrX(i,chrx)

