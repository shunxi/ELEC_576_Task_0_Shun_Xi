def helper(res,n):
    if n == 0 or n ==1:
        return 1
    else:
        if n not in res:
            res[n] = helper(res, n-1) + helper(res, n-2)
            return res[n]
        else:
            return res[n]
res = {}

n = raw_input('Which nth Fibonacci number you like to calculate?')
n = int(n)# Pytho
print 'The ' + str(n) + 'th Fibonacci number is ' + str(helper(res,n)) + '.'
print 'Thanks'
raw_input("Press Enter to continue...")