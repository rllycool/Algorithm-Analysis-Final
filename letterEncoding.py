#choose five letter word, encode and decode it.
w = 'bagel'

#encode the word
encodeW = ''
for letter in w:
    encodeW += chr(ord(letter) + 1)

print('Encoded word:', encodeW)

#now decode the word
decoded_word = ''
for letter in encodeW:
    decoded_word += chr(ord(letter) - 1)

# Print the decoded word
print('Decoded word:', decoded_word)