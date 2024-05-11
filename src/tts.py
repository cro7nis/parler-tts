import torch
from parler_tts import ParlerTTSForConditionalGeneration
from transformers import AutoTokenizer


class ParlerTTS:
    def __init__(self, model_id, device, cache_dir):
        super().__init__()
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = ParlerTTSForConditionalGeneration.from_pretrained(model_id, cache_dir=cache_dir).to(device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)

    @property
    def sampling_rate(self):
        return self.model.config.sampling_rate

    def generate(self, input_text, description):
        input_ids = self.tokenizer(description, return_tensors="pt").input_ids.to(self.device)
        prompt_input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids.to(self.device)
        generation = self.model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
        audio_arr = generation.cpu().numpy().squeeze()
        return audio_arr
