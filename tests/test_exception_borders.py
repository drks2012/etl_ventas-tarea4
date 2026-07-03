import pytest, pandas as pd
from src.transform import limpiar_ventas
 
def test_falla_sin_columna_monto():
    df = pd.DataFrame({'Producto': ['A']})    # falta 'Monto'
    with pytest.raises(KeyError):
        limpiar_ventas(df)
 
def test_dataframe_vacio():
    df = pd.DataFrame({'Producto': [], 'Monto': []})
    out = limpiar_ventas(df)
    assert len(out) == 0          # no rompe, devuelve vacío
 
def test_todos_invalidos():
    df = pd.DataFrame({'Producto': [None], 'Monto': [-1.0]})
    assert len(limpiar_ventas(df)) == 0
