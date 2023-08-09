import math
import biotype.peak_extract as pke

def score(pk1, pk2, delta=3, method='jaccard', rank=5):
    """ Compute similarity score between two peak arrays. 
        @params: pk1, pk2,  peak lists of <m/z, intensity>
        method: jaccard/rank/weighted for Jaccard/Rank/Weighted Rank Similarity
    """
    npk1, npk2 = pke.align(pk1, pk2, delta) # <peak_id, intensity>
    common = npk1.keys() & npk2.keys()
    union  = npk1.keys() | npk2.keys()
    n_common, n_union = len(common), len(union)
        
    rpk1, rpk2 = pke.rank(npk1), pke.rank(npk2)
    good_peak = lambda x: abs(rpk1[x]-rpk2[x]) < rank
    if method == 'rank':
        good_common = [good_peak(k) for k in common] 
        return sum(good_common)/float(n_union) 

    if method == 'weighted':
        weight = lambda r: math.exp(-r/25)
        # weight = lambda r: 1/float(r)
        good_common = [0.1+weight(rpk1[k])+weight(rpk2[k]) for k in common if good_peak(k)] 
        return sum(good_common)/len(union)

    # Jaccard        
    return n_common / float(n_union) 

"""cf. https://en.wikipedia.org/wiki/Rank_correlation
"""