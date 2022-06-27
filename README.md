# Seed-Guided Topic Discovery with Out-of-Vocabulary Seeds

This repository contains the source code for [**Seed-Guided Topic Discovery with Out-of-Vocabulary Seeds**](https://arxiv.org/abs/2205.01845).

## Links

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Data](#data)
- [Running on New Datasets](#running-on-new-datasets)
- [Citation](#citation)

## Installation
The code is written in C and Python 3.6. The Python dependencies are summarized in the file ```requirements.txt```. You can install them like this:
```
pip3 install -r requirements.txt
```

## Quick Start
To reproduce the results in our paper, you need to first download the [**datasets**](https://drive.google.com/file/d/1bH5xpUxkQeKfniDt79UtDNfHdOVw7V2F/view?usp=sharing). Three datasets are used in our paper: **SciDocs**, **Amazon** and **Twitter**. Once you unzip the downloaded file (i.e., ```SeeTopic.zip```), you can see **five** folders: ```scidocs/```, ```amazon/```, and ```twitter``` are the dataset folders of SciDocs, Amazon, and Twitter, respectively; ```bert-base-uncased/``` and ```biobert-v1.1/``` contain the pre-trained [BERT](https://huggingface.co/bert-base-uncased) and [BioBERT](https://huggingface.co/dmis-lab/biobert-v1.1) models downloaded from Hugging Face.

Put the five folders under the main directory ```./```. Then you need to run the following script.
```
./seetopic.sh
```
The topic mining result will be in ```{dataset}/keywords_seetopic.txt```. For example, if you are using the SciDocs dataset, the result will be in ```scidocs/keywords_seetopic.txt```.

To evaluate the result (using automatic evaluation metrics), you need to run the following script.
```
./evaluation.sh
```
PMI, NPMI, LCP, and Diversity scores will be printed out.

## Data
Three datasets are used in our paper. For each dataset, we use 60% of the documents to perform topic mining and the remaining 40% for automatic evaluation (i.e., calculating PMI, NPMI, and LCP scores). In each dataset folder, you can see three files. We use ```scidocs/``` as an example for explanation.

(1) ```scidocs/scidocs.txt``` contains the 60% of the documents to perform topic mining. Each line is a document.

(2) ```scidocs/scidocs_test.txt``` contains the remaining 40% of the documents for automatic evaluation. Each line is a document.

(3) ```scidocs/keywords_0.txt``` contains the seeds used in topic mining. Each line is a seed.
```
0:cardiovascular_diseases
1:chronic_kidney_disease
2:chronic_respiratory_diseases
3:diabetes_mellitus
4:digestive_diseases
5:hiv/aids
6:hepatitis_a/b/c/e
7:mental_disorders
8:musculoskeletal_disorders
9:neoplasms_(cancer)
10:neurological_disorders
```

## Running on New Datasets
If you have a new dataset, please take the following steps to run our code on your dataset.

(1) Prepare the input files. You need a corpus (```{dataset}/{dataset}.txt```) to perform topic mining and a set of seeds (see ```{dataset}/keywords_0.txt```). If you would like to calculate the PMI, NPMI, and LCP scores, you need a corpus (```{dataset}/{dataset}_test.txt```) to count the (co-)occurrence of top-ranked terms.

(2) You can use any tool to preprocess your corpus (e.g., phrase chunking, lowercasing). If you would like to follow our practice, please refer to the [CatE](https://github.com/yumeng5/CatE/tree/master/preprocess) preprocessing step, which uses [AutoPhrase](https://github.com/shangjingbo1226/AutoPhrase).

(3) You can use any BERT-based pre-trained language model that you think is more suitable for your seeds and corpus (e.g., [BERT-cased](https://huggingface.co/bert-base-cased), [SciBERT](https://huggingface.co/allenai/scibert_scivocab_uncased), [ChemBERT](https://huggingface.co/jiangg/chembert_cased)).

(4) ```./seetopic.sh```. Make sure you have changed the dataset name and the language model folder.

## Citation
If you find the implementation useful, please cite the following paper:
```
@article{zhang2022seed,
  title={Seed-Guided Topic Discovery with Out-of-Vocabulary Seeds},
  author={Zhang, Yu and Meng, Yu and Wang, Xuan and Wang, Sheng and Han, Jiawei},
  journal={arXiv preprint arXiv:2205.01845},
  year={2022}
}
```
