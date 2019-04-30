#!/bin/bash

echo "-------------------------------------------"
echo "Running bedtools bamtobed for your BAM file"
echo "-------------------------------------------"

bedtools bamtobed -i $1 > tradis.bed ##$1 should be the bam file of reads from TraDIS

echo "----------------------------------------------------"
echo "Editing BED file to describe just the start position"
echo "----------------------------------------------------"

describe_start_bed.py tradis.bed > start_sort.bed

echo "-------------------------------"
echo "Converting genome to BED format"
echo "-------------------------------"

gb2bed $2 > genome.bed ##$2 is .gbk of genome annotation

echo "--------------------------------------------------------"
echo "Removing descriptions from BED file of genome annotation"
echo "--------------------------------------------------------"

genome_bedit.py genome.bed > edit_genome.bed

echo "--------------------------------------------------------------"
echo "Running grep -w -f" $3 "edit_genome.bed"
echo "--------------------------------------------------------------"

grep -w -f $3 edit_genome.bed > essential_genome.bed ##$3 is essential gene names with one name per line

echo "----------------------------------------------------"
echo "Determining intersection of reads to essential genes"
echo "----------------------------------------------------"

bedtools intersect -wo -a essential_genome.bed -b start_sort.bed > essential_reads.txt

echo "---------------------"
echo "Cleaning up directory"
echo "---------------------"

rm tradis.bed start_sort.bed genome.bed edit_genome.bed essential_genome.bed 

echo "----------------------------------------------------------"
echo "COMPLETE. Find your reads in the file: essential_reads.txt"
echo "----------------------------------------------------------"
