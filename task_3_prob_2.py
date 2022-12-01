from tokenize import Double


n=int(input("number of students : "))
students=[]
for i in range(n):
    name=str(input("the name of student :"))
    degree=Double(input("its degree"))
    students[i].append([name,degree])
second_lowest_degree=[]
lowest=students[0][1]
second_lowest=0
for i in range(n):
    if students[i][1] > lowest and second_lowest==0 :
        second_lowest=students[i][1]
    if second_lowest!=0 and students[i][1]==second_lowest:
        name.append(students[i][1])
for name in second_lowest_degree :
    print(name)
    print (second_lowest_degree[name])
