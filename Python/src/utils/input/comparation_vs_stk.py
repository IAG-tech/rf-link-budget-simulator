import pandas as pd



def comparation_vs_stk():
    # Leer saltando filas problemáticas
    df = pd.read_csv(r'D:\STK\LEO_VLEO_Analysis\Facility-Facility1-To-Satellite-Satellite1_AER.csv',
                 skiprows=1,  # saltar cabecera original
                 names=['time', 'azimuth', 'elevation', 'range'],on_bad_lines='skip')

    # Filtrar solo filas con datos reales — las que tienen fecha en time
    df = df[df['time'].str.startswith('26 May') | df['time'].str.startswith('27 May')]

    # Convertir elevation y range a numérico
    df['elevation'] = pd.to_numeric(df['elevation'], errors='coerce')
    df['range'] = pd.to_numeric(df['range'], errors='coerce')

    # Eliminar NaN
    df = df.dropna()

    # Convertir time a datetime
    df['time'] = pd.to_datetime(df['time'], format='%d %b %Y %H:%M:%S.%f')

    # Separar pasos — hay un gap de más de 1 hora entre ellos
    df['gap'] = df['time'].diff() > pd.Timedelta(minutes=10)
    df['pass_id'] = df['gap'].cumsum()



    pass2 = df[df['pass_id'] == 1].copy()
    t_stk = (pass2['time'] - pass2['time'].iloc[0]).dt.total_seconds()
    el_stk = pass2['elevation'].values



    return t_stk, el_stk