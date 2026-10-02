import pytest
import pandas as pd
import numpy as np
from src.quality import evaluar_rango_fisico, evaluar_persistencia

def test_evaluar_rango_fisico():
    df = pd.DataFrame({'radiacion': [-10.0, 0.0, 500.0, 1500.0]})
    # Límites físicos para radiación solar: [0, 1200]
    resultado = evaluar_rango_fisico(df, 'radiacion', 0.0, 1200.0)
    
    # -10 y 1500 deben ser marcados como True (anómalos)
    assert list(resultado) == [True, False, False, True]

def test_evaluar_persistencia():
    # Serie con 6 valores congelados consecutivos (25.0)
    df = pd.DataFrame({'temperatura': [20.0, 25.0, 25.0, 25.0, 25.0, 25.0, 25.0, 21.0]})
    resultado = evaluar_persistencia(df, 'temperatura', limite_consecutivos=6)
    
    # Los índices 1 al 6 deben ser marcados como congelados
    assert resultado.sum() == 6