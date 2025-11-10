from functools import lru_cache
from time import time

class Fibonacci:
    def __init__(self):
        self._cache = {0: 0, 1: 1}

    def calcola_elemento_caching(self, n):
        if self._cache.get(n) is not None:
           return self._cache[n]
        else:
            self._cache[n] = (self.calcola_elemento_caching(n-1)+
                              self.calcola_elemento_caching(n-2))
            return self._cache[n]

    @lru_cache(maxsize=None)
    def calcola_elemento(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.calcola_elemento(n-1)+
                    self.calcola_elemento(n-2))




if __name__ == '__main__':
    fib = Fibonacci()
    print("Calcola elemento CON caching LRU")
    start_time = time()
    print(fib.calcola_elemento(300))
    end_time = time()
    print(end_time - start_time)

    print("Calcola elemento CON caching")
    start_time = time()
    print(fib.calcola_elemento_caching(300))
    end_time = time()
    print(end_time - start_time)

