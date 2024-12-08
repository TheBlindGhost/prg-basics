arr = [
[1,2,3],
[4,5,6],
[7,8,9]
]


def transpose_matrix(m):
    for i in range(len(m[0])):
        for j in range(len(m)):
            return m[j][i]

    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

print(transpose_matrix(arr))