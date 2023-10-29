#!/usr/bin/env python3
# Test CodeTF for parsing C++ code

# Set up steps
# 1 - Create a virtual env
#  py -3 -m venv .venv
#  .venv\Scripts\activate
#  python -m pip install --upgrade pip


# import required libraries
from transformers import pipeline
import textwrap
import numpy as np
import pandas as pd
from pprint import pprint

# from lib2to3.pgen2 import token
# from platform import python_branch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
# from torch.utils.checkpoint import checkpoint

# print(torch.__version__)

checkpoint = "Salesforce/codet5p-770m-py"
device = "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

model = AutoModelForSeq2SeqLM.from_pretrained( checkpoint,
    torch_dtype=torch.float32,
    trust_remote_code=True).to(device)

summarizer = pipeline('summarization', model=checkpoint, tokenizer=tokenizer, max_length=20, min_length=10)

code1 = " int calculator::add( int a, int b) { return a +b; } "
summary1 = summarizer(code1)

print(summary1)

# encoding = tokenizer(python_function, return_tensors="pt").to(device)
# encoding['decoder_input_ids'] = encoding['input_ids'].clone()
# outputs = model.generate(**encoding, max_length=500)
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))
