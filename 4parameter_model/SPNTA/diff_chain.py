import tensiometer
from tensiometer import mcmc_tension
import numpy as np
mcmc_tension.n_threads = 1
# create the distribution of the parameter differences:
from tensorflow.keras.callbacks import ReduceLROnPlateau

def Diff_chain_shift(A1,A2,off_size=None,MLinfo=None,boost=None,method=None):
    
    input_arr=[A1,A2]

    if(off_size is None):
        off_size=5
    if(boost is None):
        boost=4
        
    for i,chain in enumerate(input_arr):
        chain.chain_offsets =np.linspace(0,len(input_arr[i].samples[:,0]),off_size,dtype = int)
    diff_chain = mcmc_tension.parameter_diff_chain( A1, A2, boost=boost)
    
    if len(A1.getMeans())<=2 and method==None:
        shift_probability, shift_lower, shift_upper = mcmc_tension.kde_parameter_shift_2D_fft(diff_chain, feedback=0)
        return diff_chain, shift_probability, shift_lower, shift_upper
    
    if method=='ML' or len(A1.getMeans())>2:
        
        if(MLinfo is None):
            batch_size = 8192
            epochs = 50
            steps_per_epoch = 64
            MLinfo=[batch_size,epochs,steps_per_epoch]
        diff_flow_callback = tensiometer.mcmc_tension.DiffFlowCallback(diff_chain, feedback=1, learning_rate=0.01)
        
        callbacks = [ReduceLROnPlateau()]

        diff_flow_callback.train(batch_size=MLinfo[0], epochs=MLinfo[1], steps_per_epoch=MLinfo[2], callbacks=callbacks)


        exact_shift_P_1, exact_shift_low_1, exact_shift_hi_1 = diff_flow_callback.estimate_shift()
        
        return diff_chain, exact_shift_P_1, exact_shift_low_1, exact_shift_hi_1
        
        
        
        
    



