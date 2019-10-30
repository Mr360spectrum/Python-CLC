# Karter Ence
# High Score Columns
# 9/17/2019

# create and initialize three name variables
# (name1, name2, name3)
name1 = "BossLady"
name2 = "Hunter"
name3 = "AAA"
# create and initialize three score variables
# (score1, score2, score3)
score1 = 1000
score2 = 995
score3 = 850
# print a title for the high scores list
print(str.format("{0:^26}","High Scores"))
print(str.format("{0:^15} {1:^10}","Player Name","High Score"))
print("---------------------------")
# print each of the three score lines with name and score in neat columns
print(str.format("{0:^15.15} {1:>10,}",name1,score1))
print(str.format("{0:^15.15} {1:>10,}",name2,score2))
print(str.format("{0:^15.15} {1:>10,}",name3,score3))
