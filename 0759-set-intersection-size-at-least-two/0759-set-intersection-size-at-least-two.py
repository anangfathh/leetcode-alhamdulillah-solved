#Urutkan interval dari endpointnya
#ambil dari ujung kanan pada interval pertama
#cek apakah sudah ada nilai yang cocok dengan interval ke-2 pada angka yang telah kita ambil di interval sebelumnya
#jika count == 1 maka tambahkan nilai paling kanan pada interval tersebut
#jika count == 2 maka continue ke next interval
#return length dari array take

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        p1 = p2 = -1e9
        res = 0
        
        for L, R in intervals:
            count = int(p1 >= L) + int(p2 >= L)
            
            if count == 2:
                continue
            elif count == 1:
                res += 1
                if p1 >= L:
                    p2 = R
                else:
                    p1, p2 = p2, R
            else:
                res += 2
                p1, p2 = R-1, R
        
        return res
        