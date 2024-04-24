

#find the max of given list without using in bulit max function.

 #example:[5,3,76,34,13,54]
#output : mux number is 76

list_a =[0,8,76,34,13,54]
max_num = list_a[0]
for i in range(1,len(list_a)):
    if(list_a[i]>max_num):
        max_num=list_a[i]
        
print(max_num)
