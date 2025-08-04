import json
from app.trend_parser import generate_outfit
from eval.metrics import compute_bleu, compute_rouge

with open("eval/eval_samples.json", "r") as f:
    samples = json.load(f)

for sample in samples:
    trend = sample["trend"]
    reference = sample["reference"]
    generated = generate_outfit(trend)

    bleu = compute_bleu(reference, generated)
    rouge = compute_rouge(reference, generated)

    print(f"\n🔹 Trend: {trend}")
    print(f"📏 BLEU: {bleu:.2f} | ROUGE-1: {rouge['rouge1'].fmeasure:.2f} | ROUGE-L: {rouge['rougeL'].fmeasure:.2f}")
    print(f"📖 Ref: {reference}")
    print(f"✨ Gen: {generated}")