import tkinter as tk

class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Alarm GUI")

        self.timer_id = None

        self.title_lbl = tk.Label(
            root,
            text="Welcome to the Simple Alarm Clock Application (SACA)!",
            font="Calibri 15",
            justify="center"
        )
        self.title_lbl.grid(row=0, column=0, columnspan=3)

        self.time_mins_lbl = tk.Label(root, text="Minutes:")
        self.time_secs_lbl = tk.Label(root, text="Seconds:")
        self.time_mins_lbl.grid(row=3)
        self.time_secs_lbl.grid(row=4)

        self.mins_entry = tk.Entry(root, fg="blue")
        self.secs_entry = tk.Entry(root, fg="blue")
        self.mins_entry.grid(row=3, column=1)
        self.secs_entry.grid(row=4, column=1)

        self.msg_lbl = tk.Label(root, text="")
        self.msg_lbl.grid(row=7, columnspan=2)

        self.submit_btn = tk.Button(
            root,
            text="Submit Alarm!",
            bg="#ccfcd9",
            command=self.check_time_entries
        )
        self.submit_btn.grid(row=6, columnspan=2)


    def check_time_entries(self):
        try:
            mins = int(self.mins_entry.get() or 0)
            secs = int(self.secs_entry.get() or 0)

            if mins < 0 or secs < 0:
                raise ValueError

            total_seconds = mins * 60 + secs

            # Cancel any existing timer
            if self.timer_id is not None:
                self.msg_lbl.after_cancel(self.timer_id)
                self.timer_id = None

            self.start_countdown(total_seconds)

        except ValueError:
            self.mins_entry.delete(0, tk.END)
            self.secs_entry.delete(0, tk.END)
            self.msg_lbl.config(text="Invalid input!", fg="red")

    def start_countdown(self, total_seconds):
        if total_seconds < 0:
            self.msg_lbl.config(text="TIME'S UP!", fg="red")
            self.timer_id = None
            return

        mins = total_seconds // 60
        secs = total_seconds % 60

        self.msg_lbl.config(
            text=f"{mins:02d}:{secs:02d}",
            fg="black"
        )

        self.timer_id = self.msg_lbl.after(
            1000,
            self.start_countdown,
            total_seconds - 1
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()