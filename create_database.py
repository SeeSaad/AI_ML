import requests
import csv

API_KEY = "here goes your api key ;)"
queries = ["Adventure", "Fantasy", "Science Fiction", "Mystery", "Romance", "Thriller", "Horror", "Historical Fiction", "Drama"]

max_results = 40
total_results = 600
books = []

books_map = {}

for query in queries:
    for start_index in range(0, total_results, max_results):
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&startIndex={start_index}&maxResults={max_results}&langRestrict=en&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            
            if (volume_info.get('description') == None) or (volume_info.get('title') in books_map):
                continue
            
            book = {
                'title': volume_info.get('title').replace(',', ''),
                'category': query,
                'description': volume_info.get('description').replace(',', ''),
            }
            books_map[(volume_info.get('title'))] = ""
            books.append(book)

    print(f"Fetched {len(books)} books")

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'category', 'description'])
    writer.writeheader()
    writer.writerows(books)