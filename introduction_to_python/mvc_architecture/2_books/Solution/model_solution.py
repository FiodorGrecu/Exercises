import json 
book_author_list={"books":{"A Tale of Two Cities":'Charles Dickens',"Lord Of The Rings":'J.R.R. Tolkien',"Dark Psychology":'Steven Turner',"Rich Dad Poor Dad":'Robert T Kiyosaki'}}
book_list = json.dumps(book_author_list)
def get_list():
    return book_list
# print(book_list)

def retrive_book(book):
    data = json.loads(book_list)
    books = data["books"]
    result = books.get(book)
    
    return result




    
    

