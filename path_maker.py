import numpy as np

# # 꽃 모양의 x, y 경로 생성
# theta = np.linspace(0, 2*np.pi, 1000)
# radius = np.sin(6 * theta) * np.cos(4 * theta)
# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# # 경로를 CSV 파일로 저장
# data = np.column_stack((x, y))
# np.savetxt('flower_path.csv', data, delimiter=',')

# print("flower_path.csv 파일이 생성되었습니다.")

# 네잎클로버 모양의 x, y 경로 생성
theta = np.linspace(0, 2*np.pi, 1000)
radius = np.sin(4 * theta) * np.cos(4 * theta)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# 경로를 CSV 파일로 저장
data = np.column_stack((x, y))
np.savetxt('./paths/clover_path.csv', data, delimiter=',')

print("clover_path.csv 파일이 생성되었습니다.")
