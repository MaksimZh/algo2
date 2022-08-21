class Heap:

    def __init__(self):
        self.HeapArray = []
        self.__capacity = 0
        self.__size = 0
		
    def MakeHeap(self, a, depth):
        self.__capacity = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * self.__capacity
        self.__size = 0
        for key in a:
            self.Add(key)

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1 # если куча пуста

    def Add(self, key):
        if self.__size == self.__capacity:
            return False
        index = self.__size
        self.HeapArray[index] = key
        self.__size += 1
        
        while index > 0:
            parent_index = _parent_index(index)
            
            if self.HeapArray[parent_index] > self.HeapArray[index]:
                break

            tmp = self.HeapArray[index]
            self.HeapArray[index] = self.HeapArray[parent_index]
            self.HeapArray[parent_index] = tmp
            del tmp

            index = parent_index
            del parent_index


def _left_child_index(i):
    return 2 * i + 1

def _right_child_index(i):
    return 2 * i + 2

def _parent_index(i):
    return (i - 1) // 2
