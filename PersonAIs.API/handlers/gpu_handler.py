from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer, pipeline
import torch

model_name = "microsoft/Phi-3-mini-4k-instruct"
cache_dir = "./llm"

tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)

# Move model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Notify the user which platform it will use
platform = "GPU" if torch.cuda.is_available() else "CPU"
print(f"Using {platform} for inference")
print(torch.cuda.is_available())

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
}

streamer = TextStreamer(tokenizer)

while True:
    query = input("Enter your question (or 'exit' to quit): ")
    
    if query.lower() == 'exit':
        break

    full_query = f"<|system|>You are a helpful AI assistant.<|end|><|user|>{query}<|end|><|assistant|>"

    pipe(full_query, **generation_args, streamer=streamer)