import numpy as np
import hashlib
from scipy.ndimage.interpolation import shift

x = hashlib.sha256(('abc').encode('utf-8')).hexdigest()
print(x)

# print('Please write the text to be hashed below:')
# text = input()
text = 'abc'

asciiText = []
for i in text:
	ascii_i = (ord(i))
	asciiText.append(ascii_i)
# print(asciiText)

biText = ''
for i in asciiText:
	biText += (str(bin(i)[2:].zfill(8)))
# print(biText)

end64 = len(biText)
end64 = str(bin(end64)[2:].zfill(8))
while(len(end64) < 64):
	end64 = '0' + end64
# print(end64)

biText += '1'
if(len(biText) < 448):
	while(len(biText) < 448):
		biText += '0'
elif(len(biText > 448)):
	print('figure out how to do this')
	pass

biText += end64
# print(biText)

text = []
for i in range(0, 16):
	text.append(biText[i*32:i*32 + 32])
# print(text)

def BiStr_BiArray32(BiString):
	BiArray = []
	for i in range(0, 32):
		BiArray.append(int(BiString[i]))
	return BiArray

def BiArray_BiStr32(BiArray):
	BiString = ''
	for i in range(0, 32):
		BiString += str(BiArray[i])
	return BiString

for i in range(16, 64):
	num0 = BiStr_BiArray32(text[i - 15])
	num1 = BiStr_BiArray32(text[i - 2])

	w0, w1 = int(text[i - 16], 2), int(text[i - 7], 2)

	s0 = np.roll(num0, 7) ^ np.roll(num0, 18) ^ shift(num0, 3, cval = 0)
	# s0 = num0>>7 ^ num0>>18 ^ shift(num0, 3, cval = 0)
	s1 = np.roll(num1, 17) ^ np.roll(num1, 19) ^ shift(num1, 10, cval = 0)

	s00, s11 = BiArray_BiStr32(s0), BiArray_BiStr32(s1)

	s0, s1 = int(s00, 2), int(s11, 2)
	newWord = w0 + s0 + w1 + s1
	if(newWord >= 2**32):
		newWord = newWord%(2**32)
	text.append(str(bin(newWord)[2:].zfill(32))) # text array of binary strings
# print(text)

h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
	0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
	0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
	0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
	0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
	0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
	0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
	0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

hs = [int(h0), int(h1), int(h2), int(h3), int(h4), int(h5), int(h6), int(h7)] # integer array of h constants
hss = []
for i in range(0, 8):
	hss.append(str(bin(hs[i])[2:].zfill(32))) # binary string of h constants

ks = []
for i in range(0, 64):
	ks.append(str(bin(k[i])[2:].zfill(32))) # array of binary strings for k constants

a = hss[0] # set = to h0-h7 in binary string
b = hss[1]
c = hss[2]
d = hss[3]
e = hss[4]
f = hss[5]
g = hss[6]
h = hss[7]

for i in range(0, 64):
	a0, b0, c0, e0, f0, g0 = BiStr_BiArray32(a), BiStr_BiArray32(b), BiStr_BiArray32(c), BiStr_BiArray32(e), BiStr_BiArray32(f), BiStr_BiArray32(g),
		
	S0 = (np.roll(a0, 2)) ^ np.roll(a0, 13)
	S0 = S0 ^ np.roll(a0, 22)
	
	S1 = np.roll(e0, 6) ^ np.roll(e0, 11)
	S1 = S1 ^ np.roll(e0, 25)
	# Something is wrong in the line 122 as the inputs are correct but the output is not
	# ch should = 00111010011011111110011001100111 for i = 0
	ch = (int(e, 2) & int(f, 2)) ^ ((~int(e, 2)) & int(g, 2))
	ch = str(bin(ch)[2:].zfill(32))

	maj = (int(a, 2) & int(b, 2)) ^ (int(a, 2) & int(c, 2))
	maj = maj ^ (int(b, 2) & int(c, 2))
	maj = bin(maj)[2:].zfill(32)

	S11, S00, k0 = BiArray_BiStr32(S0), BiArray_BiStr32(S0), ks[i]
	# print(h, S11, ch, k0, text[i])

	S11, ch, S00, maj, h, k0, w0 = int(S11, 2), int(ch, 2), int(S00, 2), int(maj, 2), int(h, 2), int(k0, 2), int(text[i], 2)

	temp1 = h0 + S11 + ch + k0 + w0

	if(temp1 >= 2**32):
		temp1 = temp1%(2**32)
	temp2 = S00 + maj
	if(temp2 >= 2**32):
		temp2 = temp2%(2**32)

	# print(bin(temp1)[2:].zfill(32), bin(temp2)[2:].zfill(32))
	
	e = int(d, 2) + temp1
	if(e >= 2**32):
		e = e%(2**32)
	e = str(bin(e)[2:].zfill(32))

	h = g
	g = f
	f = e
	d = c
	c = b
	b = a

	a = temp1 + temp2
	if(a >= 2**32):
		a = a%(2**32)
	a = str(bin(a)[2:].zfill(32))

a, b, c, d, e, f, g, h = int(a, 2), int(b, 2), int(c, 2), int(d, 2), int(e, 2), int(f, 2), int(g, 2), int(h, 2)

# print(a, b, c, d, e, f, g, h)
# a0, b0, c0, d0, e0, f0, g0, h0 = int(a0, 2), int(b0, 2), int(c0, 2), int(d0, 2), int(e0, 2), int(f0, 2), int(g0, 2), int(h0, 2)

h0 = hs[0] + a
if(h0 >= 2**32):
	h0 = h0%(2**32)

h1 = hs[1] + b
if(h1 >= 2**32):
	h1 = h1%(2**32)

h2 = hs[2] + c
if(h2 >= 2**32):
	h2 = h2%(2**32)

h3 = hs[3] + d
if(h3 >= 2**32):
	h3 = h3%(2**32)

h4 = hs[4] + e
if(h4 >= 2**32):
	h4 = h4%(2**32)

h5 = hs[5] + f
if(h5 >= 2**32):
	h5 = h5%(2**32)

h6 = hs[6] + g
if(h6 >= 2**32):
	h6 = h6%(2**32)

h7 = hs[7] + h
if(h7 >= 2**32):
	h7 = h7%(2**32)

h0, h1, h2, h3, h4, h5, h6, h7 = hex(h0)[2:], hex(h1)[2:], hex(h2)[2:], hex(h3)[2:], hex(h4)[2:], hex(h5)[2:], hex(h6)[2:], hex(h7)[2:]

print(h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7)




