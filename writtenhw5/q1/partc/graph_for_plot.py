def graph_function(xmin,xmax,xres,function,*args):
    "takes a given mathematical function and graphs it-how it works is not important"
    x, y = [],[]
    i = 0
    while xmin + i * xres <= xmax:
        x.append(xmin + i * xres)
        y.append(function(x[i], *args))
        i += 1
    return x, y
