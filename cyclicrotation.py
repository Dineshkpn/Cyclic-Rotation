# -*- coding: utf-8 -*-


def rotatearr(A, K):
    if K == 0:
        return A
    if K == 1:
        pop_value = A.pop(0)
        A.extend([pop_value])
    for i in xrange(1, K):
        pop_value = A.pop(0)
        A.extend([pop_value])
    return A

rotatearr([3, 8, 9, 7, 6], 3)