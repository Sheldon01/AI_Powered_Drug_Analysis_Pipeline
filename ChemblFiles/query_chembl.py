import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("ChemblFiles/chembl_35.db")

# Example query: Show all tables in the database
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(query, conn)
print("Tables in the database:")
print(tables)

# Example query: Preview the 'molecule_dictionary' table
query = "SELECT * FROM molecule_dictionary LIMIT 5;"
data = pd.read_sql_query(query, conn)
print("\nPreview of molecule_dictionary table:")
print(data)

# Close the connection
conn.close()
