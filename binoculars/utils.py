from transformers import AutoTokenizer


def assert_tokenizer_consistency(model_id_1, model_id_2):
    identical_tokenizers = (
            AutoTokenizer.from_pretrained(model_id_1, local_files_only=True).vocab
            == AutoTokenizer.from_pretrained(model_id_2, local_files_only=True).vocab
    )
    if not identical_tokenizers:
        raise ValueError(f"Tokenizers are not identical for {model_id_1} and {model_id_2}.")
