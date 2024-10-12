# Web Scraper Script

This is a Python-based web scraper that retrieves data from web pages. The script runs up to 20 pages by default, but the functionality to scrape all available pages is provided in the `infinite_page.py` module.

## Features

- Scrapes data from multiple pages of a website.
- Configurable page limits (default is 20 pages).
- Infinite scraping functionality available.

## Setup

### Prerequisites

Make sure you have Python 3.x installed and `pip` to manage Python packages.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rishabh-jain28/isitca.git
    cd isitca
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Default Mode (20 pages)

To run the script with a maximum of 20 pages:

```bash
python main.py
