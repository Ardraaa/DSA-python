def bubble(array,n):
    for i in range(0,n-1):
        if array[i]>array[i+1]:
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
            i+=1
        elif array[i]<array[i+1]:
             i+=1
        else:
            break;
    

n=int(input("Enter array size: "))
array=[]
for j in range(n):
    element=int(input("Enter array elements: "))
    array.append(element)
print("array before sorting: ")
print(array)
bubble(array,n)
print("array after sorting: ")
print(array)
