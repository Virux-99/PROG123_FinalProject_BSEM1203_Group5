import tkinter as t_k                               #imports library tkinter with nickname
from tkinter import messagebox, ttk                 #imports modules from tkinter
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as mpl                     #imports chart library and creation as mpl
from datetime import datetime                       #imports present date tracking tool

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from save import (save_client_records,
                  save_stock_records,
                  load_clients_from_json,
                  load_stocks_from_json)            #imports functions from modules

from input_v import validate_client_data,validate_stock_data

from save import load_clients_from_json, load_stocks_from_json
transactions_queue = load_clients_from_json()
stock_queue = load_stocks_from_json()

window  = t_k.Tk()                                  #creates window from tknitker/tk and assigns it to varable window
window .title("Market Management System")           #titles window
window .geometry("1000x700")                        #sets windows size to 1000*700
window.configure(bg="purple",)
window .resizable(True, True)                       #allows to resize the windows width and hight

app_name = "Market Management System"               #assigns market management system to varable app_name
VERSION = "1.0"                                     #assigns varable version to one

def clear_window():                                 #defines function
    for widget in window.winfo_children():          #distroys/clears everything on screen
        widget.destroy()

#-------------------clients---------------------------
def record_clients():                                                #defines function record clients
    clear_window()
    client_frame = t_k.Frame(window,bg="lightgreen",)                #creates and displays frame on window
    client_frame.pack(fill="both",expand=True)

    form_frame = t_k.Frame(client_frame)                             #helps to center input boxes
    form_frame.pack(expand=True)

    title = t_k.Label(form_frame,                                    #creates label on client_frame and assigns it to title
        text="Record Client Transaction",                            #text on label
        font=("Arial", 16, "bold"))                                  #text font
    title.grid(row=0, column=0, columnspan=2, pady=10)               #text positioning

    (t_k.Label(form_frame, text="Client_Number", fg="black")         #creates clinat_no frame and input box
     .grid(row=1, column=0, sticky="e", padx=10, pady=5))
    client_number_entry = t_k.Entry(form_frame)
    client_number_entry.grid(row=1, column=1, pady=5)

    (t_k.Label(form_frame, text="Client Name", fg="black")
    .grid(row=2, column=0, sticky="e", padx=10, pady=5))
    name_entry = t_k.Entry(form_frame)                               #creates input box on client frame,store it in name_entry
    name_entry.grid(row=2, column=1, pady=5)                         #shows frame

    (t_k.Label(form_frame, text="Goods", fg="black")
    .grid(row=3, column=0, sticky="e", padx=10, pady=5))
    goods_entry = t_k.Entry(form_frame)                              #creates input box on client frame,store it in goods_entry
    goods_entry.grid(row=3, column=1, pady=5)                        #shows frame

    (t_k.Label(form_frame, text="Quantity", fg="black")
    .grid(row=4, column=0, sticky="e", padx=10, pady=5))
    quantity_entry = t_k.Entry(form_frame)                           #creates input box on client frame,store it in quantity_entry
    quantity_entry.grid(row=4, column=1, pady=5)                     #shows frame

    (t_k.Label(form_frame, text="Total", fg="black")
    .grid(row=5, column=0, sticky="e", padx=10, pady=5))
    total_entry = t_k.Entry(form_frame)                              #creates input box on client frame,store it in total_entry
    total_entry.grid(row=5, column=1, pady=5)                        #shows frame

    (t_k.Label(form_frame, text="Ammount paid", fg="black")
    .grid(row=6, column=0, sticky="e", padx=10, pady=5))
    paid_entry = t_k.Entry(form_frame)                               #creates input box on client frame,store it in paid_entry
    paid_entry.grid(row=6, column=1, pady=5)                         #shows frame

    (t_k.Label(form_frame, text="Date (YYYY-MM-DD)", fg="black")
     .grid(row=7, column=0, sticky="e", padx=10, pady=5))
    date_entry = t_k.Entry(form_frame)
    date_entry.grid(row=7, column=1, pady=5)

    button_frame = t_k.Frame(client_frame)
    button_frame.pack(fill="x", side="bottom")
    exit_button = t_k.Button(
        button_frame,
        text="Exit",
        command=main_menu,
        bg="red",
        fg="white"
    )

    exit_button.pack(side="right", padx=20, pady=10)

    def save_client():

        client_number = client_number_entry.get()
        name = name_entry.get()
        goods = goods_entry.get()
        quantity = quantity_entry.get()
        total = total_entry.get()
        paid = paid_entry.get()

        date = date_entry.get()
        if date.strip() == "":
            date = datetime.now().strftime("%Y-%m-%d")

        try:
            client_number = int(client_number)
            quantity = int(quantity)
            total = float(total)
            paid = float(paid)
        except ValueError:
            messagebox.showerror("Error", "Invalid number input detected")
            return

        remaining_am = total - paid

        if remaining_am < 0:
            messagebox.showerror("Error", "No negative remainders allowed")
            return

        status = "Complete" if remaining_am == 0 else "Due"

        data = {
            "client_number": client_number,
            "name": name,
            "goods": goods,
            "quantity": quantity,
            "total": total,
            "paid": paid,
            "remaining": remaining_am,
            "status": status,
            "date": date
        }

        save_client_records(transactions_queue, data)

        client_number_entry.delete(0, t_k.END)                      # clear inputs
        name_entry.delete(0, t_k.END)
        goods_entry.delete(0, t_k.END)
        quantity_entry.delete(0, t_k.END)
        total_entry.delete(0, t_k.END)
        paid_entry.delete(0, t_k.END)
        date_entry.delete(0, t_k.END)

    title_label = t_k.Label(                                              #creates the title at the top of th menu
        client_frame,
        text="Market Registration System",                                #title name
        font=("Arial", 20, "bold")                                        #title discription
    )
    title_label.pack(pady=20)                                             #show on screen with spacing

    save_button = t_k.Button(
        form_frame,
        text="Save Client",
        command=save_client,
        bg="green",
        fg="white",
        font=("Arial", 12, "bold")
    )
    save_button.grid(row=8, column=0, columnspan=2, pady=15)

#-------------------stocks---------------------
def record_stocks():                                                        #record stocks defination
    clear_window()                                                          #removes every thing on present screen
    stock_frame = t_k.Frame(window, bg="lightcoral")
    stock_frame.pack(fill="both", expand=True)

    form_frame = t_k.Frame(stock_frame)
    form_frame.pack(expand=True)

    title = t_k.Label(form_frame,
        text="Record Stocks", font=("Arial", 16, "bold"))                   #record stocks heading and properties
    title.grid(row=0, column=0, columnspan=2, pady=10)

    (t_k.Label(form_frame, text="Stock Name")                               #creates stock Name input box
     .grid(row=1, column=0, sticky="e", padx=10, pady=5))
    stock_name_entry = t_k.Entry(form_frame)
    stock_name_entry.grid(row=1, column=1, pady=5)

    (t_k.Label(form_frame, text="Stock Amount")                             #creates stock Ammount input box
     .grid(row=2, column=0, sticky="e", padx=10, pady=5))
    stock_amount_entry = t_k.Entry(form_frame)
    stock_amount_entry.grid(row=2, column=1, pady=5)

    (t_k.Label(form_frame, text="Cost Price")                               #creates stock Cost Price input box
    .grid(row=3, column=0, sticky="e", padx=10, pady=5))
    cost_price_entry = t_k.Entry(form_frame)
    cost_price_entry.grid(row=3, column=1, pady=5)

    (t_k.Label(form_frame, text="Selling Price")                            #creates stock Selling Price input box
     .grid(row=4, column=0, sticky="e", padx=10, pady=5))
    selling_price_entry = t_k.Entry(form_frame)
    selling_price_entry.grid(row=4, column=1, pady=5)

    def save_stock():
        try:
            stock_name = stock_name_entry.get()
            stock_amount = int(stock_amount_entry.get())
            cost_price = float(cost_price_entry.get())
            selling_price = float(selling_price_entry.get())

            data = {
                "stock_name": stock_name,
                "stock_amount": stock_amount,
                "cost_price": cost_price,
                "selling_price": selling_price
            }

            save_stock_records(stock_queue, data)

            stock_name_entry.delete(0, t_k.END)                                #clears input boxes arter saving
            stock_amount_entry.delete(0, t_k.END)
            cost_price_entry.delete(0, t_k.END)
            selling_price_entry.delete(0, t_k.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid"
                                 " stock values")

    save_button = t_k.Button(
        form_frame,
        text="Save Stock",
        command=save_stock,
        bg="green",
        fg="white"
    )
    save_button.grid(row=5,column=0,columnspan=2,pady=15)

#--------------------View------------------------
def view():
    clear_window()

    frame = t_k.Frame(window, bg="lightblue")
    frame.pack(fill="both", expand=True)

    title = t_k.Label(frame, text="View Records/Charts", font=("Arial", 20, "bold"), bg="lightblue")
    title.pack(pady=20)

    def view_clients():
        print(transactions_queue )
        clear_window()

        frame = t_k.Frame(window, bg="lightblue")
        frame.pack(fill="both", expand=True)

        t_k.Label(frame, text="Client Records", font=("Arial", 20, "bold")).pack(pady=10)

#------------------client_records scroll_bar------------------
        canvas = t_k.Canvas(frame)
        scrollbar = t_k.Scrollbar(frame, orient="vertical", command=canvas.yview)

        scrollable_frame = t_k.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

#-----------------button_frame-------------------------
        button_frame = t_k.Frame(frame)
        button_frame.pack(side="bottom", fill="x")

#------------records_ordering_output-------------------
        for client in transactions_queue:
            text = (
                f"Client No: {client['client_number']} | "
                f"Name: {client['name']} | "
                f"Goods: {client['goods']} | "
                f"Qty: {client['quantity']} | "
                f"Total: {client['total']} | "
                f"Paid: {client['paid']} | "
                f"Remaining: {client['remaining']} | "
                f"Status: {client['status']} | "
                f"Date: {client['date']}"
            )

            t_k.Label(scrollable_frame, text=text, anchor="w", justify="left").pack(anchor="w", padx=10, pady=2)

        exit_button = t_k.Button(                                          #creates exit button to move back to view pannel
            button_frame,
            text="Exit",
            command=view,
            bg="red",
        )
        exit_button.pack(side="right",padx=10,pady=10)


    def view_stocks():
        print(stock_queue)
        clear_window()

        frame = t_k.Frame(window, bg="lightyellow")
        frame.pack(fill="both", expand=True)

        t_k.Label(frame, text="Stock Records", font=("Arial", 20, "bold")).pack(pady=10)

#------------------stock_records scrool_bar---------------------
        canvas = t_k.Canvas(frame)
        scrollbar = t_k.Scrollbar(frame, orient="vertical", command=canvas.yview)

        scrollable_frame = t_k.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

#---------------stocks_button_frame----------------------------
        button_frame = t_k.Frame(frame)
        button_frame.pack(side="bottom", fill="x")


        for stock in stock_queue:                                                       #formats stock records to appear in an ordaly manner
            text = (
                f"Stock: {stock['stock_name']} | "
                f"Amount: {stock['stock_amount']} | "
                f"Cost: {stock['cost_price']} | "
                f"Sell: {stock['selling_price']} | "
                f"Profit: N/A"
            )

            t_k.Label(scrollable_frame, text=text, anchor="w", justify="left").pack(anchor="w", padx=10, pady=2)

        exit_button = t_k.Button(                                                       #creates exit button to move back to view pannel
            button_frame,
            text="Exit",
            command=view,
            bg="red",
        )
        exit_button.pack(side="right",padx=10,pady=10)

    def view_charts():
        clear_window()

        frame = t_k.Frame(window, bg="lightgray")
        frame.pack(fill="both", expand=True)
        t_k.Label(frame, text="Charts Menu", font=("Arial", 20, "bold")).pack(pady=20)

        bottom_frame = t_k.Frame(frame, bg="lightgray")
        bottom_frame.pack(side="bottom", fill="x")

        #----------------piechart_code------------
        def stocks_pie_chart():
            clear_window()

            window.title("Top 10 Goods Sold")

            # ---------------- OUTER FRAME ----------------
            root = t_k.Frame(window)
            root.pack(fill="both", expand=True)

            # ---------------- TOP BLACK BAR ----------------
            top_frame = t_k.Frame(root, bg="black", height=50)
            top_frame.pack(side="top", fill="x")

            top_frame.pack_propagate(False)

            # EXIT BUTTON (TOP LEFT)
            t_k.Button(
                top_frame,
                text="Exit",
                command=view_charts,
                bg="red",
                fg="white"
            ).pack(side="left", padx=10, pady=10)

            # ---------------- MIDDLE WHITE AREA ----------------
            middle_frame = t_k.Frame(root, bg="white")
            middle_frame.pack(side="top", fill="both", expand=True)

            t_k.Label(
                middle_frame,
                text="Top 10 Goods Sold",
                font=("Arial", 20, "bold"),
                bg="white"
            ).pack(pady=10)

            # ---- PIE CHART ----
            goods_count = {}

            for client in transactions_queue:
                goods = client.get("goods", "")
                qty = client.get("quantity", 0)

                if goods:
                    goods_count[goods] = goods_count.get(goods, 0) + qty

            top_goods = sorted(goods_count.items(), key=lambda x: x[1], reverse=True)[:10]

            labels = [g[0] for g in top_goods]
            values = [g[1] for g in top_goods]

            colors = [
                "red",
                "green",
                "blue",
                "orange",
                "purple",
                "cyan",
                "yellow",
                "magenta",
                "lime",
                "pink"
            ]

            fig, ax = mpl.subplots()

            ax.pie(
                values,
                colors=colors[:len(values)],
                startangle=90
            )

            ax.set_title("Pie Chart")

            canvas = FigureCanvasTkAgg(fig, master=middle_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

            # ---------------- BOTTOM BLACK LIST AREA ----------------
            bottom_frame = t_k.Frame(root, bg="black", height=200)
            bottom_frame.pack(side="bottom", fill="x")

            bottom_frame.pack_propagate(False)

            # Scrollable list container
            canvas_scroll = t_k.Canvas(bottom_frame, bg="black", highlightthickness=0)
            scrollbar = t_k.Scrollbar(bottom_frame, orient="vertical", command=canvas_scroll.yview)

            scroll_frame = t_k.Frame(canvas_scroll, bg="black")

            scroll_frame.bind(
                "<Configure>",
                lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
            )

            canvas_scroll.create_window((0, 0), window=scroll_frame, anchor="nw")
            canvas_scroll.configure(yscrollcommand=scrollbar.set)

            canvas_scroll.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            colors = [
                "red",
                "green",
                "blue",
                "orange",
                "purple",
                "cyan",
                "yellow",
                "magenta",
                "lime",
                "pink"
            ]

            t_k.Label(
                scroll_frame,
                text="Top 10 Goods Sold",
                fg="white",
                bg="black",
                font=("Arial", 14, "bold")
            ).pack(anchor="w", padx=10, pady=5)

            for i, (name, qty) in enumerate(top_goods):
                color = colors[i % len(colors)]

                t_k.Label(
                    scroll_frame,
                    text=f"{i + 1}. {name} - {qty}",
                    fg=color,
                    bg="black",
                    font=("Arial", 11, "bold")
                ).pack(anchor="w", padx=10, pady=2)

#-----------------montly_profit------------------
        def monthly_profit():
            clear_window()

            window.title("Monthly Profit Chart")

            root = t_k.Frame(window, bg="white")
            root.pack(fill="both", expand=True)

# ---------------- TOP BAR ----------------
            top_frame = t_k.Frame(root, bg="black", height=50)
            top_frame.pack(side="top", fill="x")
            top_frame.pack_propagate(False)

            t_k.Label(
                top_frame,
                text="Monthly Profit Chart",
                fg="white",
                bg="black",
                font=("Arial", 16, "bold")
            ).pack(side="left", padx=10)

            t_k.Button(
                top_frame,
                text="Exit",
                command=view_charts,
                bg="red",
                fg="white"
            ).pack(side="right", padx=10)

#-------------- MIDDLE AREA ---------------
            middle_frame = t_k.Frame(root, bg="white")
            middle_frame.pack(fill="both", expand=True)

#----------- STOCK PRICE LOOKUP -----------
            stock_lookup = {}

            for stock in stock_queue:
                name = stock["stock_name"]
                cost = stock["cost_price"]
                sell = stock["selling_price"]
                stock_lookup[name] = (cost, sell)

# -----------MONTHLY PROFIT CALCULATION -----------
            monthly = {}

            for client in transactions_queue:
                date = client.get("date", "")
                if not date:
                    continue

                month = date[:7]  # YYYY-MM

                goods = client.get("goods", "")
                qty = client.get("quantity", 0)

                if goods in stock_lookup:
                    cost, sell = stock_lookup[goods]
                    profit = (sell - cost) * qty
                else:
                    profit = 0

                monthly[month] = monthly.get(month, 0) + profit

            # sort months properly
            months = sorted(monthly.keys())
            profits = [monthly[m] for m in months]

# ------------------BAR CHART---------------------
            fig, ax = mpl.subplots(figsize=(8, 4))

            ax.bar(months, profits, color="blue")

            ax.set_xlabel("Month")
            ax.set_ylabel("Profit")
            ax.set_title("Monthly Profit Bar Chart")

            fig.autofmt_xdate()

            canvas = FigureCanvasTkAgg(fig, master=middle_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

#--------------pie_chart_button--------------
        t_k.Button(
            frame,
            text="Stocks (Pie Chart)",
            command=stocks_pie_chart,
            bg="green",
            fg="white",
            width=30
        ).pack(pady=10)

#----------------montly_profit_buttom---------
        t_k.Button(
            frame,
            text="Monthly Profits (Bar Chart)",
            command=monthly_profit,
            bg="blue",
            fg="white",
            width=30
        ).pack(pady=10)
#----------view_chart_exit_button--------------------
        t_k.Button(
            frame,
            text="Exit",
            command=view,
            bg="red",
            fg="white",
            width=30
        ).pack(pady=10)

#----------------creating_view_buttons----------------
    t_k.Button(
        frame,
        text="View Client Records",
        command=view_clients,
        bg="green",
        fg="white",
        width=25
    ).pack(pady=10)

    t_k.Button(
        frame,
        text="View Stock Records",
        command=view_stocks,
        bg="orange",
        fg="white",
        width=25
    ).pack(pady=10)

    t_k.Button(
        frame,
        text="View charts",
        command=view_charts,
        bg="blue",
        fg="white",
        width=25
    ).pack(pady=10)

    back_button = t_k.Button(frame,
        text="Exit",
        command=main_menu,
        bg="red",
        fg="white",
        width=25
    ).pack(pady=10)

#------------search_records_function------------
def search_records():
    clear_window()

    frame = t_k.Frame(window, bg="lightblue")
    frame.pack(fill="both", expand=True)

    # ---------------- HEADING ----------------
    t_k.Label(
        frame,
        text="Input Values to Filter Records",
        font=("Arial", 20, "bold"),
        bg="lightblue"
    ).pack(pady=10)

    # ---------------- FORM ----------------
    form = t_k.Frame(frame, bg="lightblue")
    form.pack(pady=10)

    # MONTH
    t_k.Label(form, text="Input Month:", bg="lightblue").grid(row=0, column=0, sticky="e")
    month_var = t_k.StringVar()
    month_box = ttk.Combobox(form, textvariable=month_var)
    month_box['values'] = [
        "", "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]
    month_box.grid(row=0, column=1)

    # YEAR
    t_k.Label(form, text="Input Year (e.g. 2026):", bg="lightblue").grid(row=1, column=0, sticky="e")
    year_entry = t_k.Entry(form)
    year_entry.grid(row=1, column=1)

    # DAY
    t_k.Label(form, text="Input Day (1–31):", bg="lightblue").grid(row=2, column=0, sticky="e")
    day_entry = t_k.Entry(form)
    day_entry.grid(row=2, column=1)

    # STATUS
    t_k.Label(form, text="Input Status (Complete / Due):", bg="lightblue").grid(row=3, column=0, sticky="e")
    status_var = t_k.StringVar()
    status_box = ttk.Combobox(form, textvariable=status_var)
    status_box['values'] = ["", "Complete", "Due"]
    status_box.grid(row=3, column=1)

    # ---------------- ERROR DISPLAY ----------------
    error_label = t_k.Label(frame, text="", fg="red", bg="lightblue", justify="left")
    error_label.pack(pady=5)

    # ---------------- RESULT AREA ----------------
    result_frame = t_k.Frame(frame, bg="white")
    result_frame.pack(fill="both", expand=True)

    # ---------------- SEARCH FUNCTION ----------------
    def run_search():
        for w in result_frame.winfo_children():
            w.destroy()

        errors = []

        month = month_var.get().strip()
        year = year_entry.get().strip()
        day = day_entry.get().strip()
        status = status_var.get().strip()

        month_map = {
            "January":"01","February":"02","March":"03","April":"04",
            "May":"05","June":"06","July":"07","August":"08",
            "September":"09","October":"10","November":"11","December":"12"
        }

        # ---------------- VALIDATION ----------------

        if month and month not in month_map:
            errors.append("Please input a valid month")

        if year:
            if not year.isdigit():
                errors.append("Year must be a number")
            else:
                if not any(c["date"][:4] == year for c in transactions_queue):
                    errors.append("No client transactions in this year")

        if day:
            if not day.isdigit():
                errors.append("Day must be a number")
            else:
                d = int(day)
                if d < 1 or d > 31:
                    errors.append("Please input a valid day (1–31)")

        if status and status not in ["Complete", "Due"]:
            errors.append("Please input valid status")

        # ---------------- SHOW ERRORS ----------------
        if errors:
            error_label.config(text="\n".join(errors))
            return

        # ---------------- FILTER ----------------
        results = []

        for c in transactions_queue:
            date = c["date"]
            c_year = date[:4]
            c_month = date[5:7]
            c_day = date[8:10]

            if month and month_map.get(month) != c_month:
                continue

            if year and year != c_year:
                continue

            if day and int(day) != int(c_day):
                continue

            if status and status != c["status"]:
                continue

            results.append(c)

        # ---------------- NO RESULTS ----------------
        if not results:
            error_label.config(text="No matching records found")
            return

        # ---------------- DISPLAY RESULTS ----------------
        canvas = t_k.Canvas(result_frame)
        scroll = t_k.Scrollbar(result_frame, command=canvas.yview)
        scroll_frame = t_k.Frame(canvas)

        scroll_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)

        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        for c in results:
            t_k.Label(
                scroll_frame,
                text=f"{c['date']} | {c['name']} | {c['goods']} | {c['status']}",
                bg="white",
                anchor="w"
            ).pack(fill="x", padx=5, pady=2)

    # ---------------- BUTTONS ----------------
    t_k.Button(frame,
        text="Search",
        command=run_search,
        bg="green",
        fg="white"
    ).pack(pady=10)

    t_k.Button(frame,
        text="Exit",
        command=view,
        bg="red",
        fg="white"
    ).pack(pady=5)

#------------------Main_menu----------------------
def main_menu():
    clear_window()

    menu_frame = t_k.Frame(window, bg="purple")
    menu_frame.pack(fill="both", expand=True)

    t_k.Label(
        menu_frame,
        text="Market Registration System",
        font=("Arial", 20, "bold"),
        bg="purple"
    ).pack(pady=20)

    t_k.Button(
        menu_frame,
        text="Record Clients",
        command=record_clients,
        bg="green"
    ).pack(pady=10)

    t_k.Button(
        menu_frame,
        text="Record Stocks",
        command=record_stocks,
        bg="red"
    ).pack(pady=10)

    t_k.Button(
        menu_frame,
        text="View",
        command=view,
        bg="blue"
    ).pack(pady=10)

    t_k.Button(
        menu_frame,
        text="Search Records",
        command=search_records,
        bg="orange"
    ).pack(pady=10)

    t_k.Button(
        menu_frame,
        text="Exit",
        command=window.quit,
        bg="yellow"
    ).pack(pady=10)

#--------------------logins----------------------
def login_screen():                                                       #defines/creates function logic_screen
    login_frame = t_k.Frame(window,bg="pink" )                            #acesses a continar inside window from tkintker and assigns it to logic frame
    login_frame.pack(expand=True)                                         #shows frame in window

    title_label = t_k.Label(                                              #creates text lable
        login_frame,                                                      #puts the label inside login frame
        text="Market Management System",                                  #assigns market managment system to varable text
        font=("Arial", 20, "bold")                                        #discribe font of the text
    )                                                                     #closes label
    title_label.pack(pady=20)                                             #dislays title with spacing

    username_label = t_k.Label(
        login_frame,                                                      #creates username label
        text="Username"
    )
    username_label.pack()                                                 #shows username label

    username_entry = t_k.Entry(login_frame)                               #creates input box for username
    username_entry.pack(pady=5)                                           #displays input box with spacing

    password_label = t_k.Label(
        login_frame,                                                      #creates password label
        text="Password"
    )
    password_label.pack()                                                 #shows password label

    password_entry = t_k.Entry(
        login_frame,                                                      #creates password input box showing ****
        show="*"
    )
    password_entry.pack(pady=5)                                           #displays pasword input box with spacing

    def login():                                                          #defines login function
        username = username_entry.get()                                   #gets users user nsme
        password = password_entry.get()                                   #and password

        if username == "Admin" and password == "91191191":                #checkes for crrect login details
            messagebox.showinfo("successful"
            )
            clear_window()                                                #clears everything on screen
            main_menu()                                                   #opens main menu window
        elif username == "Staff" and password == "1234":
            messagebox.showinfo("welcome"
            )
            clear_window()
            main_menu()
        else:
            messagebox.showerror(                                           #shows earror popup message for unsucessful login
                "Error",
                "Invalid Username or Password"
            )

    login_button = t_k.Button(                                              #creates login button thats runs the login function when clicked
        login_frame,
        text="Login",
        command=login
    )
    login_button.pack(pady=20)                                              #shows login button on screen

login_screen()                                                              #runs login screen function
window .mainloop()                                                          #keeps window open and running