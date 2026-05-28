import streamlit as st
import pandas as pd
import numpy as np
from functions.bland_altman import create_bland_altman_plot, bland_altman_analysis, calculate_bias_percentage
from utils.data_manager import DataManager
st.markdown("""

<h1 style='text-align: center; margin-bottom: 0; font-size: 3.5rem;'>
Bland-Altman Analyse 📊 
</h1>
<h3 style='text-align: center; color: #6c757d; margin-top: 0;'>
Vergleich zweier Messmethoden

</h3>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.info("Laden Sie eine CSV-Datei mit Ihren Messwerten hoch. Die Analyse wird automatisch durchgeführt.")


st.markdown("<br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "CSV-Datei hochladen",
    type="csv",
    key="bland_altman_upload"
)
# Button zur Benutzeranleitung
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📚 Zur Benutzeranleitung", use_container_width=True):
        st.switch_page("views/Benutzeranleitung_1.py")


if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep=None, engine='python')
        st.success(f"Datei erfolgreich geladen! ({len(df)} Zeilen)")
        
        with st.expander("📋 Vorschau der Daten"):
            st.dataframe(df.head(10))
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) < 2:
            st.error(f"❌ Mindestens 2 numerische Spalten erforderlich. Gefunden: {len(numeric_cols)}")
        else:
            col1, col2 = st.columns(2)
            with col1:
                x_label = st.selectbox("Referenzmessung (X-Achse):", numeric_cols)
            with col2:
                y_label = st.selectbox("Testmessung (Y-Achse):", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)
            
            if x_label == y_label:
                st.warning("⚠️ Wähle zwei unterschiedliche Spalten!")
            else:
                x = np.array(df[x_label], dtype=float)
                y = np.array(df[y_label], dtype=float)
                
                mask = ~(np.isnan(x) | np.isnan(y))
                x = x[mask]
                y = y[mask]
                
                if len(x) < 2:
                    st.error("❌ Nicht genug Datenpunkte nach Entfernung von NaN-Werten")
                else:
                    st.subheader("📈 Bland-Altman Plot")
                    fig, analysis = create_bland_altman_plot(x, y, x_label, y_label)
                    st.pyplot(fig)

                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("💾 Zu switchdrive hochladen"):
                            dm = DataManager(fs_protocol='webdav', fs_root_folder='Data_Analyzer')
                            timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
                            filename = f"bland_altman_{timestamp}.png"
                            dm.save_plot(fig, filename)
                            st.success(f"✅ Plot gespeichert: {filename}")

                    with col2:
                        # Figure in PNG-Format konvertieren
                        import io
                        img_buffer = io.BytesIO()
                        fig.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
                        img_buffer.seek(0)
                        
                        timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
                        st.download_button(
                            label="⬇️ Download",
                            data=img_buffer,
                            file_name=f"bland_altman_{timestamp}.png",
                            mime="image/png"
                        )
                    
                    st.subheader("📊 Statistiken")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Anzahl Datenpunkte", analysis['n'])
                    with col2:
                        st.metric("Mittlere Differenz", f"{analysis['mean_diff']:.4f}")
                    with col3:
                        st.metric("Std. Abweichung", f"{analysis['std_diff']:.4f}")
                    
                    col4, col5, col6 = st.columns(3)
                    with col4:
                        st.metric("Obergrenze", f"{analysis['upper_limit']:.4f}")
                    with col5:
                        st.metric("Untergrenze", f"{analysis['lower_limit']:.4f}")
                    with col6:
                        agreement_range = analysis['agreement_range']
                        st.metric("Übereinstimmungsbereich", f"{agreement_range:.4f}")
                    
                    bias_pct = calculate_bias_percentage(x, y)
                    st.metric("Bias (%)", f"{bias_pct:.2f}%")
                    
                    st.subheader("💡 Interpretation")
                    st.info(f"""
                    **Mittlere Differenz:** {analysis['mean_diff']:.4f}  
                    Die durchschnittliche Abweichung zwischen den Messmethoden
                    
                    **Grenzen der Übereinstimmung:** [{analysis['lower_limit']:.4f}, {analysis['upper_limit']:.4f}]  
                    95% der Differenzen liegen innerhalb dieser Grenzen
                    
                    **Übereinstimmungsbereich:** {agreement_range:.4f}  
                    Größere Werte deuten auf schlechtere Übereinstimmung hin
                    """)
    
    except Exception as e:
        st.error(f"❌ Fehler beim Einlesen der Datei: {e}")