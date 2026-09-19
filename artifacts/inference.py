# Standalone inference for the Polyglot Shorthand encoder.
# Requires: torch, tokenizers, and normalization.py exported alongside this file.
import json, torch
from tokenizers import Tokenizer

ART = "."                     # directory holding best.pt / tokenizer.json / config.json

def load(device="cpu"):
    cfg = json.load(open(f"{ART}/config.json"))
    tok = Tokenizer.from_file(f"{ART}/tokenizer.json")
    state = torch.load(f"{ART}/best.pt", map_location=device)
    return cfg, tok, state

# Rebuild PolyglotForTasks with the classes from the notebook, load `state`,
# then reuse prep() / feat.encode() / classify() exactly as defined there.
