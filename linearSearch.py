'''
linear_search (list, value)

    for each item in list 
        if match item == value 
            return the item's location 
        end if 
    end for 
end
'''





list = [12 ,17 ,28 ,30 ,45 ,60 ]
objectif = 28


for i in range(len(list)):
    if list[i] == objectif : 

        print(i) #location of the value (list[2])
