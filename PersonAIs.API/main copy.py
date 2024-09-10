from llama_cpp import Llama

llm = Llama(
    model_path="./llm/Phi-3-mini-4k-instruct-q4.gguf",
    n_gpu_layers=-1
)

response = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful Assistant."},
        {"role": "user", "content": "How are you?"}
    ]
)

print(response)