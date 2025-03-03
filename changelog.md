# Updates
## 18.11.24
- following last updates errors occurring due to changes to paths - amended
- previous default reference was stored in inaccessible local dir - added to data folder

## 28.10.24
- merged dev branch -> main
- updated README.md

      added sections on:
        - project info
        - install instructions
        - projects main usage 
        - detailed description
        - modules within repository
        - instructions on how to use (terminal commands)
        - troubleshooting
- "tidying-up" of mpox_kmer_typing.py
```
- created mpox_kmer_typing/commands.py
    - moved get_args -> commands.py
- created mpox_kmer_typing/directories.py
    - moved logic involved with folder creation -> set_up_log_folder -> directories.py
- changed mpox_kmer_typing/mpox_typing_functions/ -> mpox_kmer_typing/analytics/
- created mpox_kmer_typing/analytics/processing.py
  - moved logic involved with checking if reference sketch is specified -> check_ref_sketch -> processing.py
  - moved logic involved with checking input file exists -> check_input_file -> processing.py
  - moved logic processing fasta/q -> process_fastq, create_seq_sketch -> processing.py
  - moved logic checking mash file creation -> check_mash_file_status -> processing.py
```
- started adding type-hints where applicable