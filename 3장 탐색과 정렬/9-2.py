# 일반적인 삽입 정렬 알고리즘
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬됨)

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i] # i번 위치에 있는 값을 key에 저장
        j = i - 1 # j를 i 바로 왼쪽 위치로 저장
        while j>=0 and a[j] > key:
            a[j+1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j+1] = key # 찾은 삽입 위치에 key를 저장

d = [2,4,5,1,3]
ins_sort(d)
print(d)

# 연습문제 9-2
def ins_max_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i] # i번 위치에 있는 값을 key에 저장
        j = i - 1 # j를 i 바로 왼쪽 위치로 저장
        while j>=0 and a[j] < key:
            a[j+1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
        a[j+1] = key # 찾은 삽입 위치에 key를 저장

k = [2,4,5,1,3]
ins_max_sort(k)
print(k)