s = input('Retezec: ')

print('')
s = s.lower()
print(s)
print('')



s_arr = s.split()
for i in range(len(s_arr)):
    if i == 0:
        s_arr[i] = s_arr[i].capitalize()
    elif s_arr[i - 1].endswith('.'):
        s_arr[i] = s_arr[i].capitalize()
    
print(' '.join(s_arr))