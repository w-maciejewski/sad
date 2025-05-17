# Kurtoza IQR dla prędkości (Speed) legendarnych pokemonów

legendary_speed = df_pokemon[df_pokemon['Legendary'] == True]['Speed']

q1 = legendary_speed.quantile(0.25)
q3 = legendary_speed.quantile(0.75)
c10 = legendary_speed.quantile(0.10)
c90 = legendary_speed.quantile(0.90)

iqr_kurtoza = (q3 - q1) / (2 * (c90 - c10))
print(f"Kurtoza IQR dla prędkości legendarnych pokemonów: {iqr_kurtoza:.3f}")