import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import psycopg2

# Längst ner finns mina slutsatser som även syns i terminalen och en sammanfattning av min analys.

# Läs in CSV-filen korrekt
file_path = "bearbetad_materialatervinning.csv"

# Kontrollera först vilken separator som används
with open(file_path, "r", encoding="utf-8") as file:
    first_line = file.readline()
    separator = ";" if ";" in first_line else ","

# Läs in filen med rätt separator
data = pd.read_csv(file_path, sep=separator, encoding="utf-8")

# Rensa kolumnnamn för att undvika osynliga mellanslag
data.columns = data.columns.str.strip()

# Kontrollera att rätt kolumner finns
print("Kolumnnamn i CSV:", data.columns)

# Kontrollera att rätt kolumner finns
if 'Materialåtervinning %' not in data.columns:
    print("Fel: Kolumnen 'Materialåtervinning %' saknas i CSV-filen.")
    print("Följande kolumner finns i filen:", data.columns.tolist())
    exit()

# Hantera saknade värden utan FutureWarning
median_value = data["Materialåtervinning %"].median()
data["Materialåtervinning %"] = data["Materialåtervinning %"].fillna(median_value)

# Beräkna procentuell förändring per kommun
data["Procentuell förändring"] = data.groupby("Kommun/ förbund")["Materialåtervinning %"].pct_change().round(3)

# Lägg till ett trendvärde med glidande medelvärde
window_size = 3
data["Trendvärde"] = data.groupby("Kommun/ förbund")["Materialåtervinning %"].transform(lambda x: x.rolling(window_size, min_periods=1).mean())

# Kategorisera återvinningsnivåer
bins = [0, 30, 50, 100]
labels = ["Låg", "Medel", "Hög"]
data["Återvinningsnivå"] = pd.cut(data["Materialåtervinning %"], bins=bins, labels=labels)

# Filtrera data från 2015 och framåt
filtered_data = data[data["År"] >= 2015]

# Summera per kommun
grouped_data = filtered_data.groupby("Kommun/ förbund").agg(
    Genomsnittlig_återvinning=("Materialåtervinning %", "mean"),
    Antal_mätningar=("Materialåtervinning %", "count")
).reset_index()

# Spara den bearbetade datan i en ny CSV-fil
#output_file = "bearbetad_materialatervinning.csv"
#data.to_csv(output_file, sep=separator, index=False, encoding="utf-8")
#print(f"Bearbetad data sparad i: {output_file}")


# Anpassa färger för visualisering
sns.set_palette("pastel")

# 1. Histogram
# individuell_histogram_materialåtervinning.png
plt.figure(figsize=(10, 6))
sns.histplot(data["Materialåtervinning %"], bins=20, kde=True, color="blue")
plt.title("Histogram över Materialåtervinning %")
plt.xlabel("Materialåtervinning %")
plt.ylabel("Frekvens")
plt.show()
# Visualiserar frekvensen av återvinningsprocenten. 
# Medan den röda linjen (KDE) visar en uppskattning av fördelningens form.


# 2. Linjediagram
# individuell_linjediagram_materialåtervinning.png
plt.figure(figsize=(12, 6))
sns.lineplot(x="År", y="Materialåtervinning %", hue="Kommun/ förbund", data=data)
plt.title("Linjediagram över Materialåtervinning per Kommun")
plt.xlabel("År")
plt.ylabel("Materialåtervinning %")
plt.legend(title="Kommun")
plt.show()
# Det visar utvecklingen av materialåtervinning över tid per kommun.


# 3. Scatter plot
# individuell_scatterplot_materialåtervinning.png
plt.figure(figsize=(10, 6))
sns.scatterplot(x="År", y="Materialåtervinning %", hue="Kommun/ förbund", data=data, alpha=1)
plt.title("Scatter Plot över Materialåtervinning")
plt.xlabel("År")
plt.ylabel("Materialåtervinning %")
plt.legend(title="Kommun")
plt.show()
# Varje punkt representerar ett specifikt år för en viss kommun.


# 4. Heatmap
# individuell_heatmap_materialåtervinning.png
pivot_table = filtered_data.pivot(index="År", columns="Kommun/ förbund", values="Materialåtervinning %")
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, cmap="coolwarm", annot=True, fmt=".1f")
plt.title("Heatmap över materialåtervinning per kommun och år")
plt.show()
# Den visar data som en färggradient där färger representerar återvinningsprocenten för varje år och kommun.


# 5. En linjär regressionsmodell för prediktion
# individuell_linje_regression_materialåtervinning.png
features = ["År", "Procentuell förändring", "Trendvärde"]  # Lägg till fler variabler
X = data[features].dropna()
y = data.loc[X.index, "Materialåtervinning %"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Lägg till ett linjediagram för ett tydligare resultat
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color="blue", alpha=0.6, label="Predikterade värden")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linestyle="dashed", label="Perfekt prediktion")
plt.xlabel("Faktiska värden")
plt.ylabel("Predikterade värden")
plt.title("Linjär regression: Faktiska vs. Predikterade värden")
plt.legend()  # Visar vad de olika färgerna betyder
plt.grid(True)  # Lägg till rutnät för bättre läsbarhet
plt.show()
# Visar de faktiska värdena (y-test) jämfört med de predikterade värdena (y-pred) från linjär regression.



# Exportera data till Excel och PostgreSQL
#filtered_data.to_excel("bearbetad_materialåtervinnings_data.xlsx", index=False)

# Anslut till PostgreSQL-databasen
#conn = psycopg2.connect(
#    database="postgres", # Byt ut med din databas
#    user="postgres", # Byt ut med ditt användarnamn
#    password="Limpbizkit44", # Byt ut med ditt lösenord
#    host="localhost", # Byt ut med din värd
#    port="5544" # Byt ut med din port
#)
#cursor = conn.cursor() 

# Skapa tabellen i PostgreSQL om den inte redan finns
#cursor.execute("""
#    CREATE TABLE IF NOT EXISTS Återvinningsdata.återvinningsdata (
#        Kommun TEXT,
#        År INT,
#        Materialåtervinning FLOAT,
#        Procentuell_förändring FLOAT,
#        Trendvärde FLOAT,
#        Återvinningsnivå TEXT
#    )
#""")
#conn.commit()

#for _, row in filtered_data.iterrows():
#    cursor.execute("""
#        INSERT INTO Återvinningsdata.återvinningsdata (Kommun, År, Materialåtervinning, Procentuell_förändring, Trendvärde, Återvinningsnivå)
#        VALUES (%s, %s, %s, %s, %s, %s)
#    """, (row['Kommun/ förbund'], row['År'], row['Materialåtervinning %'], row['Procentuell förändring'], row['Trendvärde'], row['Återvinningsnivå']))

# Spara ändringar i databasen
# Stäng anslutningen
#conn.commit()
#cursor.close()
#conn.close()

#print("CSV-filen har importerats till PostgreSQL!")


# Slutsatser
print("Slutsatser:")
print("1. Diagrammet indikerar att majoriteten av kommunerna återvinner måttlig mängd material.")
print("1. Stort gap mellan låg och hög återvinning: Detta gap kan peka på systematiska skillnader mellan kommuner i fråga om återvinningsinfrastruktur, policyer eller medborgarnas engagemang.")
print("2. En del kommuner verkar ha stagnerat eller haft en nedgång i återvinningen under vissa perioder, vilket kan tyda på problem i återvinningssystemet eller förändringar i deras hantering av avfall.")
print("2. Det faktum att trenderna skiljer sig åt mellan kommunerna antyder att lokala beslut, prioriteringar och initiativ har en betydande inverkan på återvinningsnivåerna.")
print("3. Det finns kluster av kommuner som har liknande återvinningsnivåer, medan andra är mer spridda.")
print("3. Lätt att se trender för specifika kommuner, om de har ökat, minskat eller hållit en konstant nivå i sina återvinningsnivåer.")
print("4. Färgskalans intensitet gör det lätt att se om en kommun har konsekvent hög eller låg återvinning varje år.")
print("4. Heatmapen ger en konkret bild av varje kommuns prestation över tid, vilket kan vara användbart för att prioritera vilka kommuner som behöver åtgärder.")
print("5. Om punkterna ligger nära den röda linjen, innebär det att den linjära regressionsmodellen fungerar bra och ger realistiska förutsägelser.")
print("5. Modellen kan förbättras genom att använda mer avancerade modeller som kan fånga komplexa samband mellan olika faktorer och återvinning.")

# Sammanfattningsvis visar visualiseringarna en tydlig bild av hur återvinningen varierar mellan olika år och kommuner, de visar viktiga trender och mönster. 
# Det finns både styrkor och svagheter i återvinningssystemet, vilket pekar på att det finns ett behov att anpassa insatserna beroende på lokala förhållanden och efter vilka resurser som finns. 
# Baserat på den data som jag har så får vi viktiga insikter av den linjära regrissionsmodellen. 
# Den hade kunnat varit ännu mer komplex om vi hade haft mer historisk data att gå efter och gett mer djupgående insikter. 