#
# Ciera Bomer 
# 04-27-2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Dictionary
codes = {'A':'!', 'B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'K','J':'_',
        'K':'=','L':'+','M':'<','N':'>','O':'?','P':'/','Q':'11','R':'`','S':'`','T':'O',
        'U':'D','V':'L','W':'G','X':'F','Y':'A','Z':'E','a':'I','b':'N','c':'C','d':'q',
        'e':'w','f':'e','g':'r','h':'t','i':'y','j':'u','k':'i','l':'o','m':'p','n':'a',
        'o':'s','p':'d','q':'f','r':'g','s':'h','t':'j','u':'k','v':'l','w':'z','x':'c',
        'y':'x','z':'v'}
def encrypt_file (input_file_name, output_file_name, codes):
    try:
        with open(input_file_name, 'r') as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_name}'not found.")
        return
    encrypted_text = ''
    for char in text:
        if char in codes:
            encrypted_text += codes[char]
        else:
            encrypted_text += char
    try:
        with open(output_file_name, 'w') as outfile:
            outfile.write(encrypted_text)
        print(f"File '{input_file_name}' successfully encrypted to '{output_file_name}'.")
    except Exception as e:
        print (f"Error writing to output file '{output_file_name}':{e}")
def decrypt_file(input_file_name, codes):
    try:
        with open(input_file_name, 'r') as infile:
            encrypted_text = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_name}' not found.")
        return
    reverse_codes = {v: k for k, v in codes.items()}
    decrypted_text = ''
    for char in encrypted_text:
        if char in reverse_codes:
            decrypted_text += reverse_codes[char]
        else:
            decrypted_text += char
    print('Decrypted text: ')
    print(decrypted_text)
def main():
    input_file = 'text.txt'
    encrypted_file = 'encrypted.txt'

    encrypt_file(input_file, encrypted_file, codes)
    decrypt_file(encrypted_file, codes)
main()


