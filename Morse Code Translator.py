#Morse Code Translator
#Project tentang penerjemah kode Morse sederhana.
#Mulai

#modul yang dibutuhkan
import time

# Kamus kode Morse
morse_code_dict = {}
#Morse code Aplhabet
morse_code_dict['A'] = '.-'
morse_code_dict['B'] = '-...'
morse_code_dict['C'] = '-.-.'
morse_code_dict['D'] = '-..'
morse_code_dict['E'] = '.'
morse_code_dict['F'] = '..-.'
morse_code_dict['G'] = '--.'
morse_code_dict['H'] = '....'
morse_code_dict['I'] = '..'
morse_code_dict['J'] = '.---'
morse_code_dict['K'] = '-.-'
morse_code_dict['L'] = '.-..'
morse_code_dict['M'] = '--'
morse_code_dict['N'] = '-.'
morse_code_dict['O'] = '---'
morse_code_dict['P'] = '.--.'
morse_code_dict['Q'] = '--.-'
morse_code_dict['R'] = '.-.'
morse_code_dict['S'] = '...'
morse_code_dict['T'] = '-'
morse_code_dict['U'] = '..-'
morse_code_dict['V'] = '...-'
morse_code_dict['W'] = '.--'
morse_code_dict['X'] = '-..-'
morse_code_dict['Y'] = '-.--'
morse_code_dict['Z'] = '--..'
#Morse code Numbers
morse_code_dict['1'] = '.----'
morse_code_dict['2'] = '..---'
morse_code_dict['3'] = '...--'
morse_code_dict['4'] = '....-'
morse_code_dict['5'] = '.....'
morse_code_dict['6'] = '-....'
morse_code_dict['7'] = '--...'
morse_code_dict['8'] = '---..'
morse_code_dict['9'] = '----.'
morse_code_dict['0'] = '-----'
morse_code_dict[' '] = '/'

#Judul
print('='*30)
print('🎉 Morse Code Translator 🎉')
print('='*30)
time.sleep(2)

#Memasukkan teks yang ingin diterjemahkan
text_to_translate = input('Masukkan teks yang ingin diterjemahkan ke kode Morse: ').upper()
time.sleep(2)

#Fungsi penerjemah
def translate_to_morse(text):
    morse_translation = ''
    for char in text:
        morse_translation += morse_code_dict.get(char, '') + ' '
    return morse_translation.strip()

#Melakukan penerjemahan
morse_result = translate_to_morse(text_to_translate)
print('Teks dalam kode Morse adalah:')
print(morse_result)
time.sleep(2)

#Selesai
print('Terjemahan selesai!')
print('Terima kasih telah menggunakan Morse Code Translator!')
time.sleep(2)