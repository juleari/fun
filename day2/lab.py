boxes = open( 'data' ).read().split()

def getSize ( box ):
    sides = map( int, box.split('x') )
    sides.sort()

    return sides[0] * sides[1] + sum( 2 * sides[i] * sides[ (i + 1) % 3 ] for i in range(3) )

print sum( map( getSize, boxes ) )