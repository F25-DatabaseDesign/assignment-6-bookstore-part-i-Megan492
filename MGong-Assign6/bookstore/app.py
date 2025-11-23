from flask import Flask, render_template, request, redirect, url_for, make_response

# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   Example: [1, "China"]

categories = [
    [1, "China"],
    [2, "Japan"],
    [3, "Korea"],
    [4, "India"]
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId
#   categoryId
#   title
#   author
#   isbn
#   price      (float)
#   image      (PNG filename stored in static/images/books)
#   readNow    (1 or 0)

books = [
    # China
    [1, 1, "China: A History", "John Keay",
     "9780465025183", 24.99, "A history of china.png", 1],
    [2, 1, "Imperial China", "DK",
     "9780744020472", 31.77, "Imperial China.png", 0],
    [3, 1, "The Cambridge Illustrated History of China", "Patricia Buckley Ebrey",
     "9781009151443", 39.35, "The Camberidge illustrated history of china.png", 1],
    [4, 1, "Deng Xiaoping and the Transformation of China", "Ezra F. Vogel",
     "9780674725867", 24.00, "Deng Xiaoping.png", 0],

    # Japan
    [5, 2, "A History of Japan: Revised Edition", "R. H. P. Mason",
     "9780804820974", 18.95, "A history of apan.png", 1],
    [6, 2, "A Concise History of Japan", "Brett L. Walker",
     "9780521178723", 29.99, "A concise history of japan.png", 0],
    [7, 2, "Rain of Ruin: Tokyo, Hiroshima and the Surrender of Japan", "Richard Overy",
     "9781324105305", 17.82, "Rain of ruin.png", 1],
    [8, 2, "Downfall: The End of the Imperial Japanese Empire", "Richard B. Frank",
     "9780679414247", 20.00, "Downfall.png", 0],

    # Korea
    [9, 3, "Korea: A New History of South and North", "Victor Cha",
     "9780300259810", 10.65, "A new history of south&north.png", 1],
    [10, 3, "Korean Short History", "James L. Stokesbury",
     "9780688095130", 11.80, "A short history of the korean war.png", 0],
    [11, 3, "The Two Koreas: A Contemporary History", "Don Oberdorfer",
     "9780465031238", 22.13, "The two koreas.png", 1],
    [12, 3, "A History of Korea", "Kyung Moon Hwang",
     "9781352012583", 32.49, "A history of korea.png", 0],

    # India
    [13, 4, "The Golden Road: How Ancient India Transformed the World", "William Dalrymple",
     "9781639734146", 19.60, "The golden road.png", 1],
    [14, 4, "The Raj at War: A People's History of India's Second World War", "Yasmin Khan",
     "9780099542278", 27.09, "The Raj at war.png", 0],
    [15, 4, "A New History of India", "Stanley Wolpert",
     "9780195337563", 57.99, "A new history of India.png", 1],
    [16, 4, "History of India as it Happened", "Francois Gautier",
     "9788124117620", 31.77, "A history of india as it happened.png", 0]
]


# set up routes
@app.route('/')
def home():
    # Link to the index page. Pass the categories as a parameter
    return render_template('index.html', categories=categories)


@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get('categoryId', type=int)

    # If no categoryId given, go back to home
    if category_id is None:
        return redirect(url_for('home'))

    # Create a new list called selected_books containing books in that category
    selected_books = [book for book in books if book[1] == category_id]

    # Link to the category page. Pass the selectedCategory, categories and books as parameters
    return render_template(
        'category.html',
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )


@app.route('/search', methods=['POST'])
def search():
    # Get search term from the form
    term = request.form.get('search', '').strip().lower()

    # Simple search on book title (index 2 in the book list)
    matched_books = [book for book in books if term in book[2].lower()]

    # Re-use the category template to show search results
    return render_template(
        'category.html',
        selectedCategory=None,
        categories=categories,
        books=matched_books
    )


@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html', error=e, categories=categories)

if __name__ == "__main__":
    app.run(debug=True)
