import numpy as np
import pandas as pd
from datetime import datetime
import pytz
from scipy import stats


def passing_bablock_regression(method_x, method_y):
    """
    Calculate Passing-Bablock regression for comparing two measurement methods.
    
    The Passing-Bablock regression is a robust linear regression method that:
    - Does not require normally distributed data
    - Is resistant to outliers
    - Does not assume one method is the reference
    - Is suitable for method comparison studies
    
    Args:
        method_x (list or array): Measurements from method X
        method_y (list or array): Measurements from method Y (same length as method_x)
    
    Returns:
        dict: Dictionary containing:
            - slope: Slope of the regression line
            - intercept: Y-intercept
            - slope_ci: 95% confidence interval for slope [lower, upper]
            - intercept_ci: 95% confidence interval for intercept [lower, upper]
            - r_squared: Coefficient of determination
            - r_pearson: Pearson correlation coefficient
            - residuals: Residuals for each data point
            - mean_absolute_error: Mean absolute error
            - rmse: Root mean squared error
            - n: Number of data points
            - timestamp: Calculation timestamp
    """
    
    # Convert to numpy arrays
    x = np.asarray(method_x, dtype=float)
    y = np.asarray(method_y, dtype=float)
    
    # Validation
    if len(x) != len(y):
        raise ValueError("method_x and method_y must have the same length")
    
    if len(x) < 3:
        raise ValueError("At least 3 data points are required for Passing-Bablock regression")
    
    if np.any(np.isnan(x)) or np.any(np.isnan(y)):
        raise ValueError("Data contains NaN values")
    
    n = len(x)
    
    # Calculate differences and sums
    diff = y - x  # d_i
    sum_xy = x + y  # s_i
    
    # Calculate slope using median method (robust against outliers)
    # Slope = median((y_i - y_j) / (x_i - x_j)) for all i > j
    slopes = []
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] != x[j]:
                slope_ij = (y[i] - y[j]) / (x[i] - x[j])
                slopes.append(slope_ij)
    
    slope = np.median(slopes)
    
    # Calculate intercept
    intercept = np.median(diff - slope * x)
    
    # Calculate fitted values
    y_fitted = slope * x + intercept
    
    # Calculate residuals
    residuals = y - y_fitted
    
    # Calculate R-squared
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
    
    # Calculate Pearson correlation
    r_pearson, p_value = stats.pearsonr(x, y)
    
    # Calculate standard error for confidence intervals
    se_residuals = np.sqrt(ss_res / (n - 2))
    
    # Confidence intervals (95%)
    sxx = np.sum((x - np.mean(x)) ** 2)
    se_slope = se_residuals / np.sqrt(sxx) * np.sqrt(n / (n - 2))
    t_critical = stats.t.ppf(0.975, n - 2)  # 95% CI
    
    slope_ci = [slope - t_critical * se_slope, slope + t_critical * se_slope]
    
    se_intercept = se_residuals * np.sqrt(1/n + np.mean(x)**2 / sxx) * np.sqrt(n / (n - 2))
    intercept_ci = [intercept - t_critical * se_intercept, intercept + t_critical * se_intercept]
    
    # Error metrics
    mae = np.mean(np.abs(residuals))
    rmse = np.sqrt(np.mean(residuals ** 2))
    
    return {
        "slope": round(slope, 6),
        "intercept": round(intercept, 6),
        "slope_ci": [round(slope_ci[0], 6), round(slope_ci[1], 6)],
        "intercept_ci": [round(intercept_ci[0], 6), round(intercept_ci[1], 6)],
        "r_squared": round(r_squared, 6),
        "r_pearson": round(r_pearson, 6),
        "p_value": round(p_value, 6),
        "residuals": [round(r, 6) for r in residuals],
        "mean_absolute_error": round(mae, 6),
        "rmse": round(rmse, 6),
        "n": n,
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
    }


def compare_methods(method_x_data, method_y_data, method_x_name="Method X", method_y_name="Method Y"):
    """
    Compare two measurement methods using Passing-Bablock regression.
    
    Args:
        method_x_data (list or array): Measurements from first method
        method_y_data (list or array): Measurements from second method
        method_x_name (str): Name of first method
        method_y_name (str): Name of second method
    
    Returns:
        dict: Comparison results including regression parameters and statistics
    """
    
    results = passing_bablock_regression(method_x_data, method_y_data)
    
    # Add interpretation hints
    results["method_x_name"] = method_x_name
    results["method_y_name"] = method_y_name
    results["equation"] = f"{method_y_name} = {results['slope']} × {method_x_name} + {results['intercept']}"
    results["agreement"] = "Good" if abs(results['slope'] - 1.0) < 0.1 and abs(results['intercept']) < 0.1 else "Fair"
    
    return results


def generate_bland_altman_data(method_x, method_y):
    """
    Generate data points for Bland-Altman plot.
    
    Args:
        method_x (list or array): Measurements from method X
        method_y (list or array): Measurements from method Y
    
    Returns:
        DataFrame: Data with means, differences, and limits of agreement
    """
    
    x = np.asarray(method_x, dtype=float)
    y = np.asarray(method_y, dtype=float)
    
    df = pd.DataFrame({
        'mean': (x + y) / 2,
        'difference': y - x,
    })
    
    mean_diff = df['difference'].mean()
    std_diff = df['difference'].std()
    
    df['loa_upper'] = mean_diff + 1.96 * std_diff
    df['loa_lower'] = mean_diff - 1.96 * std_diff
    df['mean_diff'] = mean_diff
    
    return df
    