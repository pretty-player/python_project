import os
import traceback
import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue, black
from datetime import datetime

def create_train_ticket_pdf(filename, ticket_data):
    try:
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4

        # Ticket Border - Make it a square box by adjusting height
        box_width = 4 * inch
        box_height = 4 * inch
        box_x = (width - box_width) / 2
        box_y = height - 5 * inch
        c.setStrokeColor(blue)
        c.setLineWidth(2)
        c.rect(box_x, box_y, box_width, box_height)
        c.setStrokeColor(black)
        c.setLineWidth(1)

        # Header
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2, box_y + box_height - 0.5 * inch, "Train Ticket")

        # Ticket Details inside the box
        c.setFont("Helvetica", 12)
        y = box_y + box_height - 1 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Passenger Name: {ticket_data.get('name', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Age: {ticket_data.get('age', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Train: {ticket_data.get('train', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"From: {ticket_data.get('from_station', '')} To: {ticket_data.get('to_station', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Date of Journey: {ticket_data.get('date', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Class: {ticket_data.get('class', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Seat Number: {ticket_data.get('seat', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Fare: ₹{ticket_data.get('fare', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Adults: {ticket_data.get('adults', '')}")
        y -= 0.25 * inch
        c.drawString(box_x + 0.2 * inch, y, f"Children: {ticket_data.get('children', '')}")

        # Footer inside the box
        c.setFont("Helvetica", 10)
        c.drawCentredString(width / 2, box_y + 0.3 * inch, "Thank you for booking with us. Safe journey!")

        c.showPage()
        c.save()
        return True, None
    except Exception as exc:
        return False, traceback.format_exc()

class TrainBookingApp:
    def __init__(self, root):
        self.root = root
        root.title("Train Ticket Booking")
        root.resizable(False, False)

        frame = tk.Frame(root, padx=12, pady=12)
        frame.pack()

        # Passenger Details
        tk.Label(frame, text="Passenger Name *").grid(row=0, column=0, sticky="w")
        self.name_var = tk.Entry(frame, width=40)
        self.name_var.grid(row=0, column=1, pady=4)

        tk.Label(frame, text="Age *").grid(row=1, column=0, sticky="w")
        self.age_var = tk.Entry(frame, width=40)
        self.age_var.grid(row=1, column=1, pady=4)

        # Train Details
        tk.Label(frame, text="Train Name/Number *").grid(row=2, column=0, sticky="w")
        self.train_var = tk.Entry(frame, width=40)
        self.train_var.grid(row=2, column=1, pady=4)

        tk.Label(frame, text="From Station *").grid(row=3, column=0, sticky="w")
        self.from_var = tk.Entry(frame, width=40)
        self.from_var.grid(row=3, column=1, pady=4)

        tk.Label(frame, text="To Station *").grid(row=4, column=0, sticky="w")
        self.to_var = tk.Entry(frame, width=40)
        self.to_var.grid(row=4, column=1, pady=4)

        tk.Label(frame, text="Date of Journey (DD/MM/YYYY) *").grid(row=5, column=0, sticky="w")
        self.date_var = tk.Entry(frame, width=40)
        self.date_var.grid(row=5, column=1, pady=4)

        tk.Label(frame, text="Class (e.g., AC, Sleeper)").grid(row=6, column=0, sticky="w")
        self.class_var = tk.Entry(frame, width=40)
        self.class_var.grid(row=6, column=1, pady=4)

        tk.Label(frame, text="Seat Number").grid(row=7, column=0, sticky="w")
        self.seat_var = tk.Entry(frame, width=40)
        self.seat_var.grid(row=7, column=1, pady=4)

        tk.Label(frame, text="Fare (₹)").grid(row=8, column=0, sticky="w")
        self.fare_var = tk.Entry(frame, width=40)
        self.fare_var.grid(row=8, column=1, pady=4)

        # Number of Adults and Children
        tk.Label(frame, text="Number of Adults").grid(row=9, column=0, sticky="w")
        self.adults_var = tk.StringVar(value="1")
        adults_options = [str(i) for i in range(1, 11)]
        tk.OptionMenu(frame, self.adults_var, *adults_options).grid(row=9, column=1, pady=4)

        tk.Label(frame, text="Number of Children").grid(row=10, column=0, sticky="w")
        self.children_var = tk.StringVar(value="0")
        children_options = [str(i) for i in range(0, 11)]
        tk.OptionMenu(frame, self.children_var, *children_options).grid(row=10, column=1, pady=4)

        # Buttons
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=11, column=0, columnspan=2, pady=(10,0))

        tk.Button(btn_frame, text="Book Ticket & Generate PDF", command=self.on_book).pack(side="left", padx=6)
        tk.Button(btn_frame, text="Quit", command=root.quit).pack(side="left", padx=6)

    def on_book(self):
        name = self.name_var.get().strip()
        age = self.age_var.get().strip()
        train = self.train_var.get().strip()
        from_station = self.from_var.get().strip()
        to_station = self.to_var.get().strip()
        date = self.date_var.get().strip()
        class_type = self.class_var.get().strip()
        seat = self.seat_var.get().strip()
        fare = self.fare_var.get().strip()
        adults = self.adults_var.get()
        children = self.children_var.get()

        if not all([name, age, train, from_station, to_station, date]):
            messagebox.showerror("Validation", "Please fill all required fields marked with *.")
            return

        # Basic date validation
        try:
            datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Validation", "Date must be in DD/MM/YYYY format.")
            return

        ticket_data = {
            "name": name,
            "age": age,
            "train": train,
            "from_station": from_station,
            "to_station": to_station,
            "date": date,
            "class": class_type,
            "seat": seat,
            "fare": fare,
            "adults": adults,
            "children": children
        }

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            initialfile=f"{name.replace(' ', '_')}_ticket.pdf",
            title="Save Ticket PDF as..."
        )
        if not file_path:
            return

        ok, err = create_train_ticket_pdf(file_path, ticket_data)
        if ok:
            messagebox.showinfo("Success", f"Train ticket PDF saved: {file_path}")
            try:
                if os.name == "nt":
                    os.startfile(file_path)
                elif os.name == "posix":
                    os.system(f"xdg-open '{file_path}'")
            except Exception:
                pass
        else:
            messagebox.showerror("Error", f"Failed to create PDF.\n\n{err}")

def main():
    root = tk.Tk()
    TrainBookingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()