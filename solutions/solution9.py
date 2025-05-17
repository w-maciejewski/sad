# Skośność IQR dla punktów za atak (Attack) dla kilku generacji pokemonów

def iqr_skewness(series):
    q1 = series.quantile(0.25)
    med = series.median()
    q3 = series.quantile(0.75)
    return ((q3 - med) - (med - q1)) / (q3 - q1)

for gen in sorted(df_pokemon['Generation'].unique()):
    attack = df_pokemon[df_pokemon['Generation'] == gen]['Attack']
    skew_iqr = iqr_skewness(attack)
    print(f"Generacja {gen}: skośność IQR dla Attack = {skew_iqr:.3f}")