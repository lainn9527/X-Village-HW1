import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.setValues(nrows, ncols)
        self.matrix = list()
        for i in range(0, nrows):
            self.matrix.append([random.randint(0, 9) for j in range(0, ncols)])

    def add(self, m):
        """return a new Matrix object after summation"""
        if not self.checkSize(m):
            return None
        else:
            temp = list()
            for colA, colB in zip(self.matrix, m.matrix):
                temp.append([i1 + i2 for i1, i2 in zip(colA, colB)])
            tempMatrix = Matrix(self.rows, self.cols)
            tempMatrix.matrix = temp.copy()
            return tempMatrix

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if not self.checkSize(m):
            return None
        else:
            temp = list()
            for colA, colB in zip(self.matrix, m.matrix):
                temp.append([i1 - i2 for i1, i2 in zip(colA, colB)])
            tempMatrix = Matrix(self.rows, self.cols)
            tempMatrix.matrix = temp.copy()
            return tempMatrix

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if self.cols != m.rows:
            print("Matrixs' size should be in the same size")
            return None
        else:
            transB = m.transpose()
            tempList = list()
            for row in self.matrix:
                tempRow = list()
                for col in transB.matrix:
                    result = 0
                    for i in range(0, len(row)):
                        result += row[i] * col[i]
                    tempRow.append(result)
                tempList.append(tempRow)

            tempMatrix = Matrix(self.rows, m.cols)
            tempMatrix.matrix = tempList
            return tempMatrix

    def transpose(self):
        """return a new Matrix object after transpose"""
        temp = [[self.matrix[i][j]
                 for i in range(0, self.rows)]
                for j in range(0, self.cols)]
        tempMatrix = Matrix(self.cols, self.rows)
        tempMatrix.matrix = temp
        return tempMatrix

    def display(self):
        """Display the content in the matrix"""
        for col in self.matrix:
            for item in col:
                print(item, end=' ')
            print()

    def checkSize(self, m):
        if self.rows != m.rows or self.cols != m.cols:
            print("Matrixs' size should be in the same size")
            return False
        else:
            return True

    def setValues(self, row, col):
        self.rows = row
        self.cols = col
