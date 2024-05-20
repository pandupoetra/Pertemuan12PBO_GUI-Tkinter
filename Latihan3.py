import tkinter as tk
from tkinter import messagebox

class MiniLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perpustakaanku")

        self.books = []

        # Frame untuk input data buku
        self.input_frame = tk.Frame(root, bg='lightblue')
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Judul:", bg='lightblue').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.title_entry = tk.Entry(self.input_frame, width=40)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Penulis:", bg='lightblue').grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.author_entry = tk.Entry(self.input_frame, width=40)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        # Frame for buttons
        self.button_frame = tk.Frame(self.input_frame, bg='lightblue')
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(self.button_frame, text="Tambah", command=self.add_book, bg='lightgreen')
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(self.button_frame, text="Edit", command=self.update_book, bg='yellow')
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Hapus", command=self.delete_book, bg='pink')
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Canvas dan Text widget untuk menampilkan daftar buku
        self.display_frame = tk.Frame(root, bg='lightgrey', bd=2, relief=tk.SUNKEN)
        self.display_frame.pack(pady=10)

        self.display_canvas = tk.Canvas(self.display_frame, bg='white')
        self.display_canvas.pack()

        self.books_text = tk.Text(self.display_canvas, width=50, height=15, state=tk.DISABLED, bg='white', fg='black', bd=0, padx=10, pady=10)
        self.books_text.pack()

        # Selected book index
        self.selected_book_index = None

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()

        if title and author:
            self.books.append({"title": title, "author": author})
            self.refresh_books_display()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Tolong Masukan Judul Buku dan Penulis Buku")

    def update_book(self):
        if self.selected_book_index is None:
            messagebox.showwarning("Selection Error", "Tolong pilih nama buku terlebih dahulu")
            return

        title = self.title_entry.get()
        author = self.author_entry.get()

        if title and author:
            self.books[self.selected_book_index] = {"title": title, "author": author}
            self.refresh_books_display()
            self.clear_entries()
            self.selected_book_index = None
        else:
            messagebox.showwarning("Input Error", "Tolong Masukan Judul Buku dan Penulis Buku")

    def delete_book(self):
        if self.selected_book_index is None:
            messagebox.showwarning("Selection Error", "Tolong pilih nama buku terlebih dahulu")
            return

        del self.books[self.selected_book_index]
        self.refresh_books_display()
        self.clear_entries()
        self.selected_book_index = None

    def refresh_books_display(self):
        self.books_text.config(state=tk.NORMAL)
        self.books_text.delete(1.0, tk.END)
        for index, book in enumerate(self.books):
            self.books_text.insert(tk.END, f"{index + 1}. Title: {book['title']}, Author: {book['author']}\n")
        self.books_text.config(state=tk.DISABLED)

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)

    def select_book(self, event):
        try:
            index = int(self.books_text.index(tk.INSERT).split('.')[0]) - 1
            if 0 <= index < len(self.books):
                self.selected_book_index = index
                book = self.books[index]
                self.title_entry.delete(0, tk.END)
                self.title_entry.insert(tk.END, book['title'])
                self.author_entry.delete(0, tk.END)
                self.author_entry.insert(tk.END, book['author'])
        except:
            self.selected_book_index = None

if __name__ == "__main__":
    root = tk.Tk()
    app = MiniLibraryApp(root)
    app.books_text.bind("<Button-1>", app.select_book)
    root.mainloop()
