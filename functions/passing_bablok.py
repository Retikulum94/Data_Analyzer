# original version written by: https://github.com/Buhin-Mara/Passing-Bablok
# adapted and refactored

import numpy as np
import matplotlib.pyplot as plt
import statistics
import pandas as pd
from scipy import stats

def passing_bablok(x, y):
    """Calculate Passing-Bablok slope with confidence intervals"""
    N = len(x)
    ng_count = 0
    PB_list = []
    
    for i in range(N):
        for j in range(N):
            if i < j:
                slope = (y[i] - y[j]) / (x[i] - x[j])
                PB_list.append(slope)
                if slope < -1:
                    ng_count += 1
    
    shift = ng_count
    PB_list.sort()
    del PB_list[:shift]
    
    # Confidence interval calculation
    C_alpha = (1 - 0.95/2) * np.sqrt(N*(N-1)*(2*N+5)/18)
    N_PB_list = len(PB_list)
    M1 = int(round((N_PB_list - C_alpha) / 2))
    M2 = N_PB_list - M1 + 1
    
    PB_coef = statistics.median(PB_list)
    PB_upper = PB_list[M2] if M2 < len(PB_list) else PB_list[-1]
    PB_lower = PB_list[M1] if M1 >= 0 else PB_list[0]
    
    return PB_coef, PB_upper, PB_lower

def passing_bablok_intercept(xlist, ylist, slope):
    """Calculate Passing-Bablok intercept"""
    interceptlist = ylist - slope * xlist
    PB_intercept = statistics.median(interceptlist)
    return PB_intercept

def create_comparison_plot(x, y, x_label, y_label):
    """Create Least Square vs Passing-Bablok comparison plot"""
    # Least squares method
    m, b, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Passing-Bablok method
    m_PB, m_PB_upper, m_PB_lower = passing_bablok(x, y)
    b_PB = passing_bablok_intercept(x, y, m_PB)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, color="k", label="Data points")
    ax.plot([x.min(), x.max()], 
            [b + m*x.min(), b + m*x.max()],
            color="b", label=f"Least Square (slope: {m:.3f})")
    ax.plot([x.min(), x.max()], 
            [b_PB + m_PB*x.min(), b_PB + m_PB*x.max()],
            color="r", label=f"Passing-Bablok (slope: {m_PB:.3f}, CI: {m_PB_lower:.3f}-{m_PB_upper:.3f})")
    
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title("Least Square vs Passing-Bablok: Linear Regression")
    ax.legend()
    
    return fig