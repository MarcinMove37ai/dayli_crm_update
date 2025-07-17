import os
import psycopg2
import sys

# Pobierz URL bazy danych ze zmiennych środowiskowych Railway
DATABASE_URL = os.environ.get('DATABASE_URL')

if not DATABASE_URL:
    print("BŁĄD: Zmienna środowiskowa DATABASE_URL nie jest ustawiona.")
    sys.exit(1)

conn = None
try:
    # Połącz się z bazą danych
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Wykonaj funkcję
    print("Uruchamiam funkcję dziennej aktualizacji...")
    cur.execute("SELECT update_daily_date_and_aggregates();")

    # Zatwierdź transakcję
    conn.commit()

    print("Dzienna aktualizacja wykonana pomyślnie.")

    # Zamknij połączenie
    cur.close()

except Exception as e:
    print(f"Wystąpił błąd: {e}")
    sys.exit(1) # Zakończ z kodem błędu, aby Railway wiedziało o problemie
finally:
    if conn is not None:
        conn.close()
