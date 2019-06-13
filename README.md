# example-graphql-python
This simple program demonstrates how easy it is to query our GraphQL API over gRPC in Python. It:

* Request a token from our authentication API
* Creates a gRPC connection with credentials
* Instantiates a GraphQL client
* Executes a simple GraphQL query
* Prints the response

#### Running the example

First of all, visit [https://app.dfuse.io](https://app.dfuse.io) to get `YOUR_API_KEY`.

~~~bash
git clone https://github.com/dfuse-io/example-graphql-python.git
cd example-graphql-python
python3 example.py YOUR_API_KEY_HERE
~~~
