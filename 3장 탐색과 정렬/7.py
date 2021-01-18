# 순차 탐색
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1
def search_list(a,x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i
    return -1

v = [17, 92, 18, 33, 58, 7, 33 ,42]
print(search_list(v, 18)) # 2
print(search_list(v, 900)) # -1

# 연습문제 7-1
def searching(a,x):
    n = len(a)
    result = []
    for i in range(0, n):
        if x == a[i]:
            result.append(i)

    return result
mv = [17, 92, 18, 33, 58, 7, 33, 42]
print(searching(mv, 18))   # [2]    (순서상 세 번째지만, 위치 번호는 2)
print(searching(mv, 33))   # [3, 6] (33은 리스트에 두 번 나옴)
print(searching(mv, 900))  # []     (900은 리스트에 없음)

# 연습문제 7-2
# O(n)

# 연습문제 7-3
def std_search(s_no, s_name, find_no):
    n = len(s_no)
    for i in range(0, n):
        if find_no == s_no[i]:
            return s_name[i]
    return -1

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]
print(std_search(stu_no, stu_name, 105)) # "Summer"
print(std_search(stu_no, stu_name, 777)) # 없으므로 -1