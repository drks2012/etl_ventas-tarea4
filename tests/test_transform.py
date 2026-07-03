# tests/test_transform.py
from src.transform import limpiar_ventas
 
def test_quita_nulos(df_crudo):
    out = limpiar_ventas(df_crudo)
    assert out['producto'].notna().all()
 
def test_quita_negativos(df_crudo):
    out = limpiar_ventas(df_crudo)
    assert out['monto'].gt(0).all()
 
def test_quita_duplicados(df_crudo):
    out = limpiar_ventas(df_crudo)
    assert not out.duplicated().any()
 
def test_normaliza_columnas(df_crudo):
    assert list(limpiar_ventas(df_crudo).columns) == ['producto','monto']
