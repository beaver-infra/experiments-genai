from pymilvus import connections, utility, Collection, FieldSchema, CollectionSchema, DataType

connections.connect(
  alias="default",
  host="localhost",
  port="19530"
)

utility.list_collections()

song_name = FieldSchema(
  name="song_name",
  dtype=DataType.VARCHAR,
  max_length=200
)

song_id = FieldSchema(
  name="song_id",
  dtype=DataType.INT64,
  is_primary=True
)

listen_count = FieldSchema(
  name="listen_count",
  dtype=DataType.INT64
)

song_vec = FieldSchema(
  name="song_vec",
  dtype=DataType.FLOAT_VECTOR,
  dim=2
)

collection_schema = CollectionSchema(
  fields=[song_name, song_id, listen_count, song_vec],
  description="Album songs"
)

collection = Collection(
  name="album1",
  schema=collection_schema,
  using="default"
)

print(utility.list_collections())

collection.create_partition('disc1')
print(collection.has_partition('disc1'))

 