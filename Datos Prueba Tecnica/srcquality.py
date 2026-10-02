import numpy as np
import pandas as pd

def evaluar_rango_fisico(df: pd.DataFrame, columna: str, min_val: float, max_val: float) -> pd.Series:
    """Retorna Serie booleana donde True indica que el valor viola los límites físicos."""
    return (df[columna] < min_val) | (df[columna] > max_val)

def evaluar_persistencia(df: pd.DataFrame, columna: str, limite_consecutivos: int = 6) -> pd.Series:
    """Detecta valores congelados/pegados por fallas del sensor."""
    s = df[columna]
    es_igual = s.groupby((s != s.shift()).cumsum()).transform('size')
    # Excluye ceros (común en precipitación)
    return (es_igual >= limite_consecutivos) & (s != 0) & (~s.isna())

def aplicar_pipeline_calidad(df: pd.DataFrame, columna: str, config: dict) -> pd.DataFrame:
    """Aplica reglas deterministas sin modificar el conjunto de datos crudo."""
    df_out = df.copy()
    
    flag_rango = evaluar_rango_fisico(df_out, columna, config['min'], config['max'])
    flag_pers = evaluar_persistencia(df_out, columna, config['persistencia'])
    
    df_out['flag_rango'] = flag_rango
    df_out['flag_persistencia'] = flag_pers
    df_out['flag_anomalo'] = flag_rango | flag_pers
    
    return df_out