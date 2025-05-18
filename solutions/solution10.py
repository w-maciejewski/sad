# Kurtoza IQR dla ataku (Attack) legendarnych pokemonów
from scipy.stats import kurtosis
legendary_attack = df_pokemon[df_pokemon['Legendary'] == True]['Attack']

q1 = legendary_attack.quantile(0.25)
q3 = legendary_attack.quantile(0.75)
c10 = legendary_attack.quantile(0.10)
c90 = legendary_attack.quantile(0.90)

iqr_kurtoza = (q3 - q1) / (2 * (c90 - c10))
kurtoza = kurtosis(legendary_attack)
print(f"Kurtoza klasyczna dla ataku legendarnych pokemonów: {kurtoza:.3f}")
print(f"Kurtoza IQR dla ataku legendarnych pokemonów: {iqr_kurtoza:.3f}")