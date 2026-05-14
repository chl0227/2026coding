# week12-1a.py 學習計畫 Graph - DFS 第1題 Medium 題
# 房間裡有鑰匙, 可以再開新的房間。 最後能開全部房間嗎?
# DFS: Depth First Search 通常會利用 stack 或 function stack (函式呼叫函式)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0] # 我們利用stack 裡面有待處理的房間, 一開始 房間0 是開的
        visited = set() # 有去過、處理過的房間, 不要再進去了
        visited.add(0) # 已經排好、等待處理, 下次有拿到鑰匙, 不要放入stack
        while stack: # 只要stack還有東西,就繼續處理
            now = stack.pop() # 吐出1個房間,現在要處理
            for k in rooms[now]: # 把room now 房間裡,所有的鑰匙k,2.都拿來檢查
                if k in visited: continue # 鑰匙k 對應的房間k看過了,別再檢查了
                # 如果走到這裡,代表沒走過、沒有待處理的房間k
                stack.append(k) # 加入stack 資料結構
                visited.add(k) # 標記這個房間也待處理
        return len(rooms) == len(visited)# 房間的數目
