# Currency Merger
**Description**

Currency Merger is a simple tool for joining values in different currencies. For example, if I have money in USD, EUR, BRL and AED, I could use this tool to see how much I have in total in USD.

This is my first project ever, I did it for a Applied Algorithmic Thinking class. It was made in Python with the libraries TKinter and Requests, as well as the API ExchangeRate.

**Algorithm explanation**

The algorithm gets the currency exchange rates from the ExchangeRate-API, and stores them in a dictionary called currency_rates, with the name of the currency as the key and exchange rate as the value. Then I have two main functions to perform the operations: currencyConvert() and convertAndAdd().
currencyConvert() will take a value, a “FromCurrency”, a “ToCurrency” and the conversion rates as arguments, and return the converted value.
convertAndAdd() will call currencyConvert() and add the returned value in a variable called “total”, which will be accumulative (will start at 0 and we will keep adding to its value) and visible on the screen. Then, the function will update the GUI (which I will talk about next). This function’s purpose is to be called by a button in the GUI.
The interaction with the user will be made through a GUI I built with the library Tkinter. It has an entry for the value, option boxes for the currencies, a button to call convertAndAdd(), a text object for the total value, and a button to reset the program (if the user wants to start adding from 0 again). The functions will take the values in the entry box and options menus as arguments, and the “total” that they’ll generate will go to the text object, which will be shown on the screen.

**References**

These are the sources I relied on while studying the libraries and implementation of my idea:

https://www.dataquest.io/blog/python-api-tutorial/ 

https://www.tutorialspoint.com/python-get-the-real-time-currency-exchange-rate 

https://www.exchangerate-api.com/docs/overview 

https://realpython.com/python-gui-tkinter/ 

https://docs.python.org/3/library/tk.html 

https://www.tutorialspoint.com/python3/python_gui_programming.htm
