from connection import execute_and_print_query, add_column_with_data


def main():
    table_name = "Books"
    column_name_publication_year = "publication_year"
    column_name_discounted_price = "discounted_price"
    data_type_int = "INT"
    data_type_numeric = "NUMERIC(10,2)"

    update_data_publication_year = {
        "bookid = 1": 1960,
        "bookid = 2": 2012,
        "bookid = 3": 1813,
        "bookid = 4": 2001,
        "bookid = 5": 1951
    }

    calculate_discount = {
        "publication_year > 2000": "price * 0.9"
    }

    try:
        print(f"\n{table_name} table (Original):")
        execute_and_print_query(f"SELECT * FROM {table_name};")

        add_column_with_data(table_name, column_name_publication_year, data_type_int, update_data_publication_year)
        add_column_with_data(table_name, column_name_discounted_price, data_type_numeric, calculate_discount)

    except Exception as e:
        print(f"Error in main function: {e}")


if __name__ == "__main__":
    main()
