import csv
import numpy as np
import matplotlib.pyplot as plt

# Open the CSV file
with open('sales_data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    arr = np.array(list(csv_reader))


def calculate_total_sales(arr):
    sales_of_A = 0
    sales_of_B = 0
    sales_of_C = 0
    monthly_sales = {'Month': [], 'Product_A': [], 'Product_B': [], 'Product_C': []}

    for row in arr[1:]:
        month, sales_A, sales_B, sales_C = row
        sales_of_A += int(sales_A)
        sales_of_B += int(sales_B)
        sales_of_C += int(sales_C)

        # Store monthly sales data for plotting
        monthly_sales['Month'].append(month)
        monthly_sales['Product_A'].append(int(sales_A))
        monthly_sales['Product_B'].append(int(sales_B))
        monthly_sales['Product_C'].append(int(sales_C))

    print(f'Total sales of Product A: {sales_of_A}')
    print(f'Total sales of Product B: {sales_of_B}')
    print(f'Total sales of Product C: {sales_of_C}\n')

    return monthly_sales


def find_highest_sale_month(arr):
    total = 0
    month = ""
    for row in arr[1:]:
        temp = sum(map(int, row[1:]))
        if temp > total:
            total = temp
            month = row[0]
    print(f'Highest sales are {total} in {month}')


def plot_monthly_sales_trends(monthly_sales):
    plt.figure(figsize=(10, 6))

    plt.plot(monthly_sales['Month'], monthly_sales['Product_A'], label='Product A')
    plt.plot(monthly_sales['Month'], monthly_sales['Product_B'], label='Product B')
    plt.plot(monthly_sales['Month'], monthly_sales['Product_C'], label='Product C')

    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Trends for Each Product')
    plt.legend()
    plt.show()


def create_bar_chart_total_sales(total_sales):
    products = ['Product A', 'Product B', 'Product C']
    total_sales_values = [total_sales['Product_A'], total_sales['Product_B'], total_sales['Product_C']]

    plt.bar(products, total_sales_values, color=['blue', 'green', 'orange'])
    plt.xlabel('Products')
    plt.ylabel('Total Sales')
    plt.title('Total Sales for Each Product')
    plt.show()


# Calculate total sales and get monthly sales data for plotting
monthly_sales_data = calculate_total_sales(arr)

# Plot monthly sales trends for each product
plot_monthly_sales_trends(monthly_sales_data)

# Find the highest sales month
find_highest_sale_month(arr)

# Create a bar chart to compare total sales for each product
create_bar_chart_total_sales({
    'Product_A': sum(monthly_sales_data['Product_A']),
    'Product_B': sum(monthly_sales_data['Product_B']),
    'Product_C': sum(monthly_sales_data['Product_C'])
})
