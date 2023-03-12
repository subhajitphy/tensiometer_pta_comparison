from tensiometer import mcmc_tension
import numpy as np
mcmc_tension.n_threads = 1
# create the distribution of the parameter differences:

def Diff_chain_kde_parameter_shift_2D_fft(A1,A2,off_size=None):
    
    input_arr=[A1,A2]
    
    if(off_size is None):
        off_size=5
        
    for i,chain in enumerate(input_arr):
        chain.chain_offsets =np.linspace(0,len(input_arr[i].samples[:,0]),off_size,dtype = int)
    
    diff_chain = mcmc_tension.parameter_diff_chain( A1, A2, boost=1)
    
    shift_probability, shift_lower, shift_upper = mcmc_tension.kde_parameter_shift_2D_fft(diff_chain, feedback=0)
    return diff_chain, shift_probability, shift_lower, shift_upper

