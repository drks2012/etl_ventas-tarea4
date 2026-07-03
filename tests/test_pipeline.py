# tests/test_pipeline.py
import subprocess, sys, pandas as pd, pytest
 
@pytest.mark.integracion
def test_pipeline_genera_csv(tmp_path):
    salida = tmp_path / 'ventas_limpias.csv'
    cmd = [sys.executable, 'run_pipeline.py',
           '--input', 'data/ventas.csv',
           '--output', str(salida)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert salida.exists()
    df = pd.read_csv(salida)
    assert len(df) == 3 and df['monto'].gt(0).all()