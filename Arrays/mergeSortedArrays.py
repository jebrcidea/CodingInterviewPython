def mergeSortedArrays(array1, array2):
	mergedArray = list()
	index1 = 0
	index2 = 0
	while index1 in range(0, len(array1)):
		while index2 in range(0,len(array2)):
			if(index1 != len(array1) and (array1[index1] < array2[index2])):
				mergedArray.append(array1[index1])
				index1+=1
				print(mergedArray, index1, index2)
			elif(index2 != len(array2)):
				mergedArray.append(array2[index2])
				index2+=1
				print(mergedArray, index1, index2)
		if(index1 < len(array1)):
				mergedArray.append(array1[index1])
				index1+=1
				print(mergedArray, index1, index2)
	if(index2 != len(array2)):
		mergedArray.append(array2[index2])
		index2+=1
	return mergedArray