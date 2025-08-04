
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from app.rag_module import retrieve_context

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    quantization_config=bnb_config,
    trust_remote_code=True
)

llama_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=250,
    temperature=0.8,
    do_sample=True
)

def format_prompt(trend: str, context: list) -> str:
    context_text = "\n".join(f"- {item['trend_name']}: {item['description']}" for item in context)
    return f"""### Instruction:
You are a creative fashion stylist. Translate the following high-fashion trend into a wearable, affordable outfit idea for an everyday setting.

### Trend:
{trend}

### Related Microtrends:
{context_text}

### Response:"""

def generate_outfit(trend: str) -> str:
    context = retrieve_context(trend, top_k=3)
    prompt = format_prompt(trend, context)
    result = llama_pipe(prompt)[0]["generated_text"]
    if "### Response:" in result:
        result = result.split("### Response:")[-1].strip()
    return result
