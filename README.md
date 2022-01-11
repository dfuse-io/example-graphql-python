## dfuse GraphQL Python Example

This simple program demonstrates how easy it is to query our GraphQL API over gRPC in Python. It:

* Request a token from our authentication API
* Creates a gRPC connection with credentials
* Instantiates a GraphQL client
* Executes a simple GraphQL query
* Prints the response

### Requirements

You will need to have Python3 (>= 3.4+) as well as `virtualenv` and `pip`
`>= 15.0+`.

We use a virtual environment for this example, all dependencies are listed
in the `requirements.txt` at the root of this project.

#### Quickstart

First of all, visit [https://dfuse.eosnation.io/](https://dfuse.eosnation.io/) to get
a free dfuse Community Edition API key for your project.

First, clone this repository to your work folder:

```bash
git clone https://github.com/dfuse-io/example-graphql-python.git
cd example-graphql-python
```

Setup the virtual environment and pull all dependencies:

```bash
./install_deps.sh
```

Once your environment is setup properly, simply run the `main.py` script:

```bash
python3 main.py YOUR_API_KEY_HERE
```

##### Protobuf

The protocol buffers are already generated, the `generate_proto.sh` is able to regenerate them if needed, it showcases also the command the can be used to generate them back.

The required Protobuf definitions are found at the root projet under `pb`.

To re-generate, simply do:

```bash
./generate_proto.sh
```
