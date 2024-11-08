
# Top Movies Scraper

A Python script that scrapes the "Greatest Movies of All Time" list from an archived Empire Online page and saves the movie titles in a text file, creating an accessible ranked list.

## Features
- **Web Scraping**: Retrieves movie titles from an archived webpage on Empire Online.
- **File Output**: Saves the titles to a text file (`top_movies.txt`) in ranked order.

## Prerequisites

- **Python 3.x**
- **Python Libraries**:
  - BeautifulSoup (for web scraping)
  - Requests (for sending HTTP requests)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/top_movies_scraper.git
   ```
2. Navigate into the project directory:
   ```
   cd top_movies_scraper
   ```
3. Install the required libraries:
   ```
   pip install beautifulsoup4 requests
   ```

## Usage

1. Run the script:
   ```
   python movies.py
   ```
2. After running the script, a file named `top_movies.txt` will be created in the project directory. This file contains the list of top movies in ranked order.

## Code Overview

- **movies.py**: This script does the following:
  - Sends a request to an archived version of Empire Online's top movies list.
  - Parses the page content with BeautifulSoup to extract movie titles.
  - Reverses the list to create a ranked order (1st to last) and saves it to `top_movies.txt`.

## License

This project is licensed under the MIT License. Feel free to modify and use it as you like.
