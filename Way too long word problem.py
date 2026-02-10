n=int(input())
words=[]
for i in range(n):
	words.append(input())
for word in words:
	result=""
	length=len(word)
	if length>10:
		result = word[0] + str(length - 2) + word[-1]
		print(result)
	else:
		print(word)
