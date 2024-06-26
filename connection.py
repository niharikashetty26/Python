import psycopg2

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

def execute_and_commit(query, values=None):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        conn.commit()
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
    finally:
        if conn:
            conn.close()

def create_table(table_name, columns):
    columns_str = ",\n".join(columns)
    create_table_query = f"""
        CREATE TABLE {table_name} (
            {columns_str}
        );
    """
    execute_and_commit(create_table_query)
    print(f"Table '{table_name}' created successfully.")

def insert_data(table_name, columns, values):
    columns_str = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(values))
    insert_query = f"""
        INSERT INTO {table_name} ({columns_str})
        VALUES ({placeholders});
    """
    execute_and_commit(insert_query, values)

def execute_and_print_query(query):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No results found.")
            return

        column_names = [desc[0] for desc in cursor.description]
        column_widths = [max(len(str(value)) for value in col) for col in zip(*results, column_names)]

        header_format = " | ".join([f"{{:<{width}}}" for width in column_widths])
        print(header_format.format(*column_names))
        print("-+-".join(['-' * width for width in column_widths]))

        row_format = " | ".join([f"{{:<{width}}}" for width in column_widths])
        for row in results:
            print(row_format.format(*row))
        print()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if conn:
            conn.close()