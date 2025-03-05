#!/usr/bin/env nextflow
// nextflow.enable.dsl=2

params.type = "fasta"
params.input = "data/kamituga_test.fna"
params.output = ""
params.refsketch = "data/k31_s1000_orthopox_refs_genomic_renamed.fna.msh"


process mpox {
    container = "docker_files/Dockerfile"
    take:
        type 
        input
        output
        refsketch

    """
    python src/mpox_kmer_typing/mpox_kmer_typing.py ${type} ${input}
    """

}

workflow {
      mpox(params.type params.input params.output params.refsketch)

}
