# Obliczamy statystyki dla prędkości (Speed) legendarnych i nie-legendarnych pokemonów

# Podział na grupy
legendary = df_pokemon[df_pokemon['Legendary'] == True]['Speed']
non_legendary = df_pokemon[df_pokemon['Legendary'] == False]['Speed']

# Odchylenie standardowe (STD)
std_legendary = legendary.std()
std_non_legendary = non_legendary.std()

# Współczynnik zmienności (CV)
cv_legendary = (std_legendary / legendary.mean()) * 100
cv_non_legendary = (std_non_legendary / non_legendary.mean()) * 100

# Odchylenie IQR (połowa rozstępu międzykwartylowego)
q1_legendary = legendary.quantile(0.25)
q3_legendary = legendary.quantile(0.75)
iqr_legendary = q3_legendary - q1_legendary
iqr_dev_legendary = iqr_legendary / 2

q1_non_legendary = non_legendary.quantile(0.25)
q3_non_legendary = non_legendary.quantile(0.75)
iqr_non_legendary = q3_non_legendary - q1_non_legendary
iqr_dev_non_legendary = iqr_non_legendary / 2

print("Legendarny Pokémon:")
print(f"  Odchylenie standardowe (STD): {std_legendary:.2f}")
print(f"  Współczynnik zmienności (CV): {cv_legendary:.2f}%")
print(f"  Odchylenie IQR: {iqr_dev_legendary:.2f}")

print("\nNielegendarny Pokémon:")
print(f"  Odchylenie standardowe (STD): {std_non_legendary:.2f}")
print(f"  Współczynnik zmienności (CV): {cv_non_legendary:.2f}%")
print(f"  Odchylenie IQR: {iqr_dev_non_legendary:.2f}")