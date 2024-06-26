#
# Scenario: The bookstore wants to analyze its sales data to identify the bes t -selling genres.
#
# Assignment: Write SQL queries to calculate the total sales revenue for each genre by summing the
# prices of all books sold in each genre. Use GROUP BY to group the results by genre and display
# the total revenue for each.

from connection import execute_and_commit, execute_and_print_query, create_table, insert_data
def main():


    total_revenue_query = """
        SELECT genre, SUM(price) AS total_revenue
        FROM Books
        GROUP BY genre
        ORDER BY total_revenue DESC;
    """

    execute_and_print_query(total_revenue_query)

if __name__ == "__main__":
    main()
