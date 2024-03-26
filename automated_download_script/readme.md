# Automated File Download Script

This Python script automates the process of downloading a text file from a webpage using Selenium.

## Prerequisites

- Python 3.x installed on your system
- Selenium library installed (`pip install selenium webdriver_manager`)
- Chrome WebDriver installed and its path added to your system's PATH (for Chrome browser)

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python libraries using pip: selenium, webdriver_manager

# Notes
This python script does not require a link to your chromewebdriver executable.
```
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```
takes care of this for you.