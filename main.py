class BookLibrary:
	books = ['Introduction to Algorithms','Rich Dad Poor Dad','Theory of Everything','Deep Work']
	number_of_books = 5
	def display_books(self):
		for i in range(len(self.books)):
			print(self.books[i])
	def borrow_book(self,book):
		self.books.remove(book)
		print(f"You can have given {book}. Take good care of the book.")
	def add_book(self,book_name):
		self.books.append(book_name)
		print(f"We have added {book_name} to our library")
	def return_book(self,book_to_be_returned):
		self.books.append(book_to_be_returned)
		print(f"Thank You for returning {book_to_be_returned}")
book = BookLibrary()
print("Hello Guys! Welcome to Jamshedpur Town Library\n")
while True:
	user_input = int(input("\nEnter 1 for displaying the book\n2 to borrow book\n3 for adding book to the library\n4 for returning book to the library\n0 for exiting the library\n: "))
	if user_input==1:
		print("These are the books :")
		book.display_books()
	elif user_input==2:
		book_to_be_borrowed = input("Enter the name of the book you want to borrow : ")
		try:
			book.borrow_book(book_to_be_borrowed)
		except:
			print(f"{book_to_be_borrowed} is not present in the library")
	elif user_input==3:
		book_to_be_added = input("Enter the name of the book you want to add to the library : ")
		book.add_book(book_to_be_added)
	elif user_input==4:
		book_return = input("Enter the name of the book you want to return to the library : ")
		book.return_book(book_return)
	elif user_input==0:
		break
	else:
		print("\nInvalid Input")