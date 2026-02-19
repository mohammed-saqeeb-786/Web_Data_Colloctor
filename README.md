WEB Data Collector
This project is designed to collect data from the Wildberries website and save it into a CSV file.

Description
The script utilizes asynchronous requests to fetch data from the Wildberries site. The collected data includes information about the brand, product name, original price, discounted price, and stock quantity. The gathered information is then saved into a CSV file.

Installation
Clone the repository:

Bash
git clone https://github.com/minkeviiich/WB_data_collector.git
Navigate to the project directory:

Bash
cd wb-data-collector
Install the required dependencies:

Bash
pip install -r requirements.txt
Usage
Run the script:

Bash
python main.py
The data will be saved in the wb_data.csv file.

Project Structure
main.py: The main script to execute the data collection.

models.py: Data models for parsing API responses.

requirements.txt: A list of project dependencies.

Data Example
The wb_data.csv file will contain the following columns:

Column	Description
id	Unique product identifier
Brand	The brand of the product
Name	Product title/name
Original Price	The starting price before discounts
Discounted Price	The current price after discounts
Quantity	Total items available in stock
Would you like me to help you translate the actual Python code (variable names and CSV headers) within main.py or models.py to match this English documentation?

