import pandas as pd

def STK_doppler():
    """
       Loads and processes STK Range Rate report for Facility1-to-Satellite1 access.

       Reads the exported STK Range Rate CSV, filters valid data rows, separates
       individual passes by time gaps, and returns the time vector and range rate
       profile for Pass 2.

       Range rate is negative when satellite is approaching (Doppler shift positive)
       and positive when receding (Doppler shift negative). Sign convention must be
       inverted when converting to Doppler frequency shift.

       Returns:
           t_doppler_stk (pd.Series): Relative time from pass start in seconds
           RangeRate_stk (np.ndarray): Range rate in km/s for each time step

       Notes:
           Pass 2 max range rate: ±7.4 km/s → ±49 kHz Doppler at S-band (2 GHz).
           Significantly higher than simulator's ±14 kHz due to non-zenith geometry —
           satellite approaches nearly head-on at pass start, maximising radial velocity.
           STK scenario: Facility1 (Vigo, 42.24°N, 8.72°W),
           Satellite1 (250km, 97° inclination), 26-27 May 2026.
       """
    df = pd.read_csv('..\..\data\stk\Facility-Facility1-To-Satellite-Satellite1_Range_Rate.csv',
                 skiprows=1,
                 names=['time', 'RangeRate'],on_bad_lines='skip')

    # Filter valid data rows — keep only rows with actual timestamps
    df = df[df['time'].str.startswith('26 May') | df['time'].str.startswith('27 May')]

    # Convert RangeRate to numeric, drop invalid rows
    df['RangeRate'] = pd.to_numeric(df['RangeRate'], errors='coerce')
    df = df.dropna()

    # Parse timestamps
    df['time'] = pd.to_datetime(df['time'], format='%d %b %Y %H:%M:%S.%f')

    # Separate passes by time gaps > 10 minutes
    df['gap'] = df['time'].diff() > pd.Timedelta(minutes=10)
    df['pass_id'] = df['gap'].cumsum()

    # Extract Pass 2 — best pass, max range rate ±7.4 km/s
    pass2 = df[df['pass_id'] == 1].copy()
    t_doppler_stk = (pass2['time'] - pass2['time'].iloc[0]).dt.total_seconds()
    RangeRate_stk = pass2['RangeRate'].values


    return t_doppler_stk, RangeRate_stk