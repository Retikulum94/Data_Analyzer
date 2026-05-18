# Bland-Altman Plot Generator
# Verwendet zur Bewertung der Übereinstimmung zwischen zwei Messmethoden

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

def bland_altman_analysis(x, y):
    """
    Berechnet Bland-Altman Metriken
    
    Args:
        x: Referenzmessung (Array)
        y: Testmessung (Array)
    
    Returns:
        dict mit mean_diff, std_diff, upper_limit, lower_limit
    """
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    difference = y - x
    mean_diff = np.mean(difference)
    std_diff = np.std(difference, ddof=1)
    
    # Grenzen der Übereinstimmung (Limits of Agreement)
    # Standard: ±1.96 * std_diff
    upper_limit = mean_diff + 1.96 * std_diff
    lower_limit = mean_diff - 1.96 * std_diff
    
    # Konfidenzintervall für die Differenzen
    n = len(difference)
    se_diff = std_diff / np.sqrt(n)
    ci_margin = 1.96 * se_diff
    
    results = {
        'mean_diff': mean_diff,
        'std_diff': std_diff,
        'upper_limit': upper_limit,
        'lower_limit': lower_limit,
        'ci_upper': mean_diff + ci_margin,
        'ci_lower': mean_diff - ci_margin,
        'agreement_range': upper_limit - lower_limit,
        'n': n
    }
    
    return results

def calculate_bias_percentage(x, y):
    """Berechnet die prozentuale Abweichung (Bias) zwischen Methoden"""
    difference = y - x
    mean_x = np.mean(x)
    bias_percent = (np.mean(difference) / mean_x) * 100
    return bias_percent

def create_bland_altman_plot(x, y, x_label, y_label):
    """
    Erstellt Bland-Altman Plot mit Grenzen der Übereinstimmung
    
    Args:
        x: Referenzmessung
        y: Testmessung
        x_label: Label für X-Achse
        y_label: Label für Y-Achse
    
    Returns:
        matplotlib figure
    """
    # Berechnung
    mean_x = (x + y) / 2
    difference = y - x
    
    analysis = bland_altman_analysis(x, y)
    mean_diff = analysis['mean_diff']
    upper_limit = analysis['upper_limit']
    lower_limit = analysis['lower_limit']
    
    # Plot erstellen
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Datenpunkte
    ax.scatter(mean_x, difference, alpha=0.6, s=50, color='navy', label='Differenzen')
    
    # Mittellinie
    ax.axhline(mean_diff, color='red', linestyle='-', linewidth=2, label=f'Mittlere Differenz: {mean_diff:.3f}')
    
    # Grenzen der Übereinstimmung
    ax.axhline(upper_limit, color='green', linestyle='--', linewidth=1.5, 
               label=f'Obergrenze: {upper_limit:.3f}')
    ax.axhline(lower_limit, color='green', linestyle='--', linewidth=1.5, 
               label=f'Untergrenze: {lower_limit:.3f}')
    
    # Konfidenzintervalle (optional - gefüllt)
    ax.fill_between(ax.get_xlim(), 
                     analysis['ci_lower'], 
                     analysis['ci_upper'],
                     alpha=0.1, color='red', label='95% CI der Mittlinie')
    
    ax.set_xlabel(f'Mittelwert ({x_label} + {y_label})/2')
    ax.set_ylabel(f'Differenz ({y_label} - {x_label})')
    ax.set_title('Bland-Altman Plot: Übereinstimmung zwischen zwei Messmethoden')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
    return fig, analysis