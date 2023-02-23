# LinkedinProfileVisit
The program visit a number of Linkedin profiles using a random timing


This program is a Python script that uses the Selenium library to visit LinkedIn profiles from a specific given link. It automates the process of opening profiles and moving to the next profile. It clicks also on others pages and use a random timing to looks more human.

Requirements
To use this program, you need to have Python installed on your computer, as well as the following Python libraries:

selenium
pandas
webdriver_manager
You also need to have the Chrome web browser installed on your computer.

Installation
Clone or download the repository to your computer.
Install the required Python libraries using pip: pip install -r requirements.txt
Install the ChromeDriver using the webdriver_manager library: webdriver_manager.chrome.install()
Usage
Open the linkedin_scraper.py file in a text editor.
Edit the username and password variables to match your LinkedIn account credentials.
Edit the n_pages variable to set the number of pages of search results you want to scrape.
Edit the keyword search in the driver.get() line to match the search criteria you want to use.
Save the linkedin_scraper.py file.
Run the script using the command python linkedin_scraper.py.
The program will open the Chrome web browser, log in to your LinkedIn account, and start scraping profile data. The data will be saved to a Pandas dataframe and printed to the console. You can modify the program to save the data to a CSV or Excel file if desired.

Contributing
If you find any issues with the program or have ideas for how to improve it, please open an issue or submit a pull request.
