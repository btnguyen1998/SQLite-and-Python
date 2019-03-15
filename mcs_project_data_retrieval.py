import sqlite3
total = 12085
def create_db_and_table():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS vehicle_table (make text, model text, modelyear int, fuel text, city text, zipcode int) "
    cursor.execute(sql)
    cursor.close()

def add_data():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    with open("Public.csv", "r") as f:
        for line in f:
            if not line.startswith("VehicleType"):
                L = line.split(",")
                make = L[2]
                model = L[3]
                modelyear = L[4]
                fuel = L[6]
                city = L[8]
                zipcode = L[10]
                sql = "INSERT INTO vehicle_table (make, model, modelyear, fuel, city, zipcode) VALUES (:make, :model, :modelyear, :fuel, :city, :zipcode)"
                cursor.execute(sql, {"make": make, "model": model, "modelyear": modelyear, "fuel": fuel, "city": city, "zipcode": zipcode})
                conn.commit()
    cursor.close()

def display_all_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM vehicle_table"
    columns = cursor.execute(sql)
    all_entries = columns.fetchall()
    for entry in all_entries:
        print(entry)

def display_fuel():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM vehicle_table WHERE fuel LIKE '%Hybrid%'"
    fuel_column = cursor.execute(sql)
    all_fuel = list((fuel_column.fetchall()))
    print(("Percentage of Hybrid fuel based car:", (len(all_fuel)/total)*100))

def unique_models():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT DISTINCT model FROM vehicle_table"
    unique = cursor.execute(sql)
    all_unique = list(unique.fetchall())
    print("Different types of cars:", len(all_unique))

def average_car_year():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT AVG(modelyear) FROM vehicle_table"
    average = cursor.execute(sql).fetchall()
    print("Average car year:", average)


def most_commond_model():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT DISTINCT model FROM vehicle_table GROUP BY model ORDER BY COUNT(model) DESC"
    mostcommon = cursor.execute(sql).fetchall()
    print(mostcommon[0])

def second_most_common_city():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT DISTINCT city FROM vehicle_table GROUP BY city ORDER BY COUNT(city) DESC"
    second = cursor.execute(sql).fetchall()
    print(second[1])

def zipcode():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    sql = "SELECT DISTINCT zipcode FROM vehicle_table GROUP BY zipcode ORDER BY COUNT(zipcode) DESC"
    zip = cursor.execute(sql).fetchall()
    print(zip[0])

def main():
    create_db_and_table()
    add_data()
    display_fuel()
    average_car_year()
    unique_models()
    most_commond_model()
    second_most_common_city()
    zipcode()


    '''
    1. 516KB
    2. 48%
    3. 1983
    4. 197
    5. Camry
    6. Elmhurst
    7. 60618
    '''

main()