import sys

names = ["심원용", "심투용", "심삼용"]
subjects = ["수학", "영어", "과학"]

row_number = 3
col_number = 3
table = []

for i in range(row_number):
    arr = []
    for j in range(col_number):
        arr.append(0)
    table.append(arr)

# 성적 입력
table[0][0] = 40
table[0][1] = 90
table[0][2] = 80
table[1][0] = 10
table[1][1] = 20
table[1][2] = 30
table[2][0] = 70
table[2][1] = 60
table[2][2] = 50

for x in table:
    print(x)

# 과목별 평균
# total = [0,0,0]
# avg = [0,0,0]
#
# for j in range(col_number):
#     for i in range(row_number):
#         total[j] += table[i][j]
#     avg[j] = total[j] / row_number
#
# for i in range(col_number):
#     print(f"{subjects[i]} : {avg[i]}")

# 학생별 총점과 평균
# student_total_list = []
# student_mean_list = []
#
# for i in range(row_number):
#     total = 0
#     for j in range(col_number):
#         total += table[i][j]
#         student_total_list.append(total)
#
# for i in range(row_number):
#     print(f"{names[i]} 학생의 총점은 {student_total_list[i]} 이고 , "
#       f"평균은 {student_total_list[i] / col_number} 입니다.")


# 과목별 최고 점수와 해당 학생 이름
# top_list = []
# top_idx_list = []
#
# for i in range(col_number):
#     top = -1
#     top_idx = -1
#     for j in range(row_number):
#         if top < table[j][i]:
#             top = table[j][i]
#             top_idx = j
#     top_list.append(top)
#     top_idx_list.append(top_idx)
#
# print(top_list)
# print(top_idx_list)
#
# for i in range(3):
#     print(names[top_idx_list[i]])

# 총점 최고득점자와 최저득점자 이름
std_total_list = []
for i in range(3):
    std_score = table[i]
    std_total = std_score[0] + std_score[1] + std_score[2]
    std_total_list.append(std_total)
print(std_total_list)

top = -1
top_idx = -1
bottom = sys.maxsize
bottom_idx = -1
for i in range(3):
    if top < std_total_list[i]:
        top = std_total_list[i]
        top_idx = i
    if bottom > std_total_list[i]:
        bottom = std_total_list[i]
        bottom_idx = i

print(f"최고점 : {top} , 이름은 : {names[top_idx]} ")
print(f"최저점 : {bottom} , 이름은 : {names[bottom_idx]} ")


# 평균 미만 출력 (평균 60점 미만)
# for i in range(row_number):
#     total = 0
#     for j in range(col_number):
#         total += table[i][j]
#     avg = total / col_number
#     if avg < 60:
#         print(f"{names[i]} : 평균 {avg}점")

# 과락자 출력 (1과목이라도 40점 이하인 경우)
# for i in range(row_number):
#     is_fail = False
#     for j in range(col_number):
#         if table[i][j] <= 40:
#             is_fail = True
#             break
#     if is_fail:
#         print(f"{names[i]} : 과락")