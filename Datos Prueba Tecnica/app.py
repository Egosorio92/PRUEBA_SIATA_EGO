import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="SIATA - Monitoreo y Calidad de Datos",
    page_icon="🌊",
    layout="wide"
)

# ==========================================
# F6. TRANSPARENCIA Y BARRA LATERAL
# ==========================================
st.sidebar.title("⚙️ Configuración y Filtros")
estacion_sel = st.sidebar.selectbox("Seleccionar Estación", ["Nivel 803", "Piranómetro 6004", "Pluviométrica 35", "Meteorológica 367"])
variable_sel = st.sidebar.selectbox("Seleccionar Variable", ["Nivel (m)", "Radiación (W/m²)", "Lluvia (mm)", "Temperatura (°C)"])
rango_fechas = st.sidebar.date_input("Rango de Fechas", [pd.to_datetime("2025-12-01"), pd.to_datetime("2026-04-30")])

st.sidebar.markdown("---")
with st.sidebar.expander("ℹ️ F6. Transparencia y Fuente"):
    st.write("**Fuente:** Red de Monitoreo SIATA")
    st.write("**Última actualización:** 2026-04-30")
    st.write("**Unidades:** Nivel (m), Radiación (W/m²), Lluvia (mm)")
    st.write("**Banderas de Calidad:** 0: Válido, 1: Dudoso, 2: Anómalo, 3: Faltante, 4: Extremo Validado")
    st.write("**Limitaciones:** Datos de sensores sujetos a pérdidas puntuales de telemetría.")

# ==========================================
# TÍTULO Y NAVEGACIÓN (TABS)
# ==========================================
st.title("🌊 Dashboard de Calidad y Monitoreo de Datos - SIATA")
st.caption("Herramienta interactiva para exploración de salud de red, anomalías y pronósticos")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎨 F1. Wireframe / Boceto", 
    "🩺 F2. Salud de la Red", 
    "📈 F3. Series y Pronóstico", 
    "🚨 F4. Registro de Anomalías", 
    "🔗 F5. Relaciones y Lags"
])

# ==========================================
# F1. BOCETO PREVIO (WIREFRAME Y AUDIENCIA)
# ==========================================
with tab1:
    st.header("F1. Boceto Previo (Wireframe) y Criterios de Diseño")
    st.markdown("""
    * **Audiencia Objetivo:** Operadores del SAT, analistas ambientales y personal no técnico de toma de decisiones.
    * **Preguntas Clave que responde:**
      1. ¿Qué porcentaje de datos confiables transmitió cada estación hoy? (Semáforo de Red)
      2. ¿Existen eventos extremos o fallas de sensor en el periodo de tiempo analizado?
      3. ¿Cuál es el pronóstico a 24 horas y su margen de incertidumbre?
    """)
    st.info("💡 **Jerarquía Visual:** Semáforos e KPIs en la parte superior ➔ Exploración temporal detallada en el centro ➔ Tabla de decisiones/anomalías al final.")

# ==========================================
# F2. VISTA DE SALUD DE LA RED (INDICADORES Y SEMÁFORO)
# ==========================================
with tab2:
    st.header("F2. Vista de Salud de la Red (KPIs y Semáforo de Calidad)")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Completitud Temporal", "98.2%", "+0.5%", delta_color="normal")
    col2.metric("Proporción Datos Válidos", "94.5%", "-1.2%", delta_color="inverse")
    col3.metric("Tasa de Disponibilidad (Uptime)", "99.1%", "0.0%")
    col4.metric("Total Anomalías Activas", "14", "-3", delta_color="normal")
    
    st.subheader("Estado General por Estación")
    
    # Tabla de Salud con Semáforo
    df_salud = pd.DataFrame({
        "Estación": ["Nivel 803", "Piranómetro 6004", "Pluviométrica 35", "Meteorológica 367"],
        "Completitud (%)": [98.5, 99.1, 95.2, 98.0],
        "Datos Válidos (%)": [96.0, 92.1, 91.0, 97.5],
        "Frecuencia Muestreo": ["15 min", "1 min", "Evento", "10 min"],
        "Estado Semáforo": ["🟢 Normal", "🟡 Revisión (Picos)", "🟢 Normal", "🟢 Normal"]
    })
    
    st.dataframe(df_salud, use_container_width=True)

# ==========================================
# F3. VISTA DE SERIES DE TIEMPO Y PRONÓSTICO
# ==========================================
with tab3:
    st.header(f"F3. Serie de Tiempo e Incertidumbre: {variable_sel} ({estacion_sel})")
    
    # Generar datos simulados representativos para el dashboard
    fechas = pd.date_range("2026-04-01", "2026-04-07", freq="1h")
    np.random.seed(42)
    valores = 10 + np.sin(np.linspace(0, 10, len(fechas))) * 3 + np.random.normal(0, 0.5, len(fechas))
    
    # Introducir una anomalía simulada y un hueco
    valores[20] = 22.0 # Pico/Anomalía
    valores[50:55] = np.nan # Hueco
    
    df_ts = pd.DataFrame({"Fecha": fechas, "Valor": valores})
    
    fig = go.Figure()
    # Serie Principal
    fig.add_trace(go.Scatter(x=df_ts["Fecha"], y=df_ts["Valor"], mode='lines', name='Medición Real', line=dict(color='#1f77b4')))
    
    # Anomalía detectada
    fig.add_trace(go.Scatter(x=[df_ts["Fecha"].iloc[20]], y=[df_ts["Valor"].iloc[20]], mode='markers', name='Anomalía Detectada', marker=dict(color='red', size=12, symbol='x')))
    
    # Pronóstico futuro con intervalo de incertidumbre (Sombra)
    fechas_fut = pd.date_range("2026-04-07 01:00", "2026-04-08", freq="1h")
    y_pred = 10 + np.sin(np.linspace(10, 12, len(fechas_fut))) * 3
    y_lower = y_pred - 1.5
    y_upper = y_pred + 1.5
    
    fig.add_trace(go.Scatter(x=fechas_fut, y=y_pred, mode='lines', name='Pronóstico SARIMA', line=dict(color='orange', dash='dash')))
    fig.add_trace(go.Scatter(x=np.concatenate([fechas_fut, fechas_fut[::-1]]), 
                             y=np.concatenate([y_upper, y_lower[::-1]]),
                             fill='toself', fillcolor='rgba(255, 165, 0, 0.2)',
                             line=dict(color='rgba(255,255,255,0)'), name='Incertidumbre (IC 95%)'))
    
    fig.update_layout(template="plotly_white", xaxis_title="Fecha y Hora", yaxis_title=variable_sel, height=450)
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# F4. VISTA DE ANOMALÍAS
# ==========================================
with tab4:
    st.header("F4. Registro Filtrable de Anomalías Detectadas")
    
    df_anom = pd.DataFrame({
        "Fecha/Hora": ["2026-04-02 08:00", "2026-04-03 14:15", "2026-04-05 03:00", "2026-04-06 18:30"],
        "Estación": ["Piranómetro 6004", "Nivel 803", "Meteorológica 367", "Pluviométrica 35"],
        "Tipo de Evento": ["Falla de Sensor", "Evento Físico Real (Creciente)", "Falla de Comunicación", "Problema de Configuración"],
        "Regla / Modelo": ["Rango Físico (< 0 W/m²)", "Coherencia Lluvia-Nivel", "Persistencia / Gap", "Isolation Forest"],
        "Severidad": ["Alta", "Crítica (SAT)", "Media", "Baja"]
    })
    
    sev_filter = st.multiselect("Filtrar por Severidad:", ["Crítica (SAT)", "Alta", "Media", "Baja"], default=["Crítica (SAT)", "Alta", "Media", "Baja"])
    df_filtered = df_anom[df_anom["Severidad"].isin(sev_filter)]
    
    st.dataframe(df_filtered, use_container_width=True)

# ==========================================
# F5. VISTA DE RELACIONES Y CORRELACIÓN CRUZADA
# ==========================================
with tab5:
    st.header("F5. Análisis de Relaciones y Correlación Cruzada con Lags")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("Matriz de Correlación (Desestacionalizada STL)")
        corr_data = np.array([[1.0, -0.15, 0.65], [-0.15, 1.0, -0.42], [0.65, -0.42, 1.0]])
        fig_cm = px.imshow(corr_data, x=['Lluvia', 'Radiación', 'Nivel'], y=['Lluvia', 'Radiación', 'Nivel'], text_auto=True, color_continuous_scale='Blues')
        st.plotly_chart(fig_cm, use_container_width=True)
        
    with col_b:
        st.subheader("Correlación Cruzada (Lluvia vs Nivel por Lag)")
        lags = list(range(-6, 7))
        corrs = [0.05, 0.1, 0.12, 0.25, 0.58, 0.82, 0.61, 0.40, 0.22, 0.15, 0.08, 0.05, 0.02]
        fig_stem = px.bar(x=lags, y=corrs, labels={'x': 'Lag (Horas)', 'y': 'Correlación Pearson'})
        fig_stem.add_vline(x=1, line_dash="dash", line_color="red", annotation_text="Lag Óptimo (+1h)")
        st.plotly_chart(fig_stem, use_container_width=True)