
import tkinter as tk
from currency_converter import CurrencyConverter

converter = CurrencyConverter()
from tkinter import ttk

# App window
root = tk.Tk()
root.title("My Currency Converter")
root.geometry("550x700")
root.minsize(550, 700)
root.resizable(True, True)
root.configure(bg="#F0F4F8")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="Currency Converter",
    font=("Segoe UI", 22, "bold"),
    bg="#F0F4F8",
    fg="#243B53"
)
heading.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Convert currencies with ease",
    font=("Segoe UI", 10),
    bg="#F0F4F8",
    fg="#627D98"
)
subtitle.pack(pady=(0, 20))

# Main card
card = tk.Frame(root, bg="white", padx=25, pady=20)
card.pack(fill="x", padx=30)

tk.Label(
    card, text="From Currency",
    font=("Segoe UI", 11, "bold"),
    bg="white", fg="#243B53"
).pack(anchor="w")

from_currency = ttk.Combobox(
    card, values=["USD", "INR", "EUR", "GBP", "JPY"],
    state="readonly", font=("Segoe UI", 11)
)
from_currency.set("USD")
from_currency.pack(fill="x", pady=(5, 15))

tk.Label(
    card, text="To Currency",
    font=("Segoe UI", 11, "bold"),
    bg="white", fg="#243B53"
).pack(anchor="w")

to_currency = ttk.Combobox(
    card, values=["USD", "INR", "EUR", "GBP", "JPY"],
    state="readonly", font=("Segoe UI", 11)
)
to_currency.set("INR")
to_currency.pack(fill="x", pady=(5, 15))

tk.Label(
    card, text="Amount",
    font=("Segoe UI", 11, "bold"),
    bg="white", fg="#243B53"
).pack(anchor="w")

amount_entry = ttk.Entry(card, font=("Segoe UI", 12))
amount_entry.pack(fill="x", pady=(5, 15))

result_label = tk.Label(
    root,
    text="Your result will appear here",
    font=("Segoe UI", 13, "bold"),
    bg="#F0F4F8",
    fg="#3157D5",
    wraplength=440
)
result_label.pack(pady=20)

def convert_currency():
    try:
        amount = float(amount_entry.get().strip())

        if amount <= 0:
            result_label.config(
                text="Please enter an amount greater than zero."
            )
            return

        source = from_currency.get()
        target = to_currency.get()

        result = converter.convert(amount, source, target)

        result_label.config(
            text=f"{amount:.2f} {source} = {result:.2f} {target}"
        )

    except ValueError:
        result_label.config(text="Please enter a valid number.")

    except Exception:
        result_label.config(
            text="Conversion failed. Check currencies and rate data."
        )


def swap_currencies():
    source = from_currency.get()
    target = to_currency.get()
    from_currency.set(target)
    to_currency.set(source)


def clear_fields():
    amount_entry.delete(0, tk.END)
    result_label.config(text="Your result will appear here")

button_frame = tk.Frame(root, bg="#F0F4F8")
button_frame.pack()

ttk.Button(
    button_frame,
    text="Convert",
    command=convert_currency
).pack(side="left", padx=5)

ttk.Button(
    button_frame,
    text="Swap",
    command=swap_currencies
).pack(side="left", padx=5)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
).pack(side="left", padx=5)

root.mainloop()