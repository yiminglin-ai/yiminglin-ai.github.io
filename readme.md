# Life in the UK practice

> No trackers,
> No ads,
> Free.

More than 3000 questions from various sources.

This is a fork of the original [Life in the UK test](https://maxwellito.github.io/life-in-the-uk/) by maxwellito, intended for personal practice and question auditing using LLMs.

## Question Auditing

This repository contains scripts to audit and correct the question database using LLMs.

1.  Run `python3 split_questions.py` to generate batches in `audit_batches/`.
2.  Use an LLM (like ChatGPT or Claude) with the `audit_prompt.txt` to review each batch.
3.  Save the corrected JSON files in `audit_batches_corrected/`.
4.  Run `python3 merge_questions.py` to update `questions_base.json`.
