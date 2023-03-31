from scipy import stats
view_avg = [351.18 ,163.76 ,336.24 ,905.87 ,378.86 ,499.94 ,250.99 ,310.83 ,265.69 ,481.83 ,320.53 ,416.77 ,80.13 ,295.70 ,306.35 ,326.71 ,284.03 ,382.26 ,148.69 ,245.11 ]
fav_avg = [0.23 ,0.11 ,0.21 ,0.70 ,0.29 ,0.30 ,0.19 ,0.40 ,0.29 ,0.42 ,0.33 ,0.49 ,0.23 ,0.23 ,0.33 ,0.31 ,0.23 ,0.29 ,0.19 ,0.19 ]
score_avg = [1.39 ,0.53 ,1.32 ,3.96 ,1.35 ,1.44 ,1.11 ,1.37 ,1.25 ,1.68 ,1.19 ,1.81 ,0.65 ,0.93 ,1.20 ,1.08 ,0.87 ,1.23 ,0.66 ,0.66]
avgAns = [0.82 ,0.76 ,0.81 ,1.04 ,0.87 ,0.99 ,0.70 ,0.75 ,0.82 ,0.92 ,0.86 ,0.88 ,0.61 ,0.63 ,0.83 ,0.93 ,0.70 ,0.80 ,0.59 ,0.64]

ans_percentage = [0.66 ,0.60 ,0.66 ,0.74 ,0.69 ,0.73 ,0.76 ,0.60 ,0.62 ,0.67 ,0.67 ,0.55 ,0.51 ,0.65 ,0.74 ,0.65 ,0.58 ,0.65 ,0.55 ,0.53]
acc_ans_percentage = [0.36 ,0.33 ,0.36 ,0.39 ,0.39 ,0.45 ,0.41 ,0.35 ,0.28 ,0.38 ,0.36 ,0.26 ,0.25 ,0.34 ,0.39 ,0.38 ,0.28 ,0.34 ,0.28 ,0.23]
first_ans_interval = [4.56 ,1.60 ,4.54 ,5.16 ,3.60 ,5.50 ,2.66 ,5.21 ,7.50 ,2.98 ,8.24 ,18.68 ,4.53 ,5.57 ,8.62 ,6.88 ,5.56 ,5.51 ,4.59 ,7.50]
acc_time = [4.87 ,4.10 ,4.58 ,5.16 ,5.07 ,5.89 ,3.83 ,8.61 ,8.52 ,3.62 ,10.19 ,54.92 ,4.53 ,8.45 ,12.40 ,8.42 ,11.46 ,12.84 ,4.59 ,9.21]
post_avg_len = [1269.17 ,1997.00 ,1122.81 ,773.00 ,1657.71 ,1408.20 ,1658.66 ,2454.76 ,1414.24 ,1124.58 ,1577.84 ,1795.88 ,2048.67 ,1434.18 ,1821.34 ,1239.09 ,1953.91 ,1661.83 ,1772.76 ,2329.54]


print("view_avg:")
print("ans_percentage"+str(stats.spearmanr(view_avg, ans_percentage,alternative='greater')))
print("acc_ans_percentage"+str(stats.spearmanr(view_avg, acc_ans_percentage, alternative='greater')))
print("first_ans_interval"+str(stats.spearmanr(view_avg, first_ans_interval, alternative='greater')))
print("acc_time"+str(stats.spearmanr(view_avg, acc_time, alternative='greater')))
print("post_avg_len"+str(stats.spearmanr(view_avg, post_avg_len, alternative='less')))
print("--------------")
print("fav_avg:")
print("ans_percentage"+str(stats.spearmanr(fav_avg, ans_percentage,alternative='greater')))
print("acc_ans_percentage"+str(stats.spearmanr(fav_avg, acc_ans_percentage,alternative='greater')))
print("first_ans_interval"+str(stats.spearmanr(fav_avg, first_ans_interval,alternative='greater')))
print("acc_time"+str(stats.spearmanr(fav_avg, acc_time, alternative='greater')))
print("post_avg_len"+str(stats.spearmanr(fav_avg, post_avg_len, alternative='less')))
print("--------------")
print("score_avg:")
print("ans_percentage"+str(stats.spearmanr(score_avg, ans_percentage,alternative='greater')))
print("acc_ans_percentage"+str(stats.spearmanr(score_avg, acc_ans_percentage, alternative='greater')))
print("first_ans_interval"+str(stats.spearmanr(score_avg, first_ans_interval, alternative='greater')))
print("acc_time"+str(stats.spearmanr(score_avg, acc_time,alternative='greater')))
print("post_avg_len"+str(stats.spearmanr(score_avg, post_avg_len, alternative='less')))
print("--------------")
print("avgAns:")
print("ans_percentage"+str(stats.spearmanr(avgAns, ans_percentage,alternative='greater')))
print("acc_ans_percentage"+str(stats.spearmanr(avgAns, acc_ans_percentage, alternative='greater')))
print("first_ans_interval"+str(stats.spearmanr(avgAns, first_ans_interval, alternative='greater')))
print("acc_time"+str(stats.spearmanr(avgAns, acc_time, alternative='greater')))
print("post_avg_len"+str(stats.spearmanr(avgAns, post_avg_len, alternative='less')))

print("difficulty")
print("ans_p-acc_p:"+str(stats.spearmanr(ans_percentage, acc_ans_percentage,alternative='greater')))
print("ans_p-f_ans_time:"+str(stats.spearmanr(ans_percentage, first_ans_interval,alternative='less')))
print("ans_p-acc_ans_time:"+str(stats.spearmanr(ans_percentage, acc_time,alternative='less')))
print("ans_p-post_len:"+str(stats.spearmanr(ans_percentage, post_avg_len,alternative='less')))

print("acc_p-f_ans_time:"+str(stats.spearmanr(acc_ans_percentage, first_ans_interval,alternative='less')))
print("acc_p-acc_ans_time:"+str(stats.spearmanr(acc_ans_percentage, acc_time,alternative='less')))
print("acc_p-post_len:"+str(stats.spearmanr(acc_ans_percentage, post_avg_len,alternative='less')))

print("f_ans_time-acc_ans_time:"+str(stats.spearmanr(first_ans_interval, acc_time,alternative='greater')))
print("f_ans_time-post_len:"+str(stats.spearmanr(first_ans_interval, post_avg_len,alternative='greater')))

print("acc_ans_time-post_len:"+str(stats.spearmanr(acc_time, post_avg_len,alternative='greater')))




