# main.py
import pandas as pd
from src.quality import aplicar_pipeline_calidad

def procesar_y_guardar(ruta_entrada: str, ruta_salida: str, config: dict):
    # Lectura del dato crudo (Read-Only)
    df_raw = pd.read_csv(ruta_entrada)
    
    # Transformación puramente funcional
    df_processed = aplicar_pipeline_calidad(df_raw, config['col_var'], config)
    
    # Escritura en capa procesada/versionable sin alterar el origen
    df_processed.to_csv(ruta_salida, index=False)
    print(f"✓ Salida versionable generada en: {ruta_salida}")