from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

class NasreddinHocaGenerator:
    def __init__(self, model_path="nasreddin_model", base_tokenizer="ytu-ce-cosmos/turkish-gpt2"):
        # Tokenizer ve model yükleniyor
        self.tokenizer = GPT2Tokenizer.from_pretrained(base_tokenizer)
        self.model = GPT2LMHeadModel.from_pretrained(model_path)
        self.model.eval()

    def generate_joke(self, prompt="Nasreddin Hoca'nın başına komik bir olay geldi."):
        inputs = self.tokenizer(prompt, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=100,
                do_sample=True,
                temperature=0.7,
                top_k=40,
                top_p=0.9,
                repetition_penalty=1.5,
                eos_token_id=self.tokenizer.eos_token_id,
                pad_token_id=self.tokenizer.eos_token_id,
                early_stopping=True
            )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True).replace(prompt, "").strip()
