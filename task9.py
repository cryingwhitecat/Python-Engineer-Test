import math
#all abbreviations and symbols are laid out in the report
def calculate_probability(plt,plc,length_start,length_end,bl_threshold):
    
    assert length_end > length_start, "length_start has to be smaller than length_end"
    assert bl_threshold >0, "blacklisting threshold has to be greater than 0"
    assert plt>0,"probability of correctly guessing a letter has to be greater than 0"
    assert plc>0,"probability of correctly guessing a word`s length has to be greater than 0"

    plength = 1/(length_end - length_start + 1)
    psum = 0
    for i in range(length_start,length_end+1):
        temp = plc * pow(plt,i)
        psum+=temp
    ps1 = plength*psum
    ps2 = ps1**2
    pf = 1- ps2
    pb = pow(pf,bl_threshold + 1) 
    return pb
if __name__ == "__main__":
    p = calculate_probability(0.98,0.93,5,10,5)
    print(p)