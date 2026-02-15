import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "facebook/nllb-200-distilled-600M"

SOURCE_LANG = "eng_Latn"
TARGET_LANG = "por_Latn"


class Translator:

    def __init__(self):

        print("Loading model...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        print(f"Using device: {self.device}")

        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        self.model.to(self.device)

        print("Model loaded.")


    def translate_batch(self, texts, batch_size=16):

        results = []

        for i in range(0, len(texts), batch_size):

            batch = texts[i:i+batch_size]

            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512
            ).to(self.device)

            translated_tokens = self.model.generate(
                **inputs,
                forced_bos_token_id=self.tokenizer.convert_tokens_to_ids(TARGET_LANG),
                max_length=512
            )

            decoded = self.tokenizer.batch_decode(
                translated_tokens,
                skip_special_tokens=True
            )

            results.extend(decoded)

        return results
