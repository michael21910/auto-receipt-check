# Auto Receipt Check
This program web crawlers the receipt prize number in [this webpage](https://invoice.etax.nat.gov.tw/).  
Then, prepare the "receipt.txt" file with this python file in the same folder.  
index.py will output a dataframe, telling you the final checking result.  
  
## Small story :speech_balloon:
I think that checking receipts by human is such a waste of time.  
Thus, I wrote a program to solve this problem.  
  
## Things you need to do :open_book:
* Prepare a txt file called "receipt.txt" and input the receipt numbers you have. Something like this:    
![擷取](https://user-images.githubusercontent.com/78197510/131345936-37608da5-14f8-44b4-860f-db7b616d3bd7.PNG)
* Add this file with "index.py" in the same folder
* Wait until the result comes out
* Install the library "pandas"
```
pip install pandas
```
* Install the library "requests"
```
pip install requests
```
* Install the library "BeautifulSoup"
```
pip install BeautifulSoup
```
  
## What will you get :icecream:
A DataFrame that shows the receipt in txt file and the price you get.  
  
## Demo :eyes:
* oops, unfortunate.  
![擷取](https://user-images.githubusercontent.com/78197510/131346146-a4ab8833-cfdd-4a44-8ed3-52cf8a531e5a.PNG)  
  
## License
[MIT](LICENSE) © Tsuen Hsueh
