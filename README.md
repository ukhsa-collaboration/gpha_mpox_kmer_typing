# GPHA: mpox kmer Typing

### Info
- version: 0.1 (development)
- last updated (30.10.24)
- pathogen: mpox
- function: 
- author: Deb
- summary: Repository containing code to rapidly identify the clade of mpox sequences using kmer typing.


### Install
```
git clone https://gitlab.phe.gov.uk/gpha/analysis-and-evaluation/mpox_kmer_typing.git
cd mpox_kmer_typing
conda env create -n mpox_kmer_typing -f environment.yml
conda activate mpox_kmer_typing
pip install .
```

### Install (For developers)
```
git clone https://gitlab.phe.gov.uk/gpha/analysis-and-evaluation/mpox_kmer_typing.git
cd mpox_kmer_typing
conda env create -n mpox_kmer_typing -f environment.yml
conda activate mpox_kmer_typing
pip install -e ".[dev]"
pytest . 
```

### Description
This document contains the instructions on how to run the mpox kmer typing scan. This scan has been developed 
to rapidly identify mpox clades (I & II) basd on calculated kmer distances on both fasta & fastq file formats
and for 
- a) single sequences
- b) multiple-sequences

The scan has been packaged as container to allow for integration with CORE <name_of_pipeline> NEXTflow pipeline 
located on the SMED. In addition to it being able to still being used locally on user's personal device.

### Modules
```
src
- analytics
  - kmer_typing_functions.py: application of kmer logic functions
  - processing.py: functions concerning the running of typing functions
- commands.py: contains argparse class relating to ingest and processing of terminal commands
- directories.py: functions concerning logic of selecting location and creation of sub-folders
- logfile.py: functions overwriting format of logging.py file
- mpox_kmer_typing.py: main file
```

### Instructions
Usage
```
mpox_kmer_typing -t <["fastq", "fasta"]> -i <dir_input> -o: <dir_output} -r <refsketch>
```
- -t: type - specify input file type, ["fastq", "fasta"]
- -i: input - path to input file
- -o: output - output folder for results files
- -r: refsketch - path to reference sketch file

