import psycopg2
from prettytable import PrettyTable

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


def execute_and_commit(query, values=None, fetch=False, transactional=False):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        if fetch:
            results = cursor.fetchall()
            return results, cursor.description

        if transactional:
            conn.commit()
        else:
            conn.commit()

    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        if conn and transactional:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def create_table(table_name, columns):
    columns_str = ", ".join(columns)
    create_table_query = f"CREATE TABLE {table_name} ({columns_str});"
    execute_and_commit(create_table_query)
    print(f"Table '{table_name}' created successfully.")


def insert_data(table_name, columns, values):
    columns_str = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(values))
    insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
    execute_and_commit(insert_query, values)


def execute_and_print_query(query):
    try:
        results, description = execute_and_commit(query, fetch=True)
        if not results:
            print("No results found.")
            return

        table = PrettyTable()
        column_names = [desc[0] for desc in description]
        table.field_names = column_names

        for row in results:
            table.add_row(row)

        print(table)
    except Exception as e:
        print(f'Error: {e}')


class NoRowsUpdatedError(Exception):
    pass


def update_table(table_name, updates, *conditions, transactional=False):
    try:
        if not updates:
            raise ValueError("No updates provided.")

        # Check if there are any rows matching the conditions
        select_query = f"SELECT COUNT(*) FROM {table_name}"
        if conditions:
            where_clause = " AND ".join(conditions)
            select_query += f" WHERE {where_clause};"
        else:
            select_query += ";"

        result, _ = execute_and_commit(select_query, fetch=True)

        if result and len(result) > 0 and result[0][0] == 0:
            raise NoRowsUpdatedError(f"No rows match the conditions in table '{table_name}'.")

        set_values = ", ".join([f"{column} = %s" for column, value in updates.items()])
        values = tuple([value for column, value in updates.items()])

        if conditions:
            where_clause = " AND ".join(conditions)
            update_query = f"UPDATE {table_name} SET {set_values} WHERE {where_clause};"
        else:
            update_query = f"UPDATE {table_name} SET {set_values};"

        execute_and_commit(update_query, values, transactional=transactional)
        print(f"Update operation on table '{table_name}' completed successfully.")

    except NoRowsUpdatedError as e:
        print(f"Error updating table '{table_name}': {e}")
    except ValueError as e:
        print(f"Error updating table '{table_name}': {e}")
    except Exception as e:
        print(f"Unexpected error updating table '{table_name}': {e}")
