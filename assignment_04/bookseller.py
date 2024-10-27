# Constants for Sales Manager Position
MIN_YEARS_BOOKSALES = 3 
MIN_YEARS_BOOK_MANAGER = 1

years_booksales = int(input('Enter your years of bookselling experience:'))
years_book_manager = int(input('Enter how many years you have been a bookseller manager:'))

if years_booksales >= MIN_YEARS_BOOKSALES and years_book_manager >=MIN_YEARS_BOOK_MANAGER:
    print('Congratulations! You are eligble and qualified to be the new Bookseller Manager!')
else: 
# Multi-line wtih f-string
    print(f'''
Sorry, you do not meet the requirements for the new Bookseller Manager position. Please apply again later. 

You need at least:
- {MIN_YEARS_BOOKSALES} years of being a bookseller.
- {MIN_YEARS_BOOK_MANAGER} year as a bookseller manager.
Please reach out with any concerns and questions that you may have to the bookstore's email:
readingmore@gmail.com and be on the lookout for other open positions! Have a good day:)
''' )
    
