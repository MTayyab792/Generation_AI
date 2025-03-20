ls = ["karachi","Lahore", "Islamabad", "faisalabad", "Multan"]
for i in ls:   
    j=i[0].upper() + i[1:-1].lower() + i[-1].upper()
print(j)
