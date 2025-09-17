# Goatlings Shop Parser
# This script reads a saved HTML file of your Goatlings shop
# and exports the item data to a CSV file.
#
# Required library: beautifulsoup4
# You can install it by opening your command prompt and typing:
# pip install beautifulsoup4

import csv
import os
from bs4 import BeautifulSoup

def parse_shop_html(input_html_path, output_csv_path):
    """
    Parses the Goatlings shop HTML file and extracts item data into a CSV.

    Args:
        input_html_path (str): The file path for the input HTML file.
        output_csv_path (str): The file path for the output CSV file.
    """
    try:
        # Read the HTML file
        with open(input_html_path, 'r', encoding='utf-8') as f:
            # Use Python's built-in HTML parser
            soup = BeautifulSoup(f, 'html.parser')

        # Find the "Update Items" button to locate the correct section of the page.
        update_button = soup.find('input', {'value': 'Update Items'})
        
        if not update_button:
            print("Error: Could not find the 'Update Items' button on the page.")
            print("Please ensure you have saved the correct shop inventory page.")
            return

        # Find the first table that comes *before* the update button.
        item_table = update_button.find_previous('table')

        if not item_table:
            print("Error: Could not find the item table before the 'Update Items' button.")
            print("The page structure may have changed.")
            return

        # Ensure the output directory exists
        output_dir = os.path.dirname(output_csv_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        # Prepare to write to a CSV file
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow(['Item', 'Price', 'Stock', 'Value', 'Description'])

            # Find all rows in the table
            all_rows = item_table.find_all('tr')

            # Process all rows *except* the first one (the header)
            for row in all_rows[1:]:
                cells = row.find_all('td')

                # A valid item row has exactly 6 cells.
                if len(cells) < 6:
                    continue

                try:
                    # Extract data from the cells.
                    item_name = cells[0].get_text(strip=True)
                    price_input = cells[1].find('input')
                    price = price_input.get('value', '0') if price_input else 'N/A'
                    stock = cells[2].get_text(strip=True)
                    value = cells[3].get_text(strip=True).replace(' DS', '').replace(',', '')
                    description = cells[4].get_text(strip=True)

                    # Write the extracted data to the CSV
                    writer.writerow([item_name, price, stock, value, description])
                except (AttributeError, IndexError) as e:
                    # This will catch errors if a row has an unexpected structure
                    print(f"Skipping a row due to a parsing error: {e}")

        print(f"\nSuccess! Data has been exported to {os.path.abspath(output_csv_path)}")

    except FileNotFoundError:
        print(f"Error: The file '{input_html_path}' was not found.")
        print(f"Please make sure '{input_html_path}' is in the same folder as this script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    # Define the fixed input file name.
    input_file = 'shop.htm'
    
    # Ask the user for the output directory.
    print("Please enter the full folder path where you want to save 'shop.csv'.")
    print(r"Example: C:\Users\YourName\Documents\Goatlings")
    output_folder = input("Output folder path (leave blank to save in the same folder as the script): ")

    # If the user leaves it blank, default to the current directory.
    if not output_folder:
        output_folder = '.' # '.' represents the current directory

    # Create the full path for the output file.
    output_path = os.path.join(output_folder, 'shop.csv')

    # Run the parsing function
    parse_shop_html(input_file, output_path)

