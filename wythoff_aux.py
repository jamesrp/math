def moves_from(a,b):
    for i in xrange(a):
        yield (i,b)
    for i in xrange(b):
        yield (a,i)
    for i in xrange(1,min(a,b)+1):
        yield (a-i,b-i)

