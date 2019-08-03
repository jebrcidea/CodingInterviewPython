def mergeSortedArrays(array1, array2): #O(n+m)
	mergedArray = list()
	index1 = 0
	index2 = 0
	while index1 in range(0, len(array1)): #for every element in array1
		while index2 in range(0,len(array2)): #for every element in array2
			if(index1 != len(array1) and (array1[index1] < array2[index2])): #if i'm not at the end of array1 and it's smaller tha array2
				mergedArray.append(array1[index1]) #ads it to the solution
				index1+=1 #increases his index
				print(mergedArray, index1, index2) #debug
			elif(index2 != len(array2)): #if array2 at the position was bigger and i'm not at the end
				mergedArray.append(array2[index2])
				index2+=1
				print(mergedArray, index1, index2) #debug
		if(index1 < len(array1)): #at the end of array2 if there's still elements aat array1 I add them at the end
				mergedArray.append(array1[index1])
				index1+=1
				print(mergedArray, index1, index2) #debug
	if(index2 != len(array2)): #at the end of array1 if there's still elements aat array2 I add them at the end
		mergedArray.append(array2[index2])
		index2+=1
	return mergedArray