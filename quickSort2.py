def quicksort(self,L, first, last):
        i = first
        j = last
        pivote = L[int((first+last)/2)]

        while i < j:
            while L[i].Ganados < pivote.Ganados:
                i+=1
            while L[j].Ganados > pivote.Ganados:
                j-=1
            if (i <= j):
                x = L[j]
                L[j] = L[i]
                L[i] = x
                i+=1
                j-=1

        if first < j:
            L = self.quicksort(L, first, j)
        if last > i:
            L = self.quicksort(L, i, last)

        return L
