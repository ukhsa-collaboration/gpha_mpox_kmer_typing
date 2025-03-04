#!/usr/bin/env nextflow
// nextflow.enable.dsl=2

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
        get_params_and_versions(unique_id)

        preprocess(unique_id)

        classify_and_report(preprocess.out.processed_fastq, preprocess.out.combined_fastq, params.raise_server)
        extract_all(preprocess.out.processed_fastq, classify_and_report.out.assignments, classify_and_report.out.kreport, classify_and_report.out.taxonomy)

    emit:
        html_report = classify_and_report.out.report
}
