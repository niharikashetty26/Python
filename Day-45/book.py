# from connection import conn, record_exists, execute_and_print_query

# cur = None

# try:
#     cur = conn.cursor()
#     filter1 = '''
#                 select * from books where genre='Fiction' order by price asc
#                 '''
#     execute_and_print_query(cur, filter1)
#     price = 'select price from books'
#     cur.execute(price)
#     result=0
#     for i in cur.fetchall():
#         result += i[0]
#     print(result)
#     conn.commit()
# except Exception as e:
#     print(e)
# finally:
#     if cur is not None:
#         cur.close()
#     if conn is not None:
#         conn.close()
