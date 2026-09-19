# The Polyglot's Shorthand — PS 4

18.9M-parameter encoder for Latinised code-mixed Hinglish.
3.77% of the 500M budget, 3.02 ms end-to-end at batch 1.

| Metric | Value |
|---|---|
| Sentiment weighted F1 (SentiMix, our split) | 0.872 |
| Language ID weighted F1 (HingLID) | 0.970 |
| F1 retention under heavy spelling drift | 88.5% |
| F1 cost of removing emoji (n=232) | −6.9 points |
| Parameters | 18,868,240 (3.77% of ceiling) |
| Batch-1 p50, end-to-end | 3.02 ms |
| Peak throughput | 12,742 sent/s |

**Note on the 0.872.** SemEval gold test labels were never released, so we
evaluate on half the labelled validation file, and the MLM stage saw that
text unlabelled. This is an in-domain number, not a leaderboard result.
See §6 and §9 of the whitepaper.

## Run
Open `notebooks/polyglot_shorthand_pipeline.ipynb` on Kaggle (GPU, internet
on) and Run All — ~30 min on a T4. Weights: see Releases.

## Inference
python src/inference.py --text "bhai order cancel krdo please urgent meeting h"
