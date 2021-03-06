import click
import numpy as np
import torch
from transformers import AutoModelForMaskedLM, RobertaTokenizer

from src.utils import get_vocab, create_chars_to_words_map, get_permutations, scramble_words

# Constants
MODEL_NAME = "distilroberta-base"


class SeqUnscrambler:
    def __init__(self):
        self._vocab = get_vocab()
        self._chars_to_words_map = create_chars_to_words_map(self._vocab)
        self.tokenizer = self.load_tokenizer()
        self.model = self.load_model()

    @staticmethod
    def load_tokenizer():
        return RobertaTokenizer.from_pretrained(MODEL_NAME)

    @staticmethod
    def load_model():
        return AutoModelForMaskedLM.from_pretrained(MODEL_NAME)

    def analyze(self, text: str, top_k: int) -> list:
        sentence_perm = get_permutations(text, self._chars_to_words_map)

        log_prob_sent = {}
        for i in range(len(sentence_perm)):
            log_prob = 0
            for count in range(len(sentence_perm[i])):
                sentence = list(sentence_perm[i])
                current_token = sentence[count]
                sentence[count] = self.tokenizer.mask_token
                input_ids = self.tokenizer.encode(' '.join(sentence), return_tensors="pt")

                mask_token_index = torch.where(input_ids == self.tokenizer.mask_token_id)[1]

                token_logits = self.model(input_ids)[0]
                mask_token_logits = token_logits[0, mask_token_index, :]
                mask_token_prob = torch.softmax(mask_token_logits, dim=1)

                current_token_id = self.tokenizer.encode(current_token, add_special_tokens=False, add_prefix_space=True)[0]

                token_score = mask_token_prob[:, current_token_id].detach().numpy()[0]

                # calculate log-likelihood (pseudo)
                log_prob += np.log(token_score)

            log_prob_sent[' '.join(list(sentence_perm[i]))] = log_prob

        return sorted(log_prob_sent.items(), key=lambda item: item[1], reverse=True)[:top_k]


@click.command()
@click.option('-t', '--text')
@click.option('-k', '--top_k', default=1)
def main(text, top_k):
    unscrambler = SeqUnscrambler()
    print(f"Input text: {text}")

    scrambled_text = scramble_words(text)
    print(f"Scrambled text: {scrambled_text}\n")

    result = unscrambler.analyze(text=scrambled_text, top_k=top_k)
    print(f"Top {top_k} inferred input texts with log probability scores:\n")
    for sentence in result:
        print(f"sentence: {sentence[0]}\nscore: {sentence[1]}\n")


if __name__ == '__main__':
    main()
