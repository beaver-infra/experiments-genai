from pymilvus import connections, utility, Collection, FieldSchema, CollectionSchema, DataType
import string
import random

connections.connect(
  alias="default",
  host="localhost",
  port="19530"
)

print(utility.list_collections())

collection = Collection("album1")

num_entities = 3

data = [
  [''.join(random.choices(string.ascii_uppercase, k=7)) for i in range(num_entities)],
  [i for i in range(num_entities)],
  [random.randint(0, 10000) for i in range(num_entities)],
  [[random.random() for _ in range(2)] for _ in range(num_entities)]
]

print(data)

data_insert = collection.insert(data)

print(data_insert)

