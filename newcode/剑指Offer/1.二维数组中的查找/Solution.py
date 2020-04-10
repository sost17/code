# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        rows = len(array)
        columns = len(array[0])
        if rows == 0 or columns == 0:
            return False
        row = rows -1
        column = 0
        while( row >= 0 and column <= columns -1):
            if array[row][column] < target:
                column +=1
            elif array[row][column] > target:
                row -=1
            else :
                return True
        return False

if __name__ == '__main__':
    arrays =[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(Solution().Find(11,arrays))