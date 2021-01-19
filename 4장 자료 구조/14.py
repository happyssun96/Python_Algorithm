# 동명이인 찾기
# 입력 : 이름이 n개 들어있는 리스트
# 출력 : n개의 이름 중 반복되는 이름의 집합
def find_same_name(a):
    # 1단계 : 각 이름이 등장한 횟수를 딕셔너리로 만듦
    name_dict = {}
    for name in a:  # 리스트 a에 있는 자료들을 차례로 반복
        if name in name_dict:   # 이름이 name_dict에 있으면
            name_dict[name] += 1    # 등장 횟수를 1증가
        else:   # 새 이름이면
            name_dict[name] = 1
    # 2단계 만들어진 딕셔너리에서 등장 횟수가 2 이상인 것을 결과에 추가
    result = set()  # 결과값을 저장할 빈 집합
    for name in name_dict:  # 딕셔너리 name_dict에 있는 자료들을 차례로 반복
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ['Tom', 'Jerry', 'Mike', 'Tom', 'Jerry']
print(find_same_name(name))

# 연습문제 14-1
# 학생 번호에 해당하는 학생 이름 찾기(dict 이용)
# 입력: 학생 명부 딕셔너리 s_info, 찾는 학생 번호 find_no
# 출력: 해당하는 학생 이름, 해당하는 학생 번호가 없으면 물음표 "?"

def std_search(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]
    else:
        return "?"

student_info = {
    39: "Justin",
    14: "John",
    67: "Mike",
    105: "Summer"
}

print(std_search(student_info, 67))
print(std_search(student_info, 10000))