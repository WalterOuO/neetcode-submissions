class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        lon = len(self.arr)
        if lon % 2 != 0:
            return self.arr[lon//2]
        else:
            return (self.arr[(lon//2)-1] + self.arr[lon//2] ) /2

        