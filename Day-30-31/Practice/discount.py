def calculate_discount(price, discount):
    try:
        if discount < 0:
            raise ValueError("Discount cannot be negative")
        discounted_price = price - (price * discount / 100)
        print(discounted_price)
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


calculate_discount(100, 20)
calculate_discount(200, -150)
