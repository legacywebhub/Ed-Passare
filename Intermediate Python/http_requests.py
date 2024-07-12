import requests

# Define a simple API endpoint for demonstration
api_url = "https://jsonplaceholder.typicode.com/posts"

# GET Request: Retrieve data from the server
response_get = requests.get(api_url)
print("GET Request - Status Code:", response_get.status_code)
print("GET Request - Response Data:", response_get.json()[:2])  # Display the first 2 items for brevity

# POST Request: Send data to the server to create a new resource
new_post = {
    "title": "New Post",
    "body": "This is the body of the new post.",
    "userId": 1
}
response_post = requests.post(api_url, json=new_post)
print("POST Request - Status Code:", response_post.status_code)
print("POST Request - Response Data:", response_post.json())

# DELETE Request: Delete a resource from the server
delete_url = f"{api_url}/1"  # Assuming we want to delete the post with ID 1
response_delete = requests.delete(delete_url)
print("DELETE Request - Status Code:", response_delete.status_code)

# Note: The above API is for demonstration purposes and does not actually create or delete data on the server.
