import hw_python.hw6_1_employee as E
emp_data = []
# empn = 0
ec_list = []
with open("data.csv", "r") as f:
    read1 = f.readline()
    while read1 != "":
        tmp = list(read1.split(sep=","))
        tmp[4] = int(tmp[4])
        tmp[6] = int(tmp[6])
        emp_data.append(tuple(tmp))
        read1 = f.readline()
for d in emp_data:
    if d[6] == 0:
        ec_list.append(E.Emp(d[0], d[1], d[2], d[3], d[4]))
    elif d[6] == 1:
        ec_list.append(E.Manager2(d[0], d[1], d[2], d[3], d[4]))
    elif d[6] == 2:
        ec_list.append(E.Ceo(d[0], d[1], d[2], d[3], d[4]))
for i in ec_list:
    print(i, end="\n")
