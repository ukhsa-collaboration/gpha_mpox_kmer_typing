#!/usr/bin/env nextflow
// nextflow.enable.dsl=2

params.type = "$fasta"
params.input = "$data/kamituga_test.fna"
params.output = "$data"
params.refsketch = "$data/k31_s1000_orthopox_refs_genomic_renamed.fna.msh"


process mpox {
    """
    python src/mpox_kmer_typing/mpox_kmer_typing.py
    """

}

workflow ingest {
    take:
        type
        input
        output
        refsketch
    
    main:
      mpox(type, input, output, refsketch)

}
