import copy


class NRegine:
    def __init__(self):
        self._num_soluzioni = 0
        self._num_iterazioni = 0
        self._soluzioni = []

    def _risolvi_n_regine(self, N):
        self._num_soluzioni = 0
        self._num_iterazioni = 0
        self._soluzioni = []
        self._ricorsione([ ] , N)

    def _ricorsione(self, parziale, N):
        self._num_iterazioni+=1
        # caso terminale
        if len(parziale)==N:
            #print(parziale)
            self._num_soluzioni+=1
            if self._soluzione_nuova(parziale):
                self._soluzioni.append(copy.deepcopy(parziale))

        # caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append( (row, col) ) # regina
                    if self._nuova_regina_ammissibile(parziale):
                        self._ricorsione(parziale, N)
                    parziale.pop() # rimuove l'ultima regina


    def _nuova_regina_ammissibile(self, parziale):
        # True se ammissibile, False altrimenti

        ultima_regina = parziale[-1]
        for regina in parziale[ : len(parziale)-1]:
            # controllare righe
            if ultima_regina[0] == regina[0]: # stessa riga
                return False
            # controllare colonne
            if ultima_regina[1] == regina[1]: # stessa colonna
                return False
            # contrallare diagonale
            if ((ultima_regina[0]-ultima_regina[1]) ==
                    (regina[0]-regina[1])):
                return False
            if ((ultima_regina[0]+ultima_regina[1]) ==
                    (regina[0]+regina[1])):
                return False
        return True

    def _soluzione_nuova(self, soluzione_nuova):
        for soluzione in self._soluzioni:
            for regina in soluzione_nuova:
                if regina in soluzione:
                    self._num_soluzioni-=1
                    return False
        return True

if __name__ == '__main__':
    nr = NRegine()
    nr._risolvi_n_regine(4)
    print (f"Trovate {nr._num_soluzioni} soluzioni")
    print (f"Chiamata {nr._num_iterazioni} la funzione ricorsiva")
    print (nr._soluzioni)
