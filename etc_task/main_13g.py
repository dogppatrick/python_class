# 讀取資料
sj = ""
item_class = ["Attention", "Activity Level", "Impulsivity", "Adaptation",
              "Moods & Confidence", "Energy & Feelings", "Social Abilities", "Sensitivity & Regulation"]
item_class_des = ["注意力", "活動量", "衝動性", "適應性", "情緒與自信", "活力與情感表達", "社交性", "感覺敏感與思考調節"]
age_class_des = ["2歲~2歲11個月", "3歲~3歲11個月", "4歲~6歲11個月", "7歲~20歲11個月"]
item_sum = []
item_count = []
item_scale = []
age_class = ["a", "b", "c", "d"]
c = -1
q = 0
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
sc = age_class.index(subject_age_class)

with open("scale.txt", "r") as f2:
    scale_data = f2.read()
    data_sp = scale_data.split(sep="\n")
    for i in range(len(data_sp)):
        if i % 5 == sc+1:
            item_scale.append(int(data_sp[i].split(sep="\t")[item_sum[q]-item_count[q]]))
            q = q + 1

cognitive_social_total = item_scale[0] + item_scale[1] + item_scale[2] + item_scale[6]
emotions_regulation = sum(item_scale) - cognitive_social_total
sum_scale_raw = []
sum_item_count = []
sum_scale = []
sum_scale_raw.append(cognitive_social_total)
sum_scale_raw.append(emotions_regulation)
sum_item_count.append(item_count[0] + item_count[1] + item_count[2] + item_count[6])
sum_item_count.append(sum(item_count)-sum_item_count[0])
q = 0
with open("scale_total.txt", "r") as f4:
    scale_data = f4.read()
    data_sp = scale_data.split(sep="\n")
    for i in range(len(data_sp)):
        if i % 5 == sc+1:
            sum_scale.append(int(data_sp[i].split(sep="\t")[sum_scale_raw[q]-sum_item_count[q]]))
            q = q + 1

# print("\t\t\t\t\t", subject_age_class.upper())
# for i in range(len(item_class)):
#     print("%d\t%25s:\t %2d\t %d" % (i, item_class[i], item_sum[i], item_scale[i]))
print(item_class_des)
print(item_sum)
print(item_scale)
for i in range(len(item_scale)):
    print("%-15s:%2d%2d" % (item_class_des[i], item_sum[i], item_scale[i]))
with open("output.txt", "w", encoding="utf-8") as f3:
    f3.write("年齡 class:" + age_class_des[sc] + "\tclass:" + subject_age_class.upper() + "\n")
    for i in range(len(item_class)):
        # f3.write("%20s:%2d\t%2d\n" % (item_class_des[i], item_sum[i], item_scale[i]))
        f3.write("%-16s" % (item_class_des[i]))
        for j in range(9-len(item_class_des[i])):
            f3.write(" ")
        f3.write("%-3d\t" % (item_sum[i]))
        f3.write(("%-3d\n")% (item_scale[i]))
