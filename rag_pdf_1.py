from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.vector_stores.milvus import MilvusVectorStore
from llama_index.llms.ollama import Ollama

Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5") # Embedded Model
Settings.llm = Ollama(model="llama2", request_timeout=30.0) # LLM Model
Settings.chuck_size = 512

documents = SimpleDirectoryReader("./data/pdf/").load_data()

print("Single document: ", documents[0])

vector_store = MilvusVectorStore(
  dim=384,
  overwrite=True
)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
  documents, storage_context=storage_context
)

query_engine = index.as_query_engine()

response = query_engine.query("Who is father of Quantum mechanics?")
print("Response: ", response)
for node in response.source_nodes:
  print(f"Metadata {node.node.extra_info}")
  print(f"Score {node.score:.3f}")
print("\n\n")

response = query_engine.query("How is Quantum Physics is different from Classical Physics?")
print("Response: ", response)
for node in response.source_nodes:
  print(f"Metadata {node.node.extra_info}")
  print(f"Score {node.score:.3f}")
print("\n\n")

