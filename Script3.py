'''
This script is used to translate the DATA arraies at the top of every gas function. 

This script also accounts for double and single percision values. 

The output of this function goes into the Setup_npy.py file in the PyGasmix module.

Also make sure to change whatever the X value in the strings below to match the ID or name of your gas function.

'''
import sys
k=1
for line in sys.stdin:
	k=1
	line = line.replace('\t','')

	if len(line)== 0:
		continue
	if line[0]=='C':
		line = list(line)
		line[0]= '#'
		print("".join(line))
		continue
	line=line.replace(' ','')
	line = line.replace('\n','')
	if line.endswith('/'):
		k = 0
	if line.find('DATA')!=-1:
		arr = line.split('DATA')[1]
		arrname = arr.split(r'/')[0]
		arrname = arrname.replace(' ','')
		arrname =arrname+'GX = ['  # X value here.
		rest =arr.split(r'/')[1]
		rest = rest.replace('/','')
		rest = rest.replace('\t','')
		rest=rest.replace(' ','')
		arRest = rest.split(',')
		result = arrname
		for num in arRest:
			if num!='':
				if num.find('*')!=-1:
					num1 = int(num.split('*')[0])
					for i in range(num1):
						arRest.append(num.split('*')[1])
				elif num.find('D')!=-1:
					num = num.replace('D','e')+','
					result = result +num
				else:
					num = 'np.float32('+num+'),'
					result = result +num
		print(result)
	else:
		line=line.replace('/','')
		line = line.replace('\t','')
		line=line.replace(' ','')
		arRest = line.split(',')
		result = ''
		for num in arRest:
			if num!='':
				if num.find('*')!=-1:
					num1 = int(num.split('*')[0])
					for i in range(num1):
						arRest.append(num.split('*')[1])
				elif num.find('D')!=-1:
					num = num.replace('D','e')+','
					result = result +num
				else:
					num = 'np.float32('+num+'),'
					result = result +num
			
		print(result)
	if k==0:
		print(']')

