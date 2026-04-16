# week08-1.py 學習計畫 Binary Search 第1題
class Solution:
    def guessNumber(self, n: int) -> int:
        # 另一種寫法
        # for i in ragne(n+1): print( - guess(i), end=' ') # 做個實驗, 不用寫
        return bisect_left(range(n+1), 0, key=lambda x:-guess(x)) # 一行抵下面7行
        # for i in range(i, n+1): # 錯誤的暴力法, for 迴圈找答案
        #    if guess(i)==0: return i # 猜中了,答案是i
        # 不能用上面的 for 迴圈,因為 n 有20億這麼大,試不完
        # 要用小學「猜數字」每次範圍猜一半, 比他大、比他小,縮小範圍
        # 方法2:while left < right : 去逼近
        left, right = 1, n+1 # 左右的範圍(左「包含」、右「不包含」)
        while left < right: # 左右的範圍還沒有「撞再一起」
            mid = (left + right) // 2 # (猜) 中間的數
            if guess(mid) == 0: return mid # 猜到中間的數字
            if guess(mid) > 0: left = mid+1 # (暗示你) 再高一點
            else: right = mid # (暗示你)再低一點(中點設成上界)
        return left
