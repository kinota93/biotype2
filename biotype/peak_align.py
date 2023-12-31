import statistics as st
import heapq
import itertools

""""Peak Alignment
 algorithm 1 (divide): divide list into clusters where gap > delta, repeat on step=1,2,...
 algorithm 2 (linear_join): join leftmost neighbors to clusters when diameter < epsilon
 algorithm 3 (best_join): join closest neighbors to clusters when diameter < epsilon
Parameters
 sorted_uniques: a list of floats sorted in ascending order
 delta: reject threshold, neighbors with a gap wider than delta will be rejected to join a cluster
 epsilon: accept threshold, neighbors close enough within epsilon will be accepted to a cluster
""""    

def pairwise(iterable):
    """ generate pair of consequent items   
      [s0,s1,s2,s3] -> [(s0, s1), (s1, s2), (s2, s3)]
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a,b)


def evaluate(bins):
    """evaluate algorithms  
    (1) average variance, smaller is better
    (2) average gap, larger is better 
    """
    vmin = min([min(a) for a in bins])
    vmax = max([max(a) for a in bins])
    gap = sum([abs(min(b)-max(a)) for a,b in pairwise(bins)])/(vmax-vmin)
    dev = st.mean([st.pstdev(b) for b in bins])
    return gap, dev

def grouper(iterable, delta=5):
    """ Partition `iterable` into groups whose diameters no larger than delta --> Not Used. 
    numbers = [123, 124, 128, 160, 167, 213, 215, 230, 245, 255, 257, 400, 401, 402, 430]
    dict(enumerate(grouper(numbers, 15), 1))

    Output:
    {1: [123, 124, 128],
     2: [160, 167],
     3: [213, 215],
     4: [230, 245],
     5: [255, 257],
     6: [400, 401, 402],
     7: [430]}
    """
    low = None
    group = []
    for item in iterable:
        if low is None or item - low <= delta:
            group.append(item)
            if low is None:
                low = item
        else:
            yield group
            group = [item]
            low = item
    if group:
        yield group
        
def divide(sorted_uniques, delta=3):
    """algorithm 1 (divide): divide list into clusters where gap > delta, w.r.t. step=1, 2, ...
    input: a list of sortd unique m/z values, [1000.230, 1001.172,1007.401,...]
    ouput: list of m/z value lists, each m/z value list is a cluster, 
       [[1000.230, 1001.172],[1007.401,...],...] 
    """
    bins =[sorted_uniques]
    done, step = False, 1
    while not done:
        new_bins = []
        done = True
        for b in bins: # divide each bin if necessary
            s = 0
            for i in range(0, len(b)-1, step):
                j = i + step
                if j<len(b) and b[j] - b[i] > delta:
                    new_bins += [b[s:j]]
                    s, done = j, False
            
            if s < len(b): # add last part as a new bin
                new_bins += [b[s:]]
                
        bins = new_bins[:] 
        step += 1
        
    return bins 


def linear_join(sorted_uniques, delta=5, epsilon=2):
    """algorithm 2 (linear_join): join leftmost neighbors to a cluster when diameter < epsilon
    input: a list of sortd unique m/z values, [1000.230, 1001.172,1007.401,...]
    ouput: list of m/z value lists, each m/z value list is a cluster, 
       [[1000.230, 1001.172],[1007.401,...],...] 
    """
    bins = [[v] for v in sorted_uniques]
    
    for d in reversed(range(11)):
        new_bins = []
        i, e = 0, epsilon/2**d # epsilon x 1/1024,1/512, ..., 1/2, 1.0 
        while i < len(bins):
            if i == len(bins)-1:
                new_bins += [bins[i]]
                break

            a, b = bins[i], bins[i+1]
            if max(b) - min(a) < e: # diameter(a, b)< e
                new_bins += [a+b] 
                i += 2
            else:
                new_bins += [a]
                i += 1
            
        bins = new_bins[:]
        
    return bins


def best_join(sorted_uniques, delta=5, epsilon=2): 
    """algorithm 3 (best_join): reccurisively join nearest neighbors when diameter < epsilon
    input: a list of sortd unique m/z values, e.g., [1000.230, 1001.172,1007.401,...]
    ouput: list of m/z value lists, each m/z value list is a cluster, e.g.,
       [[1000.230, 1001.172],[1007.401,...],...] 
    """
    # 1. separate values to groups with gap wider than delta
    
    bins = [-1, len(sorted_uniques)-1] # a bin is an open-closed interval
    for s, t in pairwise(bins):  # (s,t] = [s+1,t]
        for i in range(s+1, t):
            if sorted_uniques [i+1] - sorted_uniques [i] > delta:
                bins += [i]
                    
    bins = sorted(list(set(bins))) # 1-step divided list
    
    #2. for each group, starting with the nearest single values, join neighbors to cluster
    
    my_bins = []
    for s, t in pairwise(bins): 
        new_bins = []
        my_bin = [[v] for v in sorted_uniques[s+1:t+1]]

        done = False
        while not done:
            n = len(my_bin)
            alpha  = lambda x: round(max(my_bin[x+1])-min(my_bin[x]),3)
            pq = [(alpha(x), x) for x in range(n-1) if alpha(x)<epsilon]
            if bool(pq): 
                heapq.heapify(pq)
                d, x= heapq.heappop(pq)
                my_bin = my_bin[:x] + [my_bin[x]+my_bin[x+1]] + my_bin[x+2:]
            else:
                new_bins += my_bin
                done = True
        
        my_bins += new_bins
        
    return sorted(my_bins, key=lambda x: x[0])
