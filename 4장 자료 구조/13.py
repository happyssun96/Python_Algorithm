# 회문(palindrome) 찾기
# 입력 : 문자열 s
# 출력 : 회문이면 True, 아니면 False
def palindrome(s):
    # 큐와 스택을 리스트로 정의
    qu = []
    st = []
    # 1단계 : 문자열의 알파벳 문자를 각각 큐와 스택에 넣음
    for x in s:
        # 해당 문자가 알파벳이면(공백, 숫자, 특수문자가 아니면)
        # 큐와 스택에 각각 그 문자를 추가
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
        # 2단계 : 큐와 스택에 들어 있는 문자를 꺼내면서 비교
    while qu: # 큐에 문자가 남아 있는 동안 반복
        if qu.pop(0) != st.pop(): # 큐와 스택에서 꺼낸 문자가 다르면 회문이 아님
            return False
        
    return True
        
print(palindrome("Wow")) # True
print(palindrome("Madam, I'm Adam")) # True
print(palindrome("Madam, I am Adam")) # False

# 연습문제 13-1
def pali(s):
    i = 0          # 문자열의 앞에서 비교할 위치
    j = len(s) - 1 # 문자열의 뒤에서 비교할 위치
    while i < j:   # 중간까지만 검사하면 됨
        # i 위치에 있는 문자가 알파벳 문자가 아니면 뒤로 이동
        if s[i].isalpha() == False:
            i += 1
        # j 위치에 있는 문자가 알파벳 문자가 아니면 앞으로 이동
        elif s[j].isalpha() == False:
            j -= 1
        # i, j 위치 둘다 알파벳 문자가 있으면 두 문자를 비교하고 다르면 회문이 아님
        elif s[i].lower() != s[j].lower():
            return False
        # i와 j 위치에 두 문자를 비교하고 같으면 다음 비교 대상으로 넘어감
        else:
            i += 1
            j -= 1

    return True

print(pali("Wow")) # True
print(pali("Madam, I am Adam")) # False