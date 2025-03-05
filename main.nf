#!/usr/bin/env nextflow
// nextflow.enable.dsl=2


include { mpox_kmer_typing } from './src/mpox_kmer_typing/'

params.type = "$fasta"
params.input = "$data/kamituga_test.fna"
params.output = "$data"
params.refsketch = "$data/k31_s1000_orthopox_refs_genomic_renamed.fna.msh"

workflow ingest {
    take:
        type
        input
        output
        refsketch
    main:
        mpox_kmer_typing(type, input, output, refsketch)

}
