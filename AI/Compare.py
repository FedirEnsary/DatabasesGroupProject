from llama_cpp import Llama

llm = Llama(
    model_path="AI\synthia-7b-v2.0-16k.Q2_K.gguf",
    n_ctx=32768,
    n_gpu_layers=32,
    n_batch=1024,
    f16_kv=False,
    verbose=False,
    
)

def compare(user, top):
    messages = [
    {"role": "system", "content": "You must compare the next two reviews and say how they are alike and different"},
    {"role": "user", "content": user},
    {"role": "user", "content": top}
    ]

    output = llm.create_chat_completion(messages=messages, max_tokens=100, stream=False)
    return output["choices"][0]["message"]["content"].strip()