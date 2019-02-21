# 讀取資料
sj = ""
item_class = ["Attention", "Activity Level", "Impulsivity", "Adaptation",
              "Moods & Confidence", "Energy & Feelings", "Social Abilities", "Sensitivity & Regulation"]
item_sum = []
item_count = []
item_scale = []
age_class = ["a", "b", "c", "d"]
c = -1
q = 0
with open("input.txt", "r") as f:
    rl = f.read(1)
    subject_age_class = rl
    rl = f.readline()
    while rl != "":
        rl = f.readline()
        if rl == "\n":
            item_sum.append(int(0))
            item_count.append(int(0))
            c = c + 1
        else:
            if rl != "":
                item_sum[c] = item_sum[c] + int(rl)
                item_count[c] = item_count[c] + 1
# read data and count total score
sc = age_class.index(subject_age_class)

with open("scale.txt", "r") as f2:
    scale_data = f2.read()
    data_sp = scale_data.split(sep="\n")
    for i in range(len(data_sp)):
        if i % 5 == sc+1:
            item_scale.append(int(data_sp[i].split(sep="\t")[item_sum[q]-item_count[q]]))
            q = q + 1

print("\t\t\t\t\t", subject_age_class.upper())
for i in range(len(item_class)):
    print("%d\t%25s:\t %2d\t %d" % (i, item_class[i], item_sum[i], item_scale[i]))

with open("output.txt", "w") as f3:
    f3.write("\t\t\t\t\t" + subject_age_class.upper()+"\n")
    for i in range(len(item_class)):
        f3.write("%d\t%25s:\t %2d\t %d\n" % (i, item_class[i], item_sum[i], item_scale[i]))
