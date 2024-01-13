import numpy as np
import matplotlib.pyplot as plt

# 꽃 모양의 x, y 경로 생성
# theta = np.linspace(0, 2*np.pi, 1000)
# radius = np.sin(6 * theta) * np.cos(4 * theta)
# x = radius * np.cos(theta) * 100
# y = radius * np.sin(theta) * 100

# # 경로를 CSV 파일로 저장
# data = np.column_stack((x, y))
# np.savetxt('./paths/flower_path.csv', data, delimiter=',')

# print("flower_path.csv 파일이 생성되었습니다.")

# # 네잎클로버 모양의 x, y 경로 생성
# theta = np.linspace(0, 2*np.pi, 1000)
# radius = np.sin(4 * theta) * np.cos(4 * theta)
# x = radius * np.cos(theta) * 100
# y = radius * np.sin(theta) * 100

# # 경로를 CSV 파일로 저장
# data = np.column_stack((x, y))
# np.savetxt('./paths/clover_path.csv', data, delimiter=',')

# print("clover_path.csv 파일이 생성되었습니다.")


# # 반지름 설정
# radius = 5

# # 각도 배열 생성
# theta = np.linspace(0, 2*np.pi, 1000)

# # 원의 방정식을 이용하여 x, y 좌표 계산
# x = radius * np.cos(theta)
# y = radius * np.sin(theta) + 5  # 중심이 (0, 5)이므로 y에 5를 더합니다.

# # 경로를 CSV 파일로 저장
# data = np.column_stack((x, y))
# np.savetxt('./paths/circle_path.csv', data, delimiter=',')

# print("circle_path.csv 파일이 생성되었습니다.")

# # 결과를 그래프로 표시
# plt.plot(x, y)
# plt.title('원 경로')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()

# 톱니바퀴 모양의 x, y 경로 생성
theta = np.linspace(0, 2*np.pi, 1000)
radius = 5

# 울퉁불퉁한 모양 추가
bumps = 7 # 울퉁불퉁한 부분의 개수
bump_height = 1  # 울퉁불퉁한 부분의 높이
bump_width = 1 # 울퉁불퉁한 부분의 폭

x = (radius + bump_height * np.cos(bumps * theta)) * np.cos(theta)
y = (radius + bump_height * np.cos(bumps * theta)) * np.sin(theta)

data = np.column_stack((x, y))
np.savetxt('./paths/gear_path.csv', data, delimiter=',')

# 경로를 그래프로 표시
plt.plot(x, y)
plt.title('gear path')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()