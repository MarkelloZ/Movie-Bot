import pandas as pd
import mysql.connector
import pandas as pd

# Φόρτωση των ανεβασμένων αρχείων CSV
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Αφαίρεση ταινιών που δεν έχουν έτος κυκλοφορίας στον τίτλο
movies_df = movies_df[movies_df['title'].str.contains(r'\(\d{4}\)')]

# Εξαγωγή του έτους κυκλοφορίας από τον τίτλο και δημιουργία της νέας στήλης 'reldate'
movies_df['reldate'] = movies_df['title'].str.extract(r'\((\d{4})\)').astype(int)

# Υπολογισμός του μέσου όρου βαθμολογιών για κάθε ταινία
average_ratings = ratings_df.groupby('movieId')['rating'].mean().reset_index()

# Συγχώνευση του dataframe των ταινιών με το dataframe των μέσων όρων βαθμολογιών
merged_df = pd.merge(movies_df[['movieId', 'title', 'reldate']], average_ratings, on='movieId')

# Μετονομασία της στήλης 'rating' σε 'ratings'
merged_df.rename(columns={'rating': 'ratings'}, inplace=True)

# Αφαίρεση του έτους κυκλοφορίας από τον τίτλο στην στήλη 'title'
merged_df['title'] = merged_df['title'].str.replace(r'\s\(\d{4}\)', '', regex=True)

# Αποθήκευση του αποτελέσματος στο αρχείο 'output.csv'
output_path = 'output.csv'
merged_df.to_csv(output_path, index=False)

# Σύνδεση με τη βάση δεδομένων MySQL
connection = mysql.connector.connect(
    host='localhost',      # Αντικατάστησε με τη διεύθυνση του server σου
    user='root',  # Αντικατάστησε με το όνομα χρήστη
    password='1234',  # Αντικατάστησε με τον κωδικό σου
    database='imbd2'   # Η βάση δεδομένων που δημιουργήσαμε παραπάνω
)

cursor = connection.cursor()

# Φόρτωση των δεδομένων από το output.csv
df = pd.read_csv('output.csv')

# Εισαγωγή δεδομένων στον πίνακα movies
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO movies (movieId, title, reldate)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE title = VALUES(title), reldate = VALUES(reldate)
    ''', (row['movieId'], row['title'], row['reldate']))

for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO ratings (userId, movieId, rating)
        VALUES (%s, %s, %s)
    ''', (row['userId'], row['movieId'], row['rating']))

# Αποθήκευση αλλαγών στη βάση δεδομένων
connection.commit()

# Κλείσιμο του cursor και της σύνδεσης
cursor.close()
connection.close()