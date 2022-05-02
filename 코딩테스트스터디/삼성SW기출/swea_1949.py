def dfs(inform):

      global answer, visited

      x,y,h,k,cnt = inform
      #현재지점의 좌표, 현재지점의 높이(h) 해당 지점에서 공사 가능 깊이(k), 현재 까지 공사를 진행한 길이

      if cnt > answer:
            answer = cnt

      for i in range(len(dx)):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

                  now_height = board[nx][ny]
                  
                  #탐색한 등산로가 현재 높이보다 낮으면 바로 연결
                  if now_height < h:

                        visited[nx][ny] = True
                        dfs([nx,ny,now_height,k,cnt+1])
                        visited[nx][ny] = False
                  
                  #등산로를 조성하려는곳이 현재 위치와 같거나 높지만, k만큼 깎는 공사를 하여 현재 높이보다 낮출수 있다면 
                  elif h <= now_height < h + k:

                        visited[nx][ny] = True
                        dfs([nx,ny,(h-1),0,cnt+1]) # 깎았으니 공사 가능 횟수 0 으로 
                        visited[nx][ny] = False



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
   
   N,K = map(int,input().split())

   board = [list(map(int,input().split())) for _ in range(N)]

   top = max(max(board))

   visited = [[False] * N for _ in range(N)]


   answer = 0

   dx = [-1,0,1,0]
   dy = [0,-1,0,1]

   for i in range(N):
      for j in range(N):

            if board[i][j] == top:

                  visited[i][j] = True
                  temp = dfs([i, j, top, K, 1]) # 해당 좌표에서 시작한 등산로 중 가장 긴 경로를 MAX 변수에 갱신함
                  visited[i][j] = False

   print('#{} {}'.format(test_case,answer))
   

