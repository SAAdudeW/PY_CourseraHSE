class Matrix:

    def __init__(self, sqlist):
        self.nrows = len(sqlist)
        self.ncolumns = len(sqlist[0])

        for row in sqlist:
            self.row = row.copy()


a = Matrix([[1, 2], [3, 4]])
print(a.nrows, a.ncolumns)
