# NYU ECE-GY7123 MiniProject2 - Fine-tuning RoBERTa on AGNEWS using LoRA
## Project Info.
**Team Name**: 🥥 Coconut <br>
**Team Member**: Ziyan Zhao🤠; Haotian Xu🐱‍👤; Tianqi Xia🐱‍🏍<br>

`config.py`: all LoRA configurations implemented and testd in this project <br>
`ensembling.ipynb`: assembly prediction on Kaggle testset - `test_unlabelled.pkl` <br>
`main.ipynb`: model training and validation code on AGNEWS dataset <br>
`param_test.ipynb`: code for checking the quantity of trainable parameters <br>
`pred.ipynb`: model inference on Kaggle testset using checkpoint model weights <br>
`test_unlabelled.pkl`: Kaggle test set <br>

This project is built based on the `Starter_Notebook.ipynb` provided by NYU ECE-GY7123. <br> 
The final result is obatined by model assembly that uses 4 best performed models on Kaggle dataset, the highest among which owns `0.889M` parameters. The final test accuracy is `84.3%` that is over the benchmark metric. <br>

### Main modifications done upon the original codes: <br>
#### Model 
Ablation experiments were performed with various LoRA configurations by dividing the 12-layer RoBERTa model into 2-4 sections. We implemented smaller r values and LoRA dropout in the shallow layers while gradually increasing both rank r and LoRA
dropout in the middle and deeper layers near the model output. In total, we experimented with 9 different configurations and fine-tuned the LoRA-dropout regularization parameter.
#### Training 
1. Lion Optimizer (lr=1e-4 weight_decay = 2e-2)
2. Cosine annealing scheduler with warmup period (6% steps)
3. Batch size = 16
4. early stopping (patience=10)
5. max steps = 2500
## Exp. Env.
All the experiments in this project were done on a remote Linux server platform `AutoDL`.  <br>
|`GPU`|`Cuda`|`Python`|`PyTorch`|`Pretrained`|`LoRA`|`Batch Size`|`Worker`|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|A100 | 12.1 | 3.12.3 | 2.3.0|True|True|16|64|
|`Optimizer`|`Scheduler`|`lr0`|`lrf`|`Momentum`|`Weight Decay`|`Patience`|`Epoch`|
|Lion|Cosine Annealing|1e-4|5e-11|0.9|2e-2|10|1|
  
### Training Process Record: <br>














