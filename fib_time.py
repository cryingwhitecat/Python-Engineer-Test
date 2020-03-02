import matplotlib.pyplot as plt
import time 
from log_fib import log_fib
from linear_fib import linear_fib
from recursive_fib import recursive_fib

def fib_func_time_measurement(fib_func, n=41, step=1):
    n_th_fibonacci, index_list, time_stat = [], [], []
    for i in range(0, n, step):
        time_start = time.time()
        fib_number = fib_func(i)
        time_end = time.time()
        n_th_fibonacci = fib_number
        index_list.append(i)
        time_stat.append((time_end - time_start) * 1000)
    return n_th_fibonacci, index_list, time_stat
    
n_th_fibonacci_rec, index_list_rec, time_stat_rec = fib_func_time_measurement(recursive_fib, 35, 1)   
n_th_fibonacci_lin, index_list_lin, time_stat_lin = fib_func_time_measurement(linear_fib, 380001, 20000)
n_th_fibonacci_log, index_list_log, time_stat_log = fib_func_time_measurement(log_fib, 380001, 20000)


plt.figure(figsize=(14, 4))
plt.plot(index_list_rec, time_stat_rec, color='red', label='recursion_fib')
plt.plot(index_list_lin, time_stat_lin, color='green', label='linear_fib')
plt.plot(index_list_log, time_stat_log, color='blue', label='logarithmic_fib')

plt.legend()

plt.xlabel('n-th fibonacci number')
plt.ylabel('time, ms')

plt.grid(True, which='both')
plt.show()