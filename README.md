# Big-Data-Quality-Cross-Check
### Improving Traffic Data Quality by Cross-Checking Loop-Based Data with Video Detection Data

### Web-Scrape Data from GDOT Navigators GUI
This project involved interacting with a web-based GUI through a VPN.
For extracting large amounts of data, navigating through pages with this interface is undesirably slow.
To expedite this process, I found that accessing download pages by altering the url to be a sustainable alternative.

The URL was formatted in a manner similar to this:
```
f'http://constant_text{VDS_location_mapped_to_a_numerical_value}constant_text{start}constant_text{end}constant_text'
```
I found that this numerical mapping could be found on another page.
So, my first step was to access this page and collect data on all VDS locations. 
This HTML feature multiple scrollable selection sections that needed to be interacted with a web driver.
An example of this page can be see below:

![alt text](https://i.ibb.co/y6Yyx0f/blocked-list-GUI.png)
