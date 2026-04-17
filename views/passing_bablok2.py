import streamlit as st
import pandas as pd
import numpy as np
from functions.passing_bablok import create_comparison_plot

st.set_page_config(page_title="Passing-Bablok Analyzer", layout="wide")

st.title("📊 Passing-Bablok Analyzer")
st.markdown("Vergleich von Least-Square und Passing-Bablok Methoden für lineare Regression")

# CSV Upload
uploaded_file = st.file_uploader("CSV-Datei hochladen", type="csv")

if uploaded_file is not None:
    # Read CSV
    try:
        df = pd.read_csv(uploaded_file, sep=None, engine='python')
        st.success(f"✅ Datei geladen! ({len(df)} Zeilen)")
        
        # Display preview
        with st.expander("📋 Vorschau der Daten"):
            st.dataframe(df.head(10))
        
        # Find numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) < 2:
            st.error(f"❌ Mindestens 2 numerische Spalten erforderlich. Gefunden: {len(numeric_cols)}")
        else:
            # Column selection
            col1, col2 = st.columns(2)
            with col1:
                x_label = st.selectbox("X-Achse (Referenz):", numeric_cols)
            with col2:
                y_label = st.selectbox("Y-Achse (Test):", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
            
            if x_label == y_label:
                st.warning("⚠️ Wähle zwei unterschiedliche Spalten!")
            else:
                x = np.array(df[x_label], dtype=float)
                y = np.array(df[y_label], dtype=float)
                
                # Remove NaN values
                mask = ~(np.isnan(x) | np.isnan(y))
                x = x[mask]
                y = y[mask]
                
                if len(x) < 2:
                    st.error("❌ Nicht genug Datenpunkte nach Entfernung von NaN-Werten")
                else:
                    # Create and display plot
                    st.subheader("📈 Vergleich der Regressionsmethoden")
                    fig = create_comparison_plot(x, y, x_label, y_label)
                    st.pyplot(fig)
                    
                    # Display statistics
                    st.subheader("📊 Statistiken")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Anzahl Datenpunkte", len(x))
                    with col2:
                        st.metric("Korrelation", f"{np.corrcoef(x, y)[0, 1]:.3f}")
    
    except Exception as e:
        st.error(f"❌ Fehler beim Einlesen der Datei: {e}")
else:
    st.info("👆 Bitte lade eine CSV-Datei hoch um zu starten")