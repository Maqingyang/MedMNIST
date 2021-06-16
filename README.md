# MedMNIST 

## Implemented Models

Implemeted models lie in medmnist/my_models.py. Import the models you want in the train.py to test them.


# Code Structure
* [`medmnist/`](medmnist/):
    * [`dataset.py`](medmnist/dataset.py): PyTorch datasets and dataloaders of MedMNIST.
    * [`models.py`](medmnist/models.py): *ResNet-18* and *ResNet-50* models.
    * [`my_models.py`](medmnist/models.py): My implementations of *ResNet-18* and *ResNet-50* models.
    * [`evaluator.py`](medmnist/evaluator.py): Standardized evaluation functions.
    * [`info.py`](medmnist/info.py): Dataset information `dict` for each subset of MedMNIST.
* [`train.py`](train.py): The training and evaluation script to reproduce the baseline results in the paper.
* [`getting_started.ipynb`](getting_started.ipynb): Explore the MedMNIST dataset with jupyter notebook. It is **ONLY** intended for a quick exploration, i.e., it does not provide full training and evaluation functionalities (please refer to [`train.py`](train.py) instead). 
* [`setup.py`](setup.py): The script to install medmnist as a module

  
# Citation
If you find this project useful, please cite our paper as:

      Jiancheng Yang, Rui Shi, Bingbing Ni. "MedMNIST Classification Decathlon: A Lightweight AutoML Benchmark for Medical Image Analysis," arXiv preprint arXiv:2010.14925, 2020.

or using bibtex:
     
     @article{medmnist,
     title={MedMNIST Classification Decathlon: A Lightweight AutoML Benchmark for Medical Image Analysis},
     author={Yang, Jiancheng and Shi, Rui and Ni, Bingbing},
     journal={arXiv preprint arXiv:2010.14925},
     year={2020}
     }

# LICENSE
The code is under Apache-2.0 License.

The datasets are under Creative Commons (CC) Licenses in general, please refer to the [project page](https://medmnist.github.io/#citation) for details. 
