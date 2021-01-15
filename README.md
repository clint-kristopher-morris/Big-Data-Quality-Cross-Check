# Big-Data-Quality-Cross-Check
### Improving Traffic Data Quality by Cross-Checking Loop-Based Data with Video Detection Data

### Web-Scrape Data from GDOT Navigators GUI
This project involved interacting with a web-based GUI through a VPN.
For extracting large amounts of data, navigating through pages with this interface is undesirably slow.
To expedite this process, I found that accessing download pages by altering the url to be a sustainable alternative.

The URL was formatted in a manner similar to this:

'http://constant_text{**VDS location mapped to a numerical value**}constant_text{**start**}constant_text{**end**}constant_text'
