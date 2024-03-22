# Experiments Gen AI

List of experiments on Gen AI ecosystem

## Setup

### Milvus

1. Use Docker Compose for `Milvus` Vector store setup. Execute `sudo docker compose -f docker-compose-milvus.yml up -d` from project root.

## Table of Content

| File / Folder name | Comments |
|:---|:---|
| rag_pdf_1.py | RAG pipeline (Load PDF Dir, Extract data and index in naive way, Embed the index into Milvus, User queries ) |
| rag_pdf_2.py | RAG pipeline (Load PDF Dir, Extract data with Sentence window, Embed the index into local storage, User queries |
| rag_pdf_3.py | RAG pipeline (Load PDF Dir, Extract data with Sentence window, Embed the index into Milvus, User queries |
