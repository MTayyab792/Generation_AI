# ls = ["karachi","Lahore", "Islamabad", "faisalabad", "Multan"]
# for i in ls:   
#     j=i[0].upper() + i[1:-1].lower() + i[-1].upper()
#     print(j)
    
    
# ls = ["karachi","Lahore", "Islamabad", "faisalabad", "Multan"]
# for i in ls:   
#     j=i[0].upper() + i[1:-1].lower() + i[-1].upper()
#     print(j)

    
# for x in range(2,21,2):
#     print(x)

# ls = [x for x in range(2,10,2)]
# print(ls)

# ls = ["karachi", "jarwalan", "Faisalabad", "kivi","test"]
# ls2=[x for x in ls if "i" in x]

# for x in ls:
#     if "a" in x:
#         ls2.append(x)
# print(ls2)

ls = ["karachi", "jarwalan", "Faisalabad", "kivi","test"]
# ls2 = [x[0].upper() +x[1:]for x in ls]
# print(ls2)
# ls2 = [x.capitalize() for x in ls]
# print(ls2)

ls2 = [x[0].upper()+x[1:-1].lower()+x[-1:].upper() for x in ls]
print(ls2)






