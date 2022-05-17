print('')
a = True
b = True
c = False
d = False
print('---nilai a= ',a,' ; ---nilai b= ',b)
print('---nilai c= ',c,'; ---nilai d= ',d)
print('')
#print('')
e = not a 
print('not a= ',e)
e = not d 
print('not d= ',e)
print('')
e = a and b
print('a and b =',e)
print('1x1')
e = a and d
print('a and d =',e)
print('1x0')
e = c and d
print('c and d =',e)
print('0x0')
print('')
e = a or b
print('a or b =',e)
print('1+1')
e = a or d
print('a or d =',e)
print('1+0')
e = c or d
print('c or d =',e)
print('0+0')
print('')
e = a ^ b
print('a xor b =',e)
e = a ^ d
print('a xor d =',e)
e = c ^ d
print('c xor d =',e)
print('true apabila 1 berjumlah ganjil(1,0;1,1,1)')
print('jika ada 1 sebanyak 2 buah / kelipatannya maka akan mati(1,1;0,0;1,1,0)')
