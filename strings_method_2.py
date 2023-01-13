k='krishna pooja'
print(k.count('o'))
print(k.count('v'))#0
print(k.find('h'))#4
print(k.rfind('v'))#-1
k='krishna pooja'
print(k.replace('pooja','vamshi')) #krishna vamshi
print(k.replace('o','u',2))#krishna puuja
print(k.replace('o','u',3))#krishna puuja
k='     krishna pooja  .      '
print(k.strip()) #krishna pooja  .
k='  krishna pooja  '.strip()
print(k)#krishna pooja
k='  krishna pooja  '
print(k.lstrip()) #krishna pooja
print(k.rstrip())#   krishna pooja
k='krishna pooja'
v='$'.join(k)
print(v)#k$r$i$s$h$n$a$ $p$o$o$j$a
k='pooja'
l='$'.join(k)
print(l)#p$o$o$j$a
k='krishna pooja'
print(k.removeprefix('k'))#rishna pooja
print(k.removesuffix('a'))#krishna pooj
print(k.removeprefix('kri'))#shna pooja
print(k.removesuffix('ja'))#krishna poo
a='krishna pooja'
print(a.isalnum()) #False bcz space is not allowed in isalnum
b='krishnapooja'
print(b.isalnum())#True
a='python12'
print(a.isalnum())#True
p='pooja.12'
print(p.isalnum())#False bcz special character not allowed
k='krishna pooja'
print(k.isalpha())#False
a=' '
print(a.isalpha())#False
a='akhila'
print(a.isascii())#True
a=chr(0)
print(a.isspace())#False
b=chr(32)
print(b.isspace())#True
print(chr(75))#K
print(chr(90))#Z
print(ord('Z'))#90
print(ord('a'))#97
print(chr(48))#0
print(chr(57))#9
print(ord('0')) #48 
print(ord(' '))#32
print(ord('!'))#33





