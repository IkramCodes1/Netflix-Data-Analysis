
import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# CHARGER LE DATASET
# ==================================================

netflex_dataset = pd.read_csv("NetFlix.csv")

df = netflex_dataset.copy()


"""
=============================================
PARTIE 1 : DATA CLEANING
=============================================
"""

# Nombre de lignes avant nettoyage
initial_rows = len(df)

# Supprimer les doublons
df.drop_duplicates(inplace=True)

# Remplacer les valeurs manquantes
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

# Supprimer les lignes incomplètes
df.dropna(
    subset=['date_added', 'rating', 'genres', 'description'],
    inplace=True
)

# Convertir date_added en format datetime
df['date_added'] = pd.to_datetime(
    df['date_added'],
    format='mixed',
    errors='coerce'
)

# Supprimer les dates invalides
df.dropna(subset=['date_added'], inplace=True)

# Résultat du nettoyage
final_rows = len(df)

print("Lignes avant nettoyage :", initial_rows)
print("Lignes après nettoyage :", final_rows)
print("Lignes supprimées :", initial_rows - final_rows)

print("\nValeurs manquantes restantes :")
print(df.isnull().sum())

print("\nType de date_added :")
print(df['date_added'].dtype)


"""
=============================================
PARTIE 2 : EXPLORATORY DATA ANALYSIS
=============================================
"""


# ==================================================
# 1. MOVIES VS TV SHOWS
# ==================================================

print("\n--- Movies vs TV Shows ---")

content_type = df["type"].value_counts()

print(content_type)

print("\nPercentage :")
print(df["type"].value_counts(normalize=True) * 100)


# Diagramme 1 : Pie Chart

content_type.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribution of Movies and TV Shows")
plt.ylabel("")
plt.show()


# ==================================================
# 2. TOP COUNTRIES
# ==================================================

print("\n--- Top Countries ---")

# Séparer les pays multiples
countries = df["country"].str.split(", ").explode()

top_countries = countries.value_counts().head(10)

print(top_countries)


# Diagramme 2 : Bar Chart

top_countries.plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==================================================
# 3. CONTENT ADDED BY YEAR
# ==================================================

print("\n--- Content Added by Year ---")

# Extraire l'année
df["year_added"] = df["date_added"].dt.year

content_by_year = df["year_added"].value_counts().sort_index()

print(content_by_year)


# Diagramme 3 : Line Chart

content_by_year.plot(
    kind="line",
    figsize=(10, 5),
    marker="o"
)

plt.title("Netflix Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid()
plt.show()


# ==================================================
# 4. MOST COMMON RATINGS
# ==================================================

print("\n--- Most Common Ratings ---")

ratings = df["rating"].value_counts()

print(ratings)


# ==================================================
# 5. MOST COMMON GENRES
# ==================================================

print("\n--- Most Common Genres ---")

# Séparer les genres multiples
genres = df["genres"].str.split(", ").explode()

top_genres = genres.value_counts().head(10)

print(top_genres)


# ==================================================
# 6. MOVIES VS TV SHOWS BY YEAR
# ==================================================

print("\n--- Movies vs TV Shows by Year ---")

type_by_year = df.groupby(
    ["year_added", "type"]
).size().unstack(fill_value=0)

print(type_by_year)


# ==================================================
# 7. CONTENT BY RELEASE YEAR
# ==================================================

print("\n--- Content by Release Year ---")

release_years = df["release_year"].value_counts().sort_index()

print(release_years)

