import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Hello, Tkinter!")

root.minsize(300, 200)
root.resizable(True, True)

root.iconbitmap("img/icon.ico")
root.config(bg="#f0f0f0")

root.attributes("-topmost", True)

main_frame = tk.Frame(root, bg="#f0f0f0", highlightbackground="black", highlightthickness=1)
main_frame.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()