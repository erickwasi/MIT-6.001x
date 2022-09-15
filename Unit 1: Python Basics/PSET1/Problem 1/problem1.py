vowels = ['a', 'e', 'i', 'o', 'u']
vowel_num = 0

for char in s:
    if char in vowels:
        vowel_num += 1

print("Number of vowels:", vowel_num)
