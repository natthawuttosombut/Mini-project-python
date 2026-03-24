
import tkinter as tk
import os
from tkinter import ttk, messagebox


from main1 import ACCENT, CARD, TEXT

LOG_FILE = "done_log.txt"

# colors
BG = "#f0f0f0"
PANEL = "#d6d6d6"
FONT_H = ("Arial", 18)
FONT_M = ("Arial", 12)
FONT_S = ("Arial", 10)
class main_app(tk.Tk):

  #use this size only
  def __init__(self):
    super().__init__()
    self.withdraw()
    self.title("TO DO LIST")
    self.geometry("600x700")
    self.iconbitmap("img/logo.ico")
    self.resizable(False, False)
    self.configure(bg=BG)
    self.tasks: list[dict] = []
    self._build_ui()

    #button
    self.btn = tk.Frame(self, bg=BG)
    self.btn.pack(fill="x", pady=10, padx=8,side="bottom") 
    self.viewlogBTN()  
    self.deiconify()

  def _build_ui(self):
    # Header
    header = tk.Frame(self, bg=BG, pady=20)
    header.pack(fill="x")
    tk.Label(header, text="TO DO LIST", font=FONT_H, bg=BG).pack()
    tk.Label(header, text="Enter the tasks to be done.", font=FONT_S, bg=BG).pack()

    # Input
    input_frame = tk.Frame(self, bg=PANEL,padx=20, pady=10)
    input_frame.pack(fill="x", padx=20)

    self.entry_var = tk.StringVar()
    entry = tk.Entry(input_frame, textvariable=self.entry_var,
      font=FONT_M, bg=CARD, fg=TEXT,
      insertbackground=ACCENT, relief="flat",
      bd=0, highlightthickness=2,
      highlightcolor=ACCENT,
      highlightbackground=CARD)


#Start: buttonLog
  def viewlogBTN(self):
    tk.Button(self.btn, text="ViewLog", 
                  bg=CARD, fg=TEXT, relief="flat",
                  activebackground="#1a4a7a", activeforeground=TEXT,
                  cursor="hand2", padx=10, pady=4,
                  command=self.view_log).pack(side="right")
                  #command send to def view_log
#End: buttonLog


  #เรียกหน้า Log
  def view_log(self):
    
    window = tk.Toplevel(self)
    window.title("Log PAGE")
    
    window.geometry("600x700")
    window.configure(bg=BG)
    window.resizable(False, False)

    tk.Label(window, text="FOR SUCCESS", font=FONT_H, bg=BG).pack()
    tk.Label(window, text="mission complete! to-do list", font=FONT_S, bg=BG).pack()
    
    frame = tk.Frame(window, bg=BG, padx=16, pady=0)
    frame.pack(fill="both", expand=True) #fill= "both"ให้ frame ขยายทั้งเเนวตั้งเเนวนอน"
    
    txt = tk.Text(frame, font=FONT_S, bg=PANEL, fg="black",relief="flat", bd=0, wrap="word", state="disabled")
    txt.pack(side="left", fill="both", expand=True)

    #scrollbar 
    sb = ttk.Scrollbar(frame, orient="vertical", command=txt.yview)
    sb.pack(side="right", fill="y") #ยึดไว้ด้านขวา
    txt.configure(yscrollcommand=sb.set) #เชื่อมกันระหว่างการเลื่อน

    #เช็คว่า Logfile มีจริงไหม
    if os.path.exists(LOG_FILE):
      #มีไฟล์ ให้เปิดไฟล์เเบบอ่าน
      with open(LOG_FILE, encoding="utf-8") as f:
        content = f.read()
    else:
      content = "(No log yet. Mark tasks as done to start logging.)"

    txt.configure(state="normal");
    txt.insert("1.0", content)
    txt.configure(state="disabled")
    print("Welcome to log")






if __name__ == "__main__":
  app = main_app()
  app.mainloop()