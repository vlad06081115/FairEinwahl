import matplotlib.pyplot as plt
import numpy as np

s = 'popa%'
s = s.replace('%', '')
print(s)








# x = np.arange(10)
# y = np.random.rand(10)
# plt.bar(x, y)
# plt.xticks(x, [f'Cat {i}' for i in x], rotation=45, fontsize=10, ha='right')
# plt.tight_layout()   # чтобы подписи не обрезались
# plt.show()








# data = [12, 25, 47, 65, 78, 90, 99]
# bins = [0, 30, 60, 88, 100]
# labels = ["0-30%", "30-60%", "60-88%", "90-100%"]

# categories = pd.cut(data, bins=bins, labels=labels)
# count = categories.value_counts()

# print(count)


# data = {
#         'student' : [],
#         'total_satisfaction' : []
#     }
# all_formed_semestrs_df = [11.1, 11.2, 12.1]
# for semestr in all_formed_semestrs_df:
#     data[f"{semestr}_satisfaction"] = []

# personal_statistik_df = pd.DataFrame(data)


# print(round(2 / 3, 2))
