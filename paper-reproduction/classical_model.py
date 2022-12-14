import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pennylane as qml
import torch
import torch.nn as nn
device = torch.device("cuda")


# initialising key constants

INPUT_DIM = 1  # num features per input
OUTPUT_DIM = 1
HIDDEN_DIM = 5
vt_dim = INPUT_DIM + HIDDEN_DIM

DEPTH = 2



class LSTM(nn.Module):

    def __init__(self):
        super().__init__()
        self.LSTM_l = nn.LSTM(input_size=INPUT_DIM, hidden_size=HIDDEN_DIM, batch_first=True)
        self.y_l = nn.Linear(HIDDEN_DIM, OUTPUT_DIM)

    def forward(self, input_seq):
        y_seq = []
        batch_size, seq_length, feature_size = input_seq.size()  # shape is  seq x features assume no batches

        ct = torch.zeros(batch_size, vt_dim)  # .to(device)
        ht = torch.zeros(batch_size, HIDDEN_DIM)  # .to(device)

        h_out, (ht, ct) = self.LSTM_l(input_seq, (ht, ct))

        y = self.y_l(h_out)
        return y


print(sum(p.numel() for p in LSTM().parameters() if p.requires_grad))