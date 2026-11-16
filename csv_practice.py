# Reflection 1:
# Python is helpful for repeating the same steps on a large amount of sales data
# without manually applying formulas each time. Excel is easier when I just want
# to quickly view the data, change a few cells, or make a simple chart.
#
# Reflection 2:
# A business could keep a daily sales log to track how its revenue changes over time.
# Append mode is useful because each new entry gets added to the log without
# deleting the entries from previous days.

import csv
from datetime import datetime


# Exercise 1: Set up the sales CSV file in the data folder.
sales_file = "data/sales.csv"


# Exercise 2: Read and print all rows, including the header.
print("\nExercise 2: Raw CSV rows")
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Exercise 3: Skip the header row and print it separately.
print("\nExercise 3: Header and data rows")
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)


# Exercise 4: Calculate the revenue for each order and the overall total.
print("\nExercise 4: Revenue totals")
total_revenue = 0
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        order_total = price * quantity
        total_revenue += order_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${order_total:.2f}")

print(f"Overall total revenue: ${total_revenue:.2f}")


# Exercise 5: Save only orders worth more than $100 in a new CSV file.
print("\nExercise 5: Cleaned CSV")
original_rows = 0
cleaned_rows = 0
with open(sales_file, "r", newline="", encoding="utf-8") as source:
    reader = csv.reader(source)
    next(reader)

    with open("data/cleaned.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_rows += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            order_total = price * quantity

            if order_total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{order_total:.2f}"])
                cleaned_rows += 1

print(f"Wrote {cleaned_rows} of {original_rows} original rows to data/cleaned.csv")


# Exercise 6: Read rows with DictReader instead of list indexes.
# csv.reader is simple when the column order is known and will not change.
# DictReader is easier to follow because it lets me use column names instead of indexes.
print("\nExercise 6: DictReader totals")
dict_total_revenue = 0
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        order_total = price * quantity
        dict_total_revenue += order_total
        print(f"{product}: ${order_total:.2f}")

print(f"Overall total with DictReader: ${dict_total_revenue:.2f}")


# Exercise 7: Accumulate revenue for each product and sort alphabetically.
print("\nExercise 7: Revenue summary by product")
product_summary = {}
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        order_total = float(row["price"]) * int(row["quantity"])
        if product not in product_summary:
            product_summary[product] = 0
        product_summary[product] += order_total

for product in sorted(product_summary):
    print(f"{product}: ${product_summary[product]:.2f}")


# Exercise 8: Append a new timestamped entry every time the script runs.
print("\nExercise 8: Append mode log")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a", encoding="utf-8") as log_file:
    log_file.write(f"{current_time} | Total revenue: ${total_revenue:.2f}\n")

print("Added one entry to data/run_log.txt")
