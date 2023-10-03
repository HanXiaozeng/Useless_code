import uuid
print('UUID生成器' + 'Version:1.1.3 20230923 191055')
a = 0
b = 0
b = int(b)
a = input('请问你想生成多少uuid?')
a = int(a)
while True:
	b = b + 1
	myuuid = uuid.uuid4()
	print(str(myuuid))
	if b == a:
		break
input('')
