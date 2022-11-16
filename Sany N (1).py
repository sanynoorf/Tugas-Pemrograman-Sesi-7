#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("=====Program untuk membalik sebuah kalimat=====")
kalimat = str(input("Masukan Kalimat :"))
balik = ""

for i in range(len(kalimat)-1,-1,-1):
    balik +=kalimat[i]
print("Kalimat sebelum di balik yaitu :", kalimat)
print("Kalimat setelah dibalik adalah :", balik)
print("====================Selesai====================")


# In[1]:


print("=====Program menghitung jumlah masing-masing huruf vokal=====")

teks = "Universitas Nusa Putera"
huruf_vokal = {'a':0, 'i':0, 'u':0, 'e':0, 'o':0}
total = 0
for vokal in teks.lower():
    if vokal in ['a', 'i', 'u', 'e','o']:
        huruf_vokal [vokal] +=1
        total +=1
print(f"Kalimatnya yaitu : {teks}")
print(f"Jumlah Huruf A = {huruf_vokal['a']}")
print(f"Jumlah Huruf I = {huruf_vokal['i']}")
print(f"Jumlah Huruf U = {huruf_vokal['u']}")
print(f"Jumlah Huruf E = {huruf_vokal['e']}")
print(f"Jumlah Huruf O = {huruf_vokal['o']}")
print(f"Total jumlah huruf vokal = {total}")
print("===========================Selesai===========================\n")

