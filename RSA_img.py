# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:35:04 2019

@author: Himaja
"""

from PIL import Image
import random
import numpy as np
import math
import matplotlib.pyplot as plt


from skimage import color, io
img = color.rgb2gray(io.imread('Jenna.jpg'))

data = (img*255).astype(np.uint8)

imgplot = plt.imshow(data)
### Img size = 899, 1174
img_1D = data.ravel()   # converting to 1D

########### RSA Algorithm

### GCD Function
def gcd(a, h):
    while(1):
        temp = a%h
        if(temp == 0):
            return h;
        a = h
        h = temp
    

################# Prime Numbers Big enough
p = 37          ### as high as possible 
q = 23
n = p*q
totient = (p-1)*(q-1)
e = random.randrange(1, totient)  


#Use Euclid's Algorithm to verify that e and phi(n) are comprime
g = gcd(e, totient)
while g != 1:
    e = random.randrange(1, totient)
    g = gcd(e, totient)

### Finding D Value  
def multiplicative_inverse(e, phi):
    d = None
    i = 1
    exit = False
    while not exit:
        temp1 = phi*i +1
        d = float(temp1/e)
        d_int = int(d)
        i += 1
        if(d_int == d):
            exit=True
    return int(d)
       
d = multiplicative_inverse(e, totient)

#### Now we have p,q,n,totient,e,g,d


#### Encryption
# for i in range(0, len(msg_ascii)): then use as msg_ascii[i]
encrypted_list = []
for i in range(0, len(img_1D)):
    current_enc = (int(img_1D[i]) ** d) % n
    encrypted_list.append(int(current_enc))
   
### Displaying encrypted image 
enc_img = np.array(encrypted_list).reshape(img.shape[0], img.shape[1])
imgplot = plt.imshow(enc_img)


### Displaying encrypted msg
enc_chars = []
for num in encrypted_list:
    enc_chars.append(chr(num))

encrypted_msg = ''.join(map(lambda x: str(x), enc_chars))

print(encrypted_msg)


####### Decryption
dec_list = []
for i in range(0, len(encrypted_list)):
    current_dec = (encrypted_list[i] ** e) % n
    dec_list.append(current_dec)

### conerting decrypted msg to characters
chars = []
for num in dec_list:
    chars.append(chr(num))


decrypted_msg = ''.join(map(lambda x: str(x), chars))

#### Back to Image 

recovered_img = np.array(dec_list).reshape(img.shape[0], img.shape[1])

imgplot = plt.imshow(recovered_img)
