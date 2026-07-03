import pytest
from src.transform import total_por_producto, limpiar_ventas
 
@pytest.mark.parametrize('producto, total_esperado', [
    ('Laptop', 2500.0),    # duplicado colapsa a una venta
    ('Mouse',  45.5),
])
def test_total_por_producto(df_crudo, producto, total_esperado):
    tot = total_por_producto(limpiar_ventas(df_crudo))
    valor = tot.loc[tot['producto'] == producto, 'total'].iloc[0]
    assert valor == pytest.approx(total_esperado)
