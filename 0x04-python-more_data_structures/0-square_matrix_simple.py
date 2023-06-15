#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ Compute the square value of all integers of a matrix"""
    return ([[col * col for col in row] for row in matrix])
