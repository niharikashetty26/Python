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

def create_table(table_name, columns):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()


        columns_str = ",\n".join(columns)
        create_table_query = f"""
            CREATE TABLE {table_name} (
                {columns_str}
            );
        """

        cursor.execute(create_table_query)
        conn.commit()
        print(f"Table '{table_name}' created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table '{table_name}': {e}")
    finally:
        if conn:
            conn.close()

def execute_and_print_query(cursor, query):
    try:
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

def insert_data(table_name, columns, values):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()


        columns_str = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(values))
        insert_query = f"""
            INSERT INTO {table_name} ({columns_str})
            VALUES ({placeholders});
        """

        cursor.execute(insert_query, values)
        conn.commit()

    except psycopg2.Error as e:
        print(f"Error inserting data into '{table_name}': {e}")
    finally:
        if conn:
            conn.close()

