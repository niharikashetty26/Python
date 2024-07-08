from prettytable import PrettyTable
from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2

# load_dotenv('../.env')
# dotenv_path = Path('.env')
load_dotenv()

hostname = os.getenv('HOSTNAME')
database = os.getenv('DATABASE')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
port_id = os.getenv('PORT_ID')

print(hostname)
print(database)
print(user_name)
print(password)
print(port_id)

conn = psycopg2.connect(
    host=hostname,
    database=database,
    user=user_name,
    password=password,
    port=port_id
)

print("Connected to database successfully!")


def get_connection():
    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=user_name,
        password=password,
        port=port_id
    )


admin_username = "admin"
admin_password = "admin123"


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
    try:
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(columns))
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"

        for value_set in values:
            execute_and_commit(insert_query, value_set, transactional=True)

        print(f"{len(values)} record(s) inserted successfully into '{table_name}'.")

    except Exception as e:
        print(f"Error inserting data into '{table_name}': {e}")

def execute_and_print_query(query):
    try:
        results, description = execute_and_commit(query, fetch=True)
        if not results:
            print("No results found.")
            return []

        table = PrettyTable()
        column_names = [desc[0] for desc in description]
        table.field_names = column_names

        for row in results:
            table.add_row(row)

        print(table)
        return results

    except Exception as e:
        print(f'Error: {e}')
        return []


class NoRowsUpdatedError(Exception):
    pass


def update_table(table_name, updates, *conditions, transactional=False):
    try:
        if not updates:
            raise ValueError("No updates provided.")

        select_query = f"SELECT * FROM {table_name}"
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


def upsert_data(table_name, columns, values, conflict_column):
    columns_str = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(values))
    conflict_update_columns = ", ".join(
        [f"{column} = EXCLUDED.{column}" for column in columns if column != conflict_column])
    upsert_query = f"""
        INSERT INTO {table_name} ({columns_str})
        VALUES ({placeholders})
        ON CONFLICT ({conflict_column})
        DO UPDATE SET {conflict_update_columns};
    """
    execute_and_commit(upsert_query, values, transactional=True)
    print(f"Upsert operation on table '{table_name}' completed successfully.")


def add_column_with_data(table_name, column_name, data_type, data=None, calculate_discount=None):
    try:
        add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type};"
        execute_and_commit(add_column_query)

        if data:
            for condition, value in data.items():
                update_query = f"UPDATE {table_name} SET {column_name} = {value} WHERE {condition};"
                execute_and_commit(update_query)

        if calculate_discount:
            for condition, expression in calculate_discount.items():
                update_query = f"UPDATE {table_name} SET {column_name} = {expression} WHERE {condition};"
                execute_and_commit(update_query)

        execute_and_print_query(f"SELECT * FROM {table_name};")
        print(f"Update operation on table '{table_name}' completed successfully.")

    except Exception as e:
        print(f"Error adding column '{column_name}': {e}")
