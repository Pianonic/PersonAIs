from transformers import AutoTokenizer, TextStreamer, AutoModelForCausalLM, pipeline
import intel_npu_acceleration_library
import torch

# Load the model
model_id = "microsoft/Phi-3-mini-4k-instruct"
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", use_cache=True, trust_remote_code=True).eval()
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Compile the model for NPU acceleration
print("Compiling model for the NPU")
model = intel_npu_acceleration_library.compile(model, dtype=torch.float16)

# Setup the pipeline for text generation
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

# Define generation arguments
generation_args = {
    "max_new_tokens": 500,
    "return_full_text": False,
    "temperature": 0.0,
    "do_sample": False,
}

# Create a TextStreamer to print the generated text in real-time
streamer = TextStreamer(tokenizer)

while True:
    # Get user input
    query = input("Enter your question (or 'exit' to quit): ")
    
    if query.lower() == 'exit':
        break

    # Add system and user tags if needed
    full_query = f"<|system|>You are a helpful AI assistant.<|end|><|user|>{query}<|end|><|assistant|>"

    # Run the model and generate output with streaming
    pipe(full_query, **generation_args, streamer=streamer)
