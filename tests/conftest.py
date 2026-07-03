# tests/conftest.py
import pytest
import pandas as pd
 
@pytest.fixture
def df_crudo():
    """Ventas con un duplicado, un nulo y un negativo."""
    return pd.DataFrame({
        'Producto': ['Laptop', 'Laptop', None, 'Teclado', 'Mouse'],
        'Monto':    [2500.0,   2500.0,   45.5,  -50.0,     45.5],
    })
 
@pytest.fixture
def df_limpio(df_crudo):
    from src.transform import limpiar_ventas
    return limpiar_ventas(df_crudo)