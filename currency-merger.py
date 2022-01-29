import os
import sys
import tkinter
import requests


def currencyConvert(value, fromCurrency, toCurrency, conversion_rates):  # This function converts currencies
    return value / conversion_rates[fromCurrency] * conversion_rates[toCurrency]


def convertAndAdd(total_local):  # This function will call currencyConvert() and display the values in the tkinter GUI.
    #  It will also accumulate the value in a variable, so we can get the addition of several currencies.
    global total
    total = total_local
    # Created a global total and a local total (with the same value)
    # Because then we can use one of them as auxiliary, to keep adding the value instead of replacing it.
    value = float(ValueEntry.get())  # Takes the value that is in the box (typed by the user).
    FromCurrency = FromCurrencyVar.get()  # Takes the value in the FromCurrency options menu.
    ToCurrency = ToCurrencyVar.get()  # Takes the value in the ToCurrency options menu.
    total += currencyConvert(value, FromCurrency, ToCurrency, conversion_rates)  # Calls the conversion function and
    #  accumulates the result in the variable "total".
    TotalText.delete(1.0, 'end')  # Erases the old value.
    TotalText.insert(1.0, f'{total:.2f} {ToCurrency}')  # Inserts the new value.


def disable_menu(menu):  # This function disables an options menu
    menu.configure(state='disabled')


def restart():  # This function is just to restart the program. A "reset" button will call it.
    python = sys.executable
    os.execl(python, python, *sys.argv)


url_usd = 'https://v6.exchangerate-api.com/v6/ee7bdb6cb32984a03320c649/latest/USD'  # ExchangeRate-API
data = (requests.get(url_usd)).json()  # This request returns a JSON object (key:value pairs)
conversion_rates = data["conversion_rates"]  # The value of the key "conversion_rates" is a dictionary.

# Below this point, it is the GUI "design". I wont comment every single line because most of it is intuitive.
# There are labels, an entry box, options menu for the currencies and buttons (that call functions when clicked).

main_window = tkinter.Tk()
main_window.title("Arthur\'s currency converter")
main_window.geometry('640x480')

appName = tkinter.Label(main_window, text='Currency Converter', font=('arial', 25, 'bold', 'underline'), fg='blue')
appName.place(x=200, y=50)

ValueLabel = tkinter.Label(main_window, text="Value: ", relief='raised')
ValueLabel.place(x=195, y=154)
ValueEntry = tkinter.Entry(main_window, bd=4)
ValueEntry.insert(1, 0)
ValueEntry.place(x=250, y=150)

FromCurrencyLabel = tkinter.Label(main_window, text="From currency: ", relief='raised')
FromCurrencyLabel.place(x=195, y=200)
FromCurrencyVar = tkinter.StringVar()  # This will hold a str variable for the option menu
FromCurrencyVar.set('USD')  # USD as the default value
FromCurrencyMenu = tkinter.OptionMenu(main_window, FromCurrencyVar, *conversion_rates)
FromCurrencyMenu.place(x=310, y=200)

ToCurrencyLabel = tkinter.Label(main_window, text="To currency: ", relief='raised')
ToCurrencyLabel.place(x=205, y=245)
ToCurrencyVar = tkinter.StringVar()  # This will hold a str variable for the option menu
ToCurrencyVar.set('USD')  # USD is set as the default value
ToCurrencyMenu = tkinter.OptionMenu(main_window, ToCurrencyVar, *conversion_rates)
ToCurrencyMenu.place(x=310, y=245)

TotalLabel = tkinter.Label(main_window, text="TOTAL: ", relief='raised')
TotalLabel.place(x=205, y=325)
TotalText = tkinter.Text(main_window, height=4, width=12, font=("arial", 15, "bold"))
TotalText.place(x=310, y=325)
total = 0  # initializing the total value

button = tkinter.Button(main_window, text='Convert and add', height=2,
                        command=lambda: [convertAndAdd(total), disable_menu(ToCurrencyMenu)])
button.place(x=265, y=435)  # The argument "command" above specifies the functions that this button will call.

button = tkinter.Button(main_window, text='Reset', height=2,
                        command=lambda: [restart()])  # Restart button.
button.place(x=400, y=435)

main_window.mainloop()
