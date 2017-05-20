def binarysearch(dataset,num):
	sorted(dataset)
	first=0
	last=len(dataset)-1

	while True:
		pivot=(first+last)//2
		if dataset[pivot]==num:
			break
		elif dataset[pivot]>num:
			last=pivot-1
		elif dataset[pivot]<num:
			first=pivot+1
	print(num,"is at postion",pivot,"in the dataset")




x=binarysearch([1,3,5,7,9,1,13,15,17,19],17)
