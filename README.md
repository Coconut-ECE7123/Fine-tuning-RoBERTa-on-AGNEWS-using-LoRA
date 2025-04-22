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

This project is built based on an open-source github project https://github.com/kuangliu/pytorch-cifar . <br> 
The final result is a modified ResNet with `4.9M` parameters that realize `95.49%` accuracy on CIFAR-10 and `85.10%` accuracy on Kaggle test set. <br>
[Model Structure](https://github.com/Coconut-ECE7123/ECE7123-DL-Project1/blob/main/model%20structure.png)
### Main modifications done upon the original codes: <br>
#### Model 
1. replaced Residual Block by Bottleneck Block
2. halved the channel width for tensors in 4 layers
3. block numbers for 4 layers: [2, 4, 6, 2]
4. introduced SE attention into Bottleneck Block
#### Training 
1. data augmentation
2. MLFlow for monitoring
3. early stopping (patience=30)
4. label smoothing(factor=0.01)
## Exp. Env.
All the experiments in this project were done on a remote Linux server platform `AutoDL`.  <br>
|`GPU`|`Cuda`|`Python`|`PyTorch`|`Pretrained`|`Label Smoothing`|`Batch Size`|`Worker`|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|RTX3090 | 12.1 | 3.12.3 | 2.3.0|False|0.01|128|16|
|`Optimizer`|`Scheduler`|`lr0`|`lrf`|`Momentum`|`Weight Decay`|`Patience`|`Epoch`|
|SGD|Cosine Annealing|5e-2|5e-4|0.9|5e-4|30|200|
  





































