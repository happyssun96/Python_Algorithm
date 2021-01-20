# Python_Algorithm
<h3>질문</h3>
<p> 연습문제 15-2 설명에 대해 -> 코드 설명이 전부인가? -> Yes </p>
<img src="https://user-images.githubusercontent.com/59468442/105175209-f4fdd600-5b66-11eb-8efe-a4a594bb7789.png" />
<p>
<ol>
    <li>시작 꼭짓점을 qu와 done에 각각 추가하고 시작합니다. -> qu = [1], done = {1}</li>
    <li>qu에서 1을 꺼내 출력합니다. -> qu = [], done = {1}</li>
    <li>1에 연결된 2,3을 qu와 done에 추가합니다. -> qu=[2,3], done={1,2,3}</li>
    <li>qu에서 2를 꺼내 출력합니다. -> qu=[3], done={1,2,3}</li>
    <li>2에 연결된 1,4,5중에서 1은 이미 done에 있으므로 중복되지 않도록 제외하고 4,5를 qu와 done에 추가합니다. -> qu=[3,4,5], done={1,2,3,4,5}</li>
    <li>qu에서 3을 꺼내 출력합니다. -> qu=[4,5], done={1,2,3,4,5}</li>
    <li>3에 연결된 1은 이미 done에 있으므로 추가하지 않습니다.</li>
    <li>qu에서 4를 꺼내 출력합니다. -> qu=[5], done={1,2,3,4,5}</li>
    <li>4에 연결된 2는 이미 done에 있으므로 추가하지 않습니다.</li>
    <li>qu에서 5를 꺼내 출력합니다. -> qu=[], done={1,2,3,4,5}</li>
    <li>5에 연결된 2는 이미 done에 있으므로 추가하지 않습니다.</li>
    <li>qu가 비었으므로 종료합니다.</li>
    <li>이 과정으로 출력된 꼭짓점 순서는 1->2->3->4->5입니다.</li>
</ol>
</p>

<h3> 질문 2 </h3>
168페이지find_fakecoin 함수 중간
<pre>
def find_fakecoin(left, right):
    for i in range(left+1, right+1): # left+1 부터 right까지 반복
        # 가장 왼쪽 동전과 나머지 동전을 차례로 비교
        result = weigh(left, left, i, i)
        if result == -1:    # left 동전이 가벼움(left 동전이 가짜)
            return left
        elif result == 1:   # i 동전이 가벼움(i 동전이 가짜)
            return i
        # 두 동전의 무게가 같으면 다음 동전으로
    # 모든 동전의 무게가 같으면 가짜 동전이 없는 예외 경우
    return -1
</pre>
<br />
이 부분에 result 부분 비교하는 부분부터 이해가 안감 <br/>
그 다음 장에 나오는 두번째 방법도 마찬가지
