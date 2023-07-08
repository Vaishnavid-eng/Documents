import re

N, M = 7, 3

matrix = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]

transposed_matrix = list(zip(*matrix))

decoded_script = ''.join(''.join(col) for col in transposed_matrix)

decoded_script = re.sub(r'[^A-Za-z0-9][!,@,#,$,%,&,\s]+(?=[A-Za-z0-9])', ' ', decoded_script)

decoded_script = re.sub('  ', ' ', decoded_script)

print(decoded_script)