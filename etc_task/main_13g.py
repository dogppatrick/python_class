# 讀取資料
sj = ""
item_class = ["Attention", "Activity Level", "Impulsivity", "Adaptation",
              "Moods & Confidence", "Energy & Feelings", "Social Abilities", "Sensitivity & Regulation"]
item_sum = []
item_count = []
item_scale = []
age_class = ["a", "b", "c", "d"]
subject_age_class = ""
c = -1

with open("data_input.dat", "r") as f:
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


subject_age_class = age_class.index(subject_age_class)

with open("scale.txt", "r") as f2:
    rl = f2.readline()
    while rl != "":
        rl = f2.readline()
        for i in range(subject_age_class):
            f2.readline()
        line_spit = rl.split(sep="\t")
        print(line_spit)
        for i in range(4 - subject_age_class):
            f2.readline()



# for i in range(len(item_class)):
#     print("%25s:\t %2d\t %d" % (item_class[i], item_sum[i], item_count[i]))
#
# print(subject_age_class)


