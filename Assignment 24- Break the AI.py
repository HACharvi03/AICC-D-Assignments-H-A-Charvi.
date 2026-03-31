from transformers import pipeline

# Load simple text generation model
generator = pipeline("text-generation", model="gpt2")

prompts = [
    "Explain in one word why the sky is blue but also explain in 100 words",
    "Write a sentence that contradicts itself",
    "Give a yes or no answer and explain why in detail",
    "Say nothing but explain everything",
    "Describe a square circle"
]

for prompt in prompts:
    print("\nPrompt:", prompt)
    output = generator(prompt, max_length=50, num_return_sequences=1)
    print("Response:", output[0]['generated_text'])