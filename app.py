import sys

def sum_values(a,b,c):
    '''  adding parametes 
    Parameters
        a (int)
        b (int)
        c (int)
    Returns 
        sum (int): sum of above number based on condition
    '''
    temp=[13,14,17,18,19]
    sum=a+b+c
    sum= sum-a if a in temp else sum
    sum= sum-b if b  in temp else sum
    sum= sum-c if c  in temp else sum
    return sum

def main(a,b,c):
    '''check all argument value are interger type or not
    Parameters
        a (string)
        b (string)
        c (string)
    Returns 
        sum (int): sum of above number based on condition
        ValueError : if all parameter are not type casted to int 
    '''

    try:
        a,b,c=map(int,[a,b,c])
    except ValueError as es:
        return 'All inputs must be numeric'
    else:
        result=sum_values(a,b,c)
        return result

if __name__=='__main__':
    try:
        _,a,b,c=sys.argv
    except ValueError as e:
        print('Exactly 3 numbers are required')
    else:
        result=main(a,b,c)
        print(result)
