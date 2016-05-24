
'''pig_latin

'''



word = input("what word do you want to translate?")
vowels = ['a','e','i','o','u','y']
char_index = 0
while char_index != len(word):
	for i in vowels:
		if word[char_index] != i:
			char_index += 1
		elif word[char_index] == i:
			chop = word + word[:char_index]
			word = chop[char_index:]
		else:
			print ("No word")
	
new_word = word +'ay'

print (new_world)
