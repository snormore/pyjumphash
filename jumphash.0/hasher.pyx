
cdef long jumphash(int N, long key):
    cdef int b = -1
    cdef int j = 0
    cdef double d1, d2
    while j < N:
        b = j
        key = key * 2862933555777941757 + 1
        d1 = b+1
        d2 = 1L << 31
        d2 /= (key >> 33) + 1
        j = int(d1 * d2)
        # j = double(b+1) * (double(1L << 31) / double((key >> 33) + 1))
    return b
