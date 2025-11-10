
class Quicksort():
    def __init__(self):
        pass

    def sort(self, sequenza):
        if len(sequenza) <= 1:
            return sequenza
        else:
            # 1) Scegliere il pivot
            pivot = sequenza[0]
            # 2) Dividere la seq. in sottoseq.
            sequenza_minori = []
            for i in range(1, len(sequenza)):
                if sequenza[i] < pivot:
                    sequenza_minori.append(sequenza[i])

            # Con list comprehension, più sintetico
            sequenza_uguali = [n for n in sequenza if n == pivot]
            sequenza_maggiori = [n for n in sequenza if n > pivot]

            # 3) Fare il sort delle sottoseq. e appendere i risultati
            return  self.sort(sequenza_minori) + sequenza_uguali + self.sort(sequenza_maggiori)

if __name__ == '__main__':
    sequenza = [3, 7, 11, 2, 5, 9, 4, 7]
    qs = Quicksort()
    print(qs.sort(sequenza))

