T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    arr = list(map(int,input().split()))

    print(arr)

    answer = 0

    for i in arr:
        if i % 2 != 0:
            answer += i

    print(test_case,answer)

