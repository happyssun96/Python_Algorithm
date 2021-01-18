# 선택 정렬
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최솟값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]

d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)

# 연습문제 8-2
def max_sort(a):
    n = len(a)
    for i in range(0, n-1):
        max_idx = i # 최댓값 찾기
        for j in range(i+1, n):
            if a[j] > a[max_idx]: # 부등호 방향 반대로
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]
    
k = [2,4,5,1,3]
max_sort(k)
print(k)