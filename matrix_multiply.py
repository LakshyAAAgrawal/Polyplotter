# Author : Lakshya A Agrawal

def matrix_multiply(m1, m2):
    '''
        This module defines a function to multiply 2 given matrices which are multiplication compatible.
        
        Prerequisite:
        the number of columns of m1 is same as the number of rows of m2
        
        Returns a matrix represented as list of list.
    '''
    m=[]
    for i in range(len(m1)):
        m_new=[]
        for k in range(len(m2[0])):
            s=0
            for j in range(len(m1[0])):
                s=s+(float(m1[i][j])*float(m2[j][k]))
            m_new.append(s)
        m.append(m_new)
    return(m)
