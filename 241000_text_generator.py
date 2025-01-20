
from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "Warren Buffet used to",
    max_length = 100,
    num_return_sequences = 2
)

print(res)

