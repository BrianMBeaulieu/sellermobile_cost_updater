# sellermobile_cost_updater

Script to take an item cost that's embedded in an ASIN and update the cogs column in the Seller Mobile template file

ASIN Format: B0A6QG0STW_1.99_6.93_257

ASIN is parsed by _ and the cost of the item needs to be in position 2 (1.99 in the example above)

# Prerequisites
* Python 3.x
* pandas package
* xlrd package
* openpyxl package

# How to Use
* Download the Excel template from Seller Mobile
* Run the python script against the file.  The cogs column will be populated with the cost extracted from the ASIN
* Upload the file back to Seller Mobile

***test with 1 row first just to confirm things***



