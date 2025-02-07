from pymongo import MongoClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import requests
import json

url="mongodb://localhost:27017/medforecast"
cli = MongoClient(url)
db=cli.get_database("Srk_learning")
coll=db.get_collection("books")

# End point creation
@csrf_exempt
def requested_Data(request):
    try:
        # query = {"title":"Srk the great"}
        query = {"pages":300}
        # query={"title":"Rich Dad Poor Dad"}
        books_cusror=coll.find(query,{"_id":0})
        book = []
        for books in books_cusror:
            # books["_id"] = str(books["_id"])
            author = books.get('author', 'Unknown')
            if author == "NaN" or (isinstance(author, float) and np.isnan(author)):
                author = "Unknown"
            
            # Ensure genres are always lists
            genres = books.get('geners', [])
            if isinstance(genres, str):  # Convert string to list if necessary
                genres = [genres]
            rating = books.get('rating',[])
            
            formatted_book = {
                "title": books.get('title', 'Untitled'),
                "author": author,
                "pages": books.get('pages', 0),
                "rating": rating,
                "genres": genres
            }
            book.append(formatted_book)
        if book:
            return JsonResponse(book,safe=False)
        else:
            return JsonResponse(f"No book with {query}",safe=False)

    except Exception as e:
        return JsonResponse(f"Error occured due to {e}",safe=False)

@csrf_exempt
def insertion(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)

            title = data.get('title')
            author = data.get('author')
            pages = data.get('pages')
            rating = data.get('rating')
            geners = list(data.get('geners')) 

            query = {
                'title':title,
                'author':author,
                'pages':pages,
                'rating':rating,
                'geners':geners
                }
            
            books_cusror=coll.insert_one(query)
            print(books_cusror)
            return JsonResponse("The data inserted successfully",safe=False)
        
        except Exception as e:
            return JsonResponse(f"Error occured due to {e}",safe=False)
        
    return JsonResponse({'error': 'Only POST requests are allowed'},status=405)

@csrf_exempt
def deletion(request):
    if(request.method == 'POST'):
        try:

            data = json.loads(request.body)

            title = data.get('title')
            query={'title':title}
            find = coll.find_one(query,{'_id':0})
            print(find)

            if find:
                delete = coll.delete_one(query)
                return JsonResponse("The Data is Deleted Successfully",safe=False)
            else:
                return JsonResponse("Data is Not Found",safe=False)
        except Exception as e:
            return JsonResponse(f"An error occured {e}",safe=False,status=405)
    
    else:
        return JsonResponse("Invalid Request Format",safe=False)

@csrf_exempt
def updation(request):

    if(request.method == 'POST'):

        try:
            data = json.loads(request.body)

            title = data.get('title')
            author = data.get('author')
            geners = list(data.get('geners'))

            query = {'title':title}

            find = coll.find_one(query,{'_id':0})
            print(find)

            if find:
                update = coll.update_one(
                    query,
                    {
                        '$set':{'author':author},
                        '$push':{'geners':{'$each':geners}}
                    }
                )
                return JsonResponse("The data is updated successfully",safe=False)
            else:
                return JsonResponse("The data not found",safe=False)
        except Exception as e:
            return JsonResponse(f"an un expected error occured {e}",safe=False)
    else:
        return JsonResponse("Invalid method request",safe=False)