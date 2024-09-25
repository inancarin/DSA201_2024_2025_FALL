"""
matrix = [
          [1, 2, 3],
          [4, 5, 6],
          [9, 8, 9],
        ]
"""

matrix = [
          [1, 2, 3, 100, 20],
          [4, 5, 6, 30, 1000],
          [9, 8, 10, 4, 25],
          [198, 10, 20, 30, 40],
          [77, 66, 55, 44, 33]
        ]


sum1, sum2 = 0, 0
j = len(matrix) - 1 # initial col value
for i in range(len(matrix)):
    sum1 += matrix[i][i]
    sum2 += matrix[i][j]
    j -= 1

diff = abs(sum1 - sum2)
print(diff)
