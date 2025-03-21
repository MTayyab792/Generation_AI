ls = ["karachi","Lahore", "Islamabad", "faisalabad", "Multan"]
c=[]
for i in ls:   
    c.insert(0,i)
    print(c)
    j=i[0].upper() + i[1:-1].lower() + i[-1].upper()
print(j)
