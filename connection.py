import psycopg2
from psycopg2 import extras

hostname = '127.0.0.1'
database = 'Bookstore'
user_name = 'postgres'
pwd = 'admin'
port_id = 5432

def get_connection():
    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=user_name,
        password=pwd,
        port=port_id
    )

def json_record_exists(cursor, value, table_name, column_name):
    cursor.execute(f'SELECT 1 FROM {table_name} WHERE {column_name} = %s', (extras.Json(value),))
    return cursor.fetchone() is not None

def record_exists(cursor, id, table_name, table_id):
    cursor.execute(f'SELECT 1 FROM {table_name} WHERE {table_id} = %s', (id,))
    return cursor.fetchone() is not None

def execute_and_print_query(cursor, query):
    try:
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No results found.")
            return

        # Fetch column names from cursor description
        column_names = [desc[0] for desc in cursor.description]

        # Determine maximum length for each column
        column_widths = [max(len(str(value)) for value in col) for col in zip(*results, column_names)]

        # Print the headers
        header_format = " | ".join([f"{{:<{width}}}" for width in column_widths])
        print(header_format.format(*column_names))
        print("-+-".join(['-' * width for width in column_widths]))

        # Print each row of results
        row_format = " | ".join([f"{{:<{width}}}" for width in column_widths])
        for row in results:
            print(row_format.format(*row))
        print()
    except Exception as e:
        print(f'Error: {e}')
