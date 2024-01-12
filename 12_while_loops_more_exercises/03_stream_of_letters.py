import string



count_c = 0
count_n = 0
count_o = 0

result = ''
word2 = ''
while True:
    symbol = input()
    if symbol == 'End':
        break
    else:
        if symbol in string.ascii_letters:
            if count_c >= 1 and count_n >= 1 and count_o >= 1:
                result += " "
                count_o = 0
                count_n = 0
                count_c = 0

            if symbol == 'c':
                count_c += 1
                if count_c > 1:
                    result += symbol
                else:
                    continue

            elif symbol == 'n':
                count_n += 1
                if count_n > 1:
                    result += symbol
                else:
                    continue

            elif symbol == 'o':
                count_o += 1
                if count_o > 1:
                    result += symbol
                else:
                    continue
            else:
                result += symbol

print(result)

