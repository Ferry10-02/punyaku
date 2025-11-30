import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

BG = "#ffd9ea"
CARD = "#ffb6d2"
STRONG = "#ff6b98"
WHITE = "#ffffff"
FONT = ("Helvetica", 12, "bold")


# ---- LOAD IMAGE ----
def load_img(path, size=(170, 170)):
    img = Image.open(path).convert("RGBA")
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)


# =====================================================
#                MINI GAME – MAKEUP THEME
# =====================================================

# 1. Makeup Show (blush, eyeshadow, lipstick)
def game_makeup_show():
    g = tk.Toplevel()
    g.title("Makeup Show")
    g.geometry("400x520")
    g.configure(bg=BG)

    tk.Label(g, text="Makeup Show", font=("Arial", 20, "bold"),
             bg=BG, fg=STRONG).pack(pady=10)

    canvas = tk.Canvas(g, width=260, height=330, bg="white")
    canvas.pack()

    # wajah
    face = canvas.create_oval(60, 40, 200, 220, fill="#ffe0bd")

    # tombol makeup
    def add_blush():
        canvas.create_oval(90, 140, 120, 170, fill="#ff88b0")
        canvas.create_oval(140, 140, 170, 170, fill="#ff88b0")

    def add_lipstick():
        canvas.create_rectangle(115, 185, 145, 195, fill="#ff3c66")

    def add_eyeshadow():
        canvas.create_rectangle(90, 90, 120, 110, fill="#b57cff")
        canvas.create_rectangle(140, 90, 170, 110, fill="#b57cff")

    tk.Button(g, text="Blush On", bg=STRONG, fg="white",
              font=FONT, command=add_blush).pack(pady=5)

    tk.Button(g, text="Lipstick", bg="#ff6fa2", fg="white",
              font=FONT, command=add_lipstick).pack(pady=5)

    tk.Button(g, text="Eyeshadow", bg="#b57cff", fg="white",
              font=FONT, command=add_eyeshadow).pack(pady=5)


# 2. Tidy Up Makeup – drag makeup item ke pouch
def game_tidy_up():
    g = tk.Toplevel()
    g.title("Tidy Up Makeup")
    g.geometry("400x450")
    g.configure(bg=BG)

    tk.Label(g, text="Rapikan makeup ke pouch!",
             bg=BG, fg=STRONG, font=("Arial", 16, "bold")).pack(pady=10)

    canvas = tk.Canvas(g, width=350, height=330, bg="white")
    canvas.pack()

    # pouch (tujuan)
    pouch = canvas.create_rectangle(230, 240, 330, 315, fill="#ffd1e6", outline="purple", width=3)

    # items makeup
    lipstick = canvas.create_rectangle(50, 50, 100, 110, fill="#ff4d7a")
    brush = canvas.create_rectangle(120, 70, 170, 130, fill="#c38aff")

    selected = None

    def start_drag(event):
        nonlocal selected
        selected = canvas.find_closest(event.x, event.y)[0]

    def drag(event):
        if selected:
            canvas.coords(selected, event.x-30, event.y-30, event.x+30, event.y+30)

    def release(event):
        x, y, _, _ = canvas.coords(selected)
        if 230 < x < 330 and 240 < y < 315:
            messagebox.showinfo("Good!", "Makeup sudah dirapikan!")

    canvas.bind("<Button-1>", start_drag)
    canvas.bind("<B1-Motion>", drag)
    canvas.bind("<ButtonRelease-1>", release)


# 3. Relax Collection – skincare relax
def game_relax():
    g = tk.Toplevel()
    g.title("Relax Collection")
    g.geometry("400x480")
    g.configure(bg=BG)

    tk.Label(g, text="Skincare Relax", bg=BG, fg=STRONG,
             font=("Arial", 20, "bold")).pack(pady=10)

    tk.Label(g, text="Pilih skincare untuk relaks ✨",
             bg=BG, font=("Arial", 12)).pack()

    frame = tk.Frame(g, bg=BG)
    frame.pack(pady=20)

    def apply(name):
        messagebox.showinfo("Relax", f"{name} applied! Kulit terasa segar ✨")

    skincare = [
        ("Masker", "#ff9bbd"),
        ("Toner", "#ffd07f"),
        ("Serum", "#a1e3ff"),
        ("Cream", "#baffc9")
    ]

    for name, color in skincare:
        tk.Button(frame, text=name, bg=color, width=12, height=2,
                  font=FONT, command=lambda n=name: apply(n)).pack(pady=6)


# 4. Pop It (makeup sponge)
def game_pop_it():
    g = tk.Toplevel()
    g.title("Pop It Sponge")
    g.geometry("360x420")
    g.configure(bg=BG)

    tk.Label(g, text="Pop The Makeup Sponge!",
             bg=BG, fg=STRONG, font=("Arial", 18, "bold")).pack(pady=10)

    frame = tk.Frame(g, bg=BG)
    frame.pack(pady=10)

    def pop(btn):
        btn.config(text="POP!", bg="white", fg="gray")
        btn.config(state="disabled")

    for i in range(4):
        row = tk.Frame(frame, bg=BG)
        row.pack()
        for j in range(4):
            b = tk.Button(
                row,
                text="●",
                font=("Arial", 20),
                width=3,
                bg="#ff89b3",
                fg="white"
            )
            b.config(command=lambda bt=b: pop(bt))
            b.pack(side="left", padx=5, pady=5)


# 5. Wedding Dress – makeup pengantin
def game_wedding():
    g = tk.Toplevel()
    g.title("Wedding Makeup")
    g.geometry("400x470")
    g.configure(bg=BG)

    tk.Label(g, text="Wedding Makeup Artist",
             bg=BG, fg=STRONG, font=("Arial", 18, "bold")).pack(pady=10)

    canvas = tk.Canvas(g, width=280, height=330, bg="white")
    canvas.pack()

    face = canvas.create_oval(80, 50, 200, 200, fill="#ffe0bd")

    def apply(color, y1, y2):
        canvas.create_oval(110, y1, 165, y2, fill=color)

    tk.Button(g, text="Blush Pink", bg="#ff9cc2", fg="white",
              command=lambda: apply("#ffc0d9", 140, 170)).pack(pady=5)

    tk.Button(g, text="Highlighter", bg="#fff5aa", fg="black",
              command=lambda: apply("#fff5aa", 120, 135)).pack(pady=5)

    tk.Button(g, text="Lipstick", bg="#ff4d7a", fg="white",
              command=lambda: apply("#ff4d7a", 175, 185)).pack(pady=5)


# 6. Dress Up – pakaian MUA
def game_dress_up():
    g = tk.Toplevel()
    g.title("Dress Up MUA")
    g.geometry("400x450")
    g.configure(bg=BG)

    tk.Label(g, text="Dress Up Makeup Artist",
             bg=BG, fg=STRONG, font=("Arial", 18)).pack(pady=10)

    canvas = tk.Canvas(g, width=260, height=330, bg="white")
    canvas.pack()

    shirt = canvas.create_rectangle(90, 130, 170, 200, fill="#ffccdd")

    def change(color):
        canvas.itemconfig(shirt, fill=color)

    tk.Button(g, text="Pink", bg="#ff9cae", fg="white",
              command=lambda: change("#ff9cae")).pack(pady=5)
    tk.Button(g, text="Purple", bg="#c39aff", fg="white",
              command=lambda: change("#c39aff")).pack(pady=5)
    tk.Button(g, text="Mint", bg="#9affd4", fg="white",
              command=lambda: change("#9affd4")).pack(pady=5)


# =====================================================
#                        DASHBOARD
# =====================================================
class GameCard(tk.Frame):
    def __init__(self, master, image, title, command=None):
        super().__init__(master, bg=BG)

        self.card = tk.Frame(self, bg=CARD, bd=0)
        self.card.pack(padx=10, pady=(0, 5))

        img_label = tk.Label(self.card, image=image, bd=0)
        img_label.image = image
        img_label.pack(padx=12, pady=12)

        title_box = tk.Frame(self, bg=STRONG, height=36)
        title_box.pack(fill="x", padx=10)
        title_box.pack_propagate(False)

        lbl = tk.Label(title_box, text=title.upper(),
                       bg=STRONG, fg=WHITE, font=FONT)
        lbl.pack(expand=True)

        if command:
            self.card.bind("<Button-1>", lambda e: command())
            img_label.bind("<Button-1>", lambda e: command())
            lbl.bind("<Button-1>", lambda e: command())


class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Makeup Games Dashboard")
        self.configure(bg=BG)
        self.geometry("430x770")
        self.resizable(False, False)

        self.games = {
            "Makeup Show": game_makeup_show,
            "Tidy Up": game_tidy_up,
            "Relax Collection": game_relax,
            "Pop It": game_pop_it,
            "Wedding Dress": game_wedding,
            "Dress Up": game_dress_up
        }

        self.make_grid()

    def make_grid(self):
        grid = tk.Frame(self, bg=BG)
        grid.pack()

        titles = list(self.games.keys())
        paths = [
            "D:/Febry/assets/1.jpg",
            "D:/Febry/assets/2.jpg",
            "D:/Febry/assets/3.jpg",
            "D:/Febry/assets/4.jpg",
            "D:/Febry/assets/5.jpg",
            "D:/Febry/assets/6.jpg"
        ]

        idx = 0
        for r in range(3):
            row = tk.Frame(grid, bg=BG)
            row.pack(pady=5)
            for c in range(2):
                img = load_img(paths[idx])
                card = GameCard(row, img, titles[idx],
                                command=self.games[titles[idx]])
                card.pack(side="left", padx=6)
                idx += 1


# ---- RUN ----
Dashboard().mainloop()
