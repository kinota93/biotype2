from BaselineRemoval import BaselineRemoval
from scipy import signal

def find_peaks(y, cwt=False, smooth=False, baseline=False):
    """ returns a tuple of a peak list and the corresponding intensity list   
      peaks are extracted using cwt / prominence based algorithms
      with singal smoothing and/or baseline correction
    """
    window, deg = 15, 2     
    z = y
    if smooth:
        z = signal.savgol_filter(y, window, deg, deriv=0)

    if baseline:
        brm = BaselineRemoval(z)
        z = brm.ZhangFit(lambda_=400,repitition=15, porder=1)

    if cwt == True:
        peaks = signal.find_peaks_cwt(z, [20])  
    else:
        dist, prom = 100, 600
        peaks,_ = signal.find_peaks(z, distance=dist, prominence=prom)
    
    return peaks, z

def rank(pk):
    """returns a new dict with rank for each m/z value 
    """
    return {key: rank for rank, key in enumerate(sorted(pk, key=pk.get, reverse=True), 1)}

def align(pk1, pk2, delta = 3):
    """transform list of <m/z, intensity> to that of <peak_id, intensity>    
      assign an identical id to peaks whose m/z values are close enough (within `delta`) 
      returns: two dictionaries of <peak_id, intensity> 
    """
    dic_pk1 = dict(zip(pk1[0], pk1[1])) # a dict of {m/z: intensity} 
    dic_pk2 = dict(zip(pk2[0], pk2[1])) # a dict of {m/z: intensity} 

    n1, n2 = len(pk1[0]), len(pk2[0])               
    n = n1 + n2
    
    log_pk1 = list(zip(pk1[0], [0]*n1)) # a list of tuples (m/z, 0) 
    log_pk2 = list(zip(pk2[0], [1]*n2)) # a list of tuples (m/z, 1)
    log_pk1.extend(log_pk2)
    npk_sorted = sorted(log_pk1, key=lambda x: x[0])
        
    peak_id = 1
    npk = [dict(),  dict()]
    for i in range(n):
        m1, k1 = npk_sorted[i]
        if i < n - 1:
            m2, k2 = npk_sorted[i+1]
            if k1 != k2 and abs(m1-m2) <= delta:
                npk[k1][m1] = peak_id
                npk[k2][m2] = peak_id
                peak_id = peak_id + 1
        if m1 not in npk[k1].keys():
            npk[k1][m1] = peak_id
            peak_id = peak_id + 1
            
    npk0_swap = {peak_id: dic_pk1[mz] for mz, peak_id in npk[0].items()}
    npk1_swap = {peak_id: dic_pk2[mz] for mz, peak_id in npk[1].items()}

    return npk0_swap, npk1_swap
