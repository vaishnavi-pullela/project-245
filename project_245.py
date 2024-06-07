from web3 import Web3
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)


infura_url = 'https://mainnet.infura.io/v3/9395889d32814da1af5759483dc15f20'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Write Code for Task 01 below.
def ethereum_block():
	number = int(block_entry.get())
	block_data = web3.eth.get_block(number)
	transaction = web3.eth.get_transaction(block_data['transactions'][-1].hex())
    value = transaction['value']
	value_in_ether = value / 10 ** 18
	value_in_dollar = value_in_ether * 3689.68

	gas = transaction['gas']

	block_entry.destroy()
	search_btn.destroy()


search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()

