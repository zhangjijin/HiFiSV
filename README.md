# HiFiSV
![image](https://github.com/zhangjijin/HiFi_SV/blob/main/LOGO.png)
## Overview
HiFiSV,a robust and integrative pipeline for detecting genome SVs using PacBio HiFi resequencing data.It is a Python based program, combining 27 genome structural variations (SVs) detection pipelines. 
This program contains two modes of SVs calling pipelines, one is SVs calling through directly map PacBio ccs reads data to the reference genome, the other is SVs calling through reads assembly and align the assembled contigs to the reference genome. 
Details of the program are shown below.
![image](https://github.com/zhangjijin/HiFi_SV/blob/main/overview.png)
The entire pipeline is designed as follow.
![image](https://github.com/zhangjijin/HiFi_SV/blob/main/HiFi-SV.png)

## Installation

```
# Get hifisv source code
wget -O hifisv.tar.gz https://github.com/zhangjijin/HiFi_SV/archive/refs/tags/v0.1.0.tar.gz
tar xvzf hifisv.tar.gz
# Change to directory
cd HiFi_SV-0.0.1
# Create conda environment with all dependencies
conda env create -n hifisv-env -f hifisv_env.yml
# Activate environment
conda activate hifisv-env
# To test if the installation was successful run
$ python the/path/to/hifiSV.py -h
# Deactivate environment
$ conda deactivate
```
## Usage
```
python the/path/to/hifiSV.py -m <allrun/readmode/contigmode> -r <ref.fasta> -f <query.fastq> <options>
```
Parameter
**parameter** | **Description** | **Default**
 -------- | :-----------:  | :-----------: 
 -m/--mode | allrun:Run all pipelines<br>readmode:Only run pipelines through reads mapping<br>contigmode:Only run pipelines through aligning after contigs assembly | allrun
 -r/--reference | The input reference genome fasta file | None
 -f/--fastq | The input Pacbio HiFi ccs fastq file | None
 --min-depth | Minimum number of reads that support a SV | 1
 -t/--threads | Number of running threads | 1
  -s/--sample | Sample name | sample

## Output
All output results are normalized to VCF format and stored in the outputVCF subdirectory of the running directory.
## Contact
For advising, bug reporting and requiring help, please post on Github Issue or contact jijinzhang@genetics.ac.cn.
