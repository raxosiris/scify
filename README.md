# Understanding Scientific Literature at ever higher Levels

This repo experiments with scientific text mining, relation extraction, claim verification and topic modelling. The goal is to extract semantically meaningful relations for use in knowledge graphs for insight mining.  

Biomedical and [scientific literature datasets](https://allenai.org/data/s2orc) (*July 2020: 800GB, 130M papers, 12M fulltext pubs*) are getting better and plentier and there's many new papers with code that push the SOTA. Just the last couple of months we saw double digit improvements in F1 in many sub-tasks, like claim extraction, finding emerging concepts, NER, NEL, denoising distant supervision data generation, claim verification and so on. I shared [some of my thoughts and research](https://roamresearch.com/#/app/markus/page/7epJgOL3X) on this before. 



## Easy Auto Setup

**I prepped this repo so setup is automatic, painless and fast.** Just *code and data*, no fighting with the environment or data prep.

*If you work with a new dataset, please add the URL and helper scripts as you see it in the /script folder so it's easy to reproduce.*

After `git clone`, go inside the project `root` directory, do this:


```shell
// create conda env (I named it scify)
conda env create -f environment.yml

// activate conda env
conda activate scify

// install libraries
pip3 install -r requirements.txt

// download models (spacy, scispacy and so on)
pip3 install -r download_models.txt

// download datasets
python scify/scripts/downloader.py
//if there's an error then go to scripts/dataset_urls.py and download with the url from your browser

// install scify kernel for jupyter
ipython kernel install --user --name=scify
```

~~`Attention!` The pubmed xml samples you have to download [here]([ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline-2018-sample/](ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline-2018-sample/)) because the request lib in `downloader.py` doesn't handle `FTP`. [TODO]~~ *Nevermind just fixed it...*

## Datasets
[Global Network of Biomedical Relations](https://academic.oup.com/bioinformatics/article/34/15/2614/4911883) This paper is great. The distribution and data files. Table3 has the *THEMES* that dependency graphs are clustered in *(eg. show support for)*: This is what's in the distribution files.

```python
from 
```



PubMed XML dumps: Be careful. The XMLs are often not correctly formatted and can't be imported. 



`Hint`: Often Jupyter saves spaCy models locally in /var/folders/vl/



## ENTITY LINKING

`UMLS` is huge and takes long to load even when cached



*`python` is not homoiconic
