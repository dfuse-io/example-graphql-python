import http.client
import json
import ssl
import sys
from google.protobuf.struct_pb2 import Struct

import grpc

from dfuse.graphql.v1 import graphql_pb2_grpc
from dfuse.graphql.v1.graphql_pb2 import Request

ssl._create_default_https_context = ssl._create_unverified_context


def token_for_api_key(apiKey):
    connection = http.client.HTTPSConnection("auth.eosnation.io")
    connection.request('POST', '/v1/auth/issue',
                       json.dumps({"api_key": apiKey}), {'Content-type': 'application/json'})
    response = connection.getresponse()

    if response.status != 200:
        raise Exception(
            f" Status: {response.status} reason: {response.reason}")

    token = json.loads(response.read().decode())['token']
    connection.close()

    return token


def graphql_stream():
    credentials = grpc.access_token_call_credentials(
        token_for_api_key(sys.argv[1]))
    channel = grpc.secure_channel('eos.dfuse.eosnation.io:9000',
                                  credentials=grpc.composite_channel_credentials(grpc.ssl_channel_credentials(),
                                                                                 credentials))
    return graphql_pb2_grpc.GraphQLStub(channel)


document = '''
subscription($query: String!, $cursor: String) {
  searchTransactionsForward(query: $query, liveMarkerInterval: 12, limit: 10, cursor: $cursor) {
    block {
      num
    }
    trace {
      id
      matchingActions{
        account
        receiver
        name
        json
      }
    }
  }
}
'''

variables = Struct()
variables["query"] = "account:eosio.token receiver:eosio.token action:transfer"

stream = graphql_stream()
stream = stream.Execute(Request(query=document, variables=variables))

for rawResult in stream:
    if rawResult.errors:
        print(rawResult.errors)
    else:
        result = json.loads(rawResult.data)
        if result['searchTransactionsForward']['trace'] == None:
            print("Live progress at block {}".format(
                result['searchTransactionsForward']['block']['num']))
        else:
            print(result['searchTransactionsForward']
                  ['trace']['matchingActions'])
