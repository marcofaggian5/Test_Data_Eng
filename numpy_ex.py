import numpy as np

if __name__ == '__main__':

    a = np.arange(10)

    # extract odd numbers
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def select_odd(array: np.ndarray) -> (np.ndarray):
        out = np.array([])
        for el in array:
            if el % 2 == 1:
                out = np.append(out, el)
        return out

    a = np.full((3, 3), True, dtype=bool)

    # replace odd numbers with -1
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def replace_odd(array: np.ndarray, replacement: int) -> (np.ndarray):
        out = np.array([])
        for el in array:
            if el % 2 == 1:
                out = np.append(out, -1)
            else:
                out = np.append(out, el)
        return out


    arr[arr % 2 == 1] = -1

    arr = np.arange(10)
    out = np.where(arr % 2 == 1, -1, arr)
    print(arr)
    print(out)

    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

    # common items
    print(np.intersect1d(a, b))
    # How to remove from one array those items that exist in another?
    print(np.setdiff1d(a, b))
    # positions where elements of two arrays match
    print(np.where(a == b))

    def maxx(x, y):
        """Get the maximum of two items"""
        if x >= y:
            return x
        else:
            return y

    pair_max = np.vectorize(maxx, otypes=[float])

    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])

    print(pair_max(a, b))

