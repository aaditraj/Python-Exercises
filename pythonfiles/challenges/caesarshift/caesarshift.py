alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesarshift(word, shift):
    blankword = ''
    for i in word:
        index = alphabet.find(i)
        if index + shift >= len(alphabet):
            blankword += alphabet[index+shift-len(alphabet)]
        elif index + shift < 0:
            blankword += alphabet[index+shift+26]
        else:
            blankword += alphabet[index+shift]
    return blankword

print(caesarshift('zap', 5))
print(caesarshift('blah', 2))
print(caesarshift('abc', -30))
