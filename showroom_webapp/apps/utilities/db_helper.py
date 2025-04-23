from django.db import connection


def get_data(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Select All Data to JSON
def get_data_with_values(query, values):
    with connection.cursor() as cursor:
        cursor.execute(query, values)
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return results

# Insert Data
def insert(conn, query, values):
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()


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



# class DBHelper():
#     def __init__(self):
#         self.db = connection()
    
#     def get_data(self, query, values):
#         return select(self.db, query, values)
    
#     def get_count_data(self, query):
#         return row_count(self.db, query)
    
#     def get_count_filter_data(self, query, values):
#         return row_count_value(self.db, query, values)
    
#     def save_data(self, query, values):
#         return insert(self.db, query, values)
    
#     def save_return(self, query, values):
#         return insert_return(self.db, query, values)

#     def update_data(self, query, values):
#         return insert(self.db, query, values)
    
#     def execute(self, query):
#         return execute(self.db, query)