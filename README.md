# YouTube RAG Assistant

A lightweight Retrieval-Augmented Generation (RAG) library that allows users to ask questions about YouTube videos using their transcripts.

## Features

- Automatic YouTube transcript extraction.
- Automatic video ID extraction.
- Text chunking with overlap.
- Semantic embeddings using Sentence Transformers.
- Vector similarity search using FAISS.
- Answer generation using Hugging Face FLAN-T5.
- Video processing cache for multiple questions.

## Installation

```bash
pip install git+https://github.com/mahir-iitp/youtube-rag-assistant.git
```

## Usage

```python
from youtube_rag import answer_question

youtube_url = "https://www.youtube.com/watch?v=VIDEO_ID"

question = "What is the main topic of this video?"

answer = answer_question(youtube_url, question)

print(answer)
```

## Models Used

- Embedding: all-MiniLM-L6-v2
- LLM: google/flan-t5-base
- Vector Database: FAISS

## Requirements

- Python 3.9+
- Internet connection for initial model and transcript downloads.
- Sufficient RAM for model inference.

## Limitations

- Videos must have accessible transcripts.
- First execution requires downloading the Hugging Face models.
- CPU inference may take some time.

## License

MIT License.
