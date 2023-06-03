# coding: utf-8
import random
import os

flag = b"ctf4b{xxx___censored___xxx}"

# Please remove here if you wanna test this code in your environment :)
flag = os.getenv("FLAG").encode()

cipher = [23726, 9235, 36110, 44535, 48845, 21924, 57624, 44534, 46242, 46247, 57606, 51567, 44129, 37647, 38046, 22503, 46225, 50641, 4396, 25293, 50639, 23115, 26272, 20488, 38845, 39632, 42461, 47995, 48845, 40419, 24368, 46225, 18513, 27579, 40007, 28933, 47525, 38055, 38044, 22503, 21625, 23718, 22819, 37257, 36109, 38451, 46240, 43687, 60050, 36121, 22210, 20758, 40830, 51091, 57607, 4397, 57623, 23718, 46233, 25006, 46680, 51534, 21636, 59054, 48413, 40012, 47525, 47998, 36120]
for i in range(len(flag)-1):
    c = ((flag[i] + flag[i+1]) ** 2 + i)
    cipher.append(c)

random.shuffle(cipher)

print(f"cipher = {cipher}")
