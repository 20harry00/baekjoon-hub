def solution(arr):
    """
    arr: n x n 2차원 리스트
    return: arr이 대칭행렬이면 1, 아니면 0
    """
    n = len(arr)
    for i in range(n):
        # j는 i보다 큰 쪽만 비교하면 충분
        for j in range(i + 1, n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
