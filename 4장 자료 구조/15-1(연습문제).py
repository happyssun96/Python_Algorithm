# 그래프 탐색: 너비 우선 탐색
# 입력: 그래프 g, 탐색 시작점 start
# 출력: start에서 출발해 연결된 꼭짓점들을 출력

def search(g, start):
    qu = []  # 기억장소 1 : 앞으로 처리해야 할 사람들을 큐에 저장
    done = set() # 기억장소 2 : 이미 큐에 추가한 꼭짓점들을 집합에 기록(중복 방지)

    qu.append(start) # 시작점을 큐에 넣고 시작
    done.add(start) # 집합에도 추가

    while qu:   # 큐에 처리할 꼭짓점이 남아 있는 동안
        p = qu.pop(0)   # 큐에서 처리 대상을 하나 꺼내
        print(p) # 꼭짓점 이름을 출력
        for x in g[p]: # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 꼭짓점들을
                qu.append(x) # 큐에 추가
                done.add(x) # 집합에도 추가

graph = {
    1 : [2,3],
    2 : [1, 4, 5],
    3 : [1],
    4  : [2],
    5 : [2]
}

search(graph, 1)
print()
