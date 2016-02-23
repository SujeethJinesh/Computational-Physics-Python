import matplotlib.pyplot as P

x0, x1 = -2, 2
y0, y1 = -2, 2

def mandel_python(n=100,maxi=512):

    dx, dy = (x1-x0)/(n-1), (y1-y0)/(n-1)


    xs = [x0 + i*dx for i in range(n)]
    ys = [y0 + i*dy for i in range(n)] #get complex arrays

    result = []                     #this will hold your array values
    for y in ys:
        row = []
        for x in xs:
            z, c = 0, x + 1j*y

            escape = maxi
            for i in range(1,maxi): # calculates using given formula
                z = z*z + c

                if abs(z) > 2:
                    escape = i
                    break

            row.append(escape)
        result.append(row)

    return result

P.figure()
P.imshow(mandel_python(),origin='lower',extent=(x0,x1,y0,y1))
P.show()