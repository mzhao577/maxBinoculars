import argparse
from binoculars import Binoculars

MODEL_PAIRS = {
    "small": ("gpt2", "gpt2-medium"),
    "large": ("gpt2-medium", "gpt2-large"),
    "falcon": ("tiiuae/falcon-7b", "tiiuae/falcon-7b-instruct"),
}

parser = argparse.ArgumentParser()
parser.add_argument("--model", choices=MODEL_PAIRS.keys(), default="small",
                    help="Model pair to use: small, large, or falcon")
args = parser.parse_args()

observer, performer = MODEL_PAIRS[args.model]

# ChatGPT (GPT-4) output when prompted with "Can you write a few sentences about a capybara that is an astrophysicist?"
sample_string = '''Dr. Capy Cosmos, a capybara unlike any other, astounded the scientific community with his
groundbreaking research in astrophysics. With his keen sense of observation and unparalleled ability to interpret
cosmic data, he uncovered new insights into the mysteries of black holes and the origins of the universe. As he
peered through telescopes with his large, round eyes, fellow researchers often remarked that it seemed as if the
stars themselves whispered their secrets directly to him. Dr. Cosmos not only became a beacon of inspiration to
aspiring scientists but also proved that intellect and innovation can be found in the most unexpected of creatures.'''

print(f"Observer: {observer}, Performer: {performer}")
bino = Binoculars(observer_name_or_path=observer, performer_name_or_path=performer)
details = bino.compute_score_detailed(sample_string)
print(f"Perplexity:       {details['perplexity']:.4f}")
print(f"Cross-perplexity: {details['cross_perplexity']:.4f}")
print(f"Binoculars score: {details['binoculars_score']:.4f}")
print(f"Prediction:       {bino.predict(sample_string)}")
