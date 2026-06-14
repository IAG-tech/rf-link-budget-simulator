import pandas as pd
def comparation_vs_stk():
    """
       Loads and processes STK AER report for Facility1-to-Satellite1 access.

       Reads the exported STK AER CSV, filters valid data rows, separates
       individual passes by time gaps, and returns the time vector and
       elevation profile for Pass 2 (the best pass over Vigo, 250km VLEO).

       Returns:
           t_stk (pd.Series): Relative time from pass start in seconds
           el_stk (np.ndarray): Elevation angle in degrees for each time step

       Notes:
           Pass 2 (index 1) selected as representative pass — max elevation 36.9°,
           duration ~465s. Demonstrates real orbital geometry vs simulator's
           zenith pass assumption.
           STK scenario: Facility1 (Vigo, 42.24°N, 8.72°W),
           Satellite1 (250km, 97° inclination), 26-27 May 2026.
       """
    df = pd.read_csv(r'D:\STK\LEO_VLEO_Analysis\Facility-Facility1-To-Satellite-Satellite1_AER.csv',
                 skiprows=1,  # saltar cabecera original
                 names=['time', 'azimuth', 'elevation', 'range'],on_bad_lines='skip')

    # Filter valid data rows — keep only rows with actual timestamps
    df = df[df['time'].str.startswith('26 May') | df['time'].str.startswith('27 May')]

    # Convert elevation and range to numeric, drop invalid rows
    df['elevation'] = pd.to_numeric(df['elevation'], errors='coerce')
    df['range'] = pd.to_numeric(df['range'], errors='coerce')
    df = df.dropna()

    # Parse timestamps
    df['time'] = pd.to_datetime(df['time'], format='%d %b %Y %H:%M:%S.%f')

    # Separate passes by time gaps > 10 minutes
    df['gap'] = df['time'].diff() > pd.Timedelta(minutes=10)
    df['pass_id'] = df['gap'].cumsum()

    # Extract Pass 2 — best pass, max elevation 36.9°
    pass2 = df[df['pass_id'] == 1].copy()
    t_stk = (pass2['time'] - pass2['time'].iloc[0]).dt.total_seconds()
    el_stk = pass2['elevation'].values


    return t_stk, el_stk