"""
Ejercicio 4: Recomendador de libros
Fuente: https://developer.nytimes.com/docs/books-product/1/overview
Elementos a utilizar: 
¿Qué debe poder hacer tu código?
1.	Pedirle al usuario decidir qué lista de “Best Sellers” quiere consultar. 
2.	Poder escoger si quiere ver los “Best Sellers” actuales o de alguna fecha en específica. 
3.	Poder escoger un precio específico del libro que quiere adquirir. 
4.	Poder escoger un rango de edades dirigido para el libro. 
Resultado: 
1.	Poder verlo de manera estructurada, poniendo la información clave del libro que estás recomendado para la información que te dio el usuario. 
2.	Poder acceder rápidamente a la reseña generada por el NYT acerca del libro recomendado.
3.	Para los Best Sellers actuales, decirle al usuario dónde lo puede comprar. 
4.	Poder mostrar toda esta información en una aplicación / pantalla / interfaz gráfica amigable para que el usuario pueda interactuar con los resultados.


"""

import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Label, Button
import requests
import webbrowser

#  API key del New York Times generada al crear la cuenta de developer
API_KEY = 'RPRfDTskAG8w30ij7c0gQGKj9UcVF1Ut'

def fetch_books(list_name, date=None):
    """
    Solicita al API de NYT los libros de una lista de best sellers específica.
    Puede buscar en la lista actual o en una fecha específica.
    """
    base_url = "https://api.nytimes.com/svc/books/v3/lists"
    if date:
        url = f"{base_url}/{date}/{list_name}.json"
    else:
        url = f"{base_url}/current/{list_name}.json"
    params = {'api-key': API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", "Failed to fetch data from NYT API")
        return None

def open_review(url):
    """
    Abre un URL en el navegador predeterminado del usuario.
    """
    webbrowser.open(url)

def main_window():
    """
    Crea la ventana principal de la aplicación y maneja las interacciones del usuario.
    """
    window = tk.Tk()
    window.title("NYT Best Sellers Recommender")

    def get_user_choices():
        """
        Permite al usuario seleccionar los criterios para la búsqueda de libros.
        """
        list_name = simpledialog.askstring("Input", "Which Best Sellers list do you want to check? (e.g., hardcover-fiction)")
        date = simpledialog.askstring("Input", "Enter date in YYYY-MM-DD format or leave blank for current:")
        max_price = simpledialog.askstring("Input", "Maximum price you would pay for a book (leave blank for no limit):")
        age_group = simpledialog.askstring("Input", "Target age group (leave blank for no preference):")

        if list_name:
            books_data = fetch_books(list_name, date)
            if books_data:
                display_books(books_data, max_price, age_group)

    def display_books(books_data, max_price, age_group):
        """
        Muestra los libros que coinciden con los criterios seleccionados en una nueva ventana.
        """
        new_window = Toplevel(window)
        new_window.title("Filtered Best Sellers")
        books = books_data.get('results', {}).get('books', [])
        filtered_books = [book for book in books if (not max_price or float(book.get('price', float('inf'))) <= float(max_price)) and (not age_group or book.get('age_group', 'All Ages') == age_group)]

        if not filtered_books:
            Label(new_window, text="No books match your criteria.").pack()
        else:
            for book in filtered_books:
                info = f"{book['title']} by {book['author']} - Price: ${book.get('price', 'N/A')}\nAge Group: {book.get('age_group', 'All Ages')}\n"
                Label(new_window, text=info).pack()
                Button(new_window, text="Read Review or Buy", command=lambda b=book: open_review(b['amazon_product_url'])).pack()

    Button(window, text="Choose List and Date", command=get_user_choices).pack()

    window.mainloop()

if __name__ == "__main__":
    main_window()
