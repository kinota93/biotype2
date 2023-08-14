`A = (a[0],a[1],\cdots,a[n-1])`

A bin is an open-closed interval `(s, t]`

```python

def exec_segment(a, b, precision, step):
    """refine bins `b` by segmenting `a` with precision constraint 
     @params a: list of items sorted in acending order, b: bins of a, 
       precision: gap between items in a segment will not exceed this precision,
       step: granularity of segments
    """ 
    done = True
    new_bins = b[:] # make a copy
    for s, t in pairwise(b)
        for i in range(s+1,t):
            j = i + step
            if j < n and a[j] - a[i] > precision:
                new_bins += [j-1]
                done = False

    new_bins = sorted(new_bins)
            
    if done:
        return new_bins
    else:
        return exec_segment(a, new_bins, precision, step+1)
  

def pairwise(b):
    """transform b to pairs of (b[i], b[i+1])
    """
    n = len(b)
    return [(b[i], b[i+1]) for i in range(n-1)]

```