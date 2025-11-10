
class DichotomicSearch:
    def __init__(self):
        pass

    def search(self, input, val):
        if len(input) == 1:
            if input[0] == val:
                return True
            else:
                return False
        else:
            indice = len(input) // 2
            return self.search(input[:indice], val) or self.search(input[indice:], val)


if __name__ == '__main__':
    sequenza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dic = DichotomicSearch()
    print(dic.search(sequenza, 17))