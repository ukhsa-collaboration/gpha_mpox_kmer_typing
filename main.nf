#!/usr/bin/env nextflow
// nextflow.enable.dsl=2

params.type = "fasta"
params.input = "data/kamituga_test.fna"
params.output = ""
params.refsketch = "data/k31_s1000_orthopox_refs_genomic_renamed.fna.msh"


process mpox {
    container = "docker_files/Dockerfile"

    type = "fasta"
    input = "data/kamituga_test.fna"
    output = ""
    refsketch = "data/k31_s1000_orthopox_refs_genomic_renamed.fna.msh"
    print("running mpox scan")
    """
    python src/mpox_kmer_typing/mpox_kmer_typing.py --type type --input input --refsketch refsketch
    """

}

workflow {
      mpox()

}
