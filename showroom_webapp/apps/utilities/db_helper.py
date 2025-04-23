from django.db import connection


# Select All Data to JSON
def get_data(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Select Data with Value to JSON
def get_data_with_values(query, values):
    with connection.cursor() as cursor:
        cursor.execute(query, values)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Insert Data
def save_data(query, values):
    with connection.cursor() as cursor:
        cursor.execute(query, values)

# Insert Data Return
def save_return_data(query, values):
    with connection.cursor() as cursor:
        cursor.execute(query, values)
        connection.commit()
        return cursor.lastrowid

# Execute Query without Values
def execute(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    return json_data
