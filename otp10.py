thai_keyboard_array = [
    ['/', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙', '๐', '-'],
    ['ๆ', 'X', 'P', 'K', 'N', '-', 'อึ', 'Y', '-', 'L (โอ)', 'อ', 'ฝ'],
    ['+', ',', 'ทรทบ', 'ทวน', 'ป', 'ความถี่', 'ผิด', 'ฆ', 'ญ', 'ฎ', 'ฐ', 'ฑ'],
    ['ภ', 'พ', '(', 'ศ (ศูย์)', 'ฤ', 'A', 'ฎ', 'ฏ', 'ฐ', 'ข', 'ฃ', 'ฑ'],
    ['(', 'ษ', 'T', 'ฝ', '.', '(', '(', 'C', '(', 'Z', 'ก', 'M'],
    ['ณ', 'ญ', 'ฐ', 'ฑ', '-', '/', 'ฦ', '(', '(', 'ส', 'F', '('],
    ['ฒ', 'J', 'พื้นที่', 'ฒ', '(', '(', '(', '(', '(', '(', '(', 'ว'],
    ['?', 'R', 'ผ่าน', 'Q', 'เพื่อ', '(', 'V', '(', 'U', '(', '(', 'หย'],
    ['(', '(', '(', '(', '(', '(', '(', 'D', '(', '(', 'ม', 'ห'],
    ['(', '(', '(', 'จ', '(', 'ผ', '(', 'G', '(', '(', 'S', 'B'],
    ['(', 'H', '(', '(', 'บริเวณ', '(', '(', '(', '(', '(', '(', '(']
]

def compare_word(word, keyboard_array):
    """
    เปรียบเทียบตัวอักษรในคำกับอาร์เรย์แป้นพิมพ์

    Args:
        word (str): คำที่ต้องการเปรียบเทียบ
        keyboard_array (list): อาร์เรย์แทนแป้นพิมพ์

    Returns:
        dict: ผลการเปรียบเทียบ โดยมีคีย์เป็นตัวอักษรในคำ
              และค่าเป็น True หากพบตัวอักษรในอาร์เรย์แป้นพิมพ์, False หากไม่พบ
    """
    comparison_result = {}
    for char in word:
        found = False
        for row in keyboard_array:
            if char in row:
                found = True
                break
        comparison_result[char] = found
    return comparison_result

# ตัวอย่างการใช้งาน
word_to_compare = "สวัสดี"
comparison = compare_word(word_to_compare, thai_keyboard_array)
print(f"ผลการเปรียบเทียบคำว่า '{word_to_compare}': {comparison}")

word_to_compare_2 = "abc"
comparison_2 = compare_word(word_to_compare_2, thai_keyboard_array)
print(f"ผลการเปรียบเทียบคำว่า '{word_to_compare_2}': {comparison_2}")