## What is an HTTP Request?

HTTP (Hypertext Transfer Protocol) is a way for computers to talk to each other over the internet. When you visit a website, your computer sends an HTTP request to the website's server asking for the web page. The server then sends back an HTTP response with the web page data.

Imagine you want to borrow a book from the library. You write a request on a piece of paper and give it to the librarian. The librarian reads your request and brings you the book you asked for. In this case, you are like your computer, the librarian is like the website's server, and the book is like the web page data.

- Types of HTTP Requests: GET, POST, PUT, PATCH, DELETE


# GET Request

GET: Imagine you want to get a book from the library. You ask the librarian, and they give you the book. This is like a GET request.

* Purpose: To retrieve data from a server.

* Uniqueness: It is used to ask for a specific resource, like a web page or an image. When you type a URL in your browser and hit enter, your browser sends a GET request.

* Example: Visiting a webpage, downloading a file.


# POST Request

POST: Now, imagine you want to donate a new book to the library. You give the book to the librarian, and they add it to the collection. This is like a POST request.

* Purpose: To send data to a server to create or update a resource.

* Uniqueness: It is often used when submitting form data, like when you fill out a registration form on a website and click submit.

* Example: Logging into a website, submitting a contact form.


# PUT Request:

PUT: Suppose you found a book in the library with some missing pages, and you have the complete book at home. You bring the complete book to the librarian, and they replace the old book with the new one. This is like a PUT request.

* Purpose: To update a resource on a server.

* Uniqueness: It replaces the current resource with the new data you send. It is usually used for updating information.

* Example: Updating user information.


# DELETE Request:

DELETE: If you tell the librarian to remove a book from the library collection because it is outdated or damaged, this is like a DELETE request.

* Purpose: To delete a resource from a server.

* Uniqueness: It removes a specified resource from the server.

* Example: Deleting a post on a blog.


# PATCH Request:

PATCH: If you notice that only the title of a book is wrong, you tell the librarian to change just the title without touching the rest of the book. This is like a PATCH request.

* Purpose: To partially update a resource on a server.

* Uniqueness: It applies partial modifications to a resource. Unlike PUT, it only changes parts of the resource.

* Example: Changing only the email address in user information.


SUMMARY

HTTP requests are used to interact with web servers and perform different actions, like retrieving data (GET), sending data (POST), updating data (PUT), deleting data (DELETE), and partially updating data (PATCH). Understanding these requests is essential for web scraping and working with web APIs. This basic project demonstrates how to use GET, POST, and DELETE requests in Python, providing a practical example of how to interact with web servers.