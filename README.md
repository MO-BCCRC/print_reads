#PrintReads : Renders, in SAM/BAM format, all reads from the input data set in the order in which they appear in the input file.


```
Development information

date created : Sep 09 2014
last update  : Sep 09  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Realigned alignment, BQSR file (1st Step), reference genome, dbsnp 
Output       : Recalibrated Alignment
Seed used    : <no_seed>

```


###Usage

PrintReads can dynamically merge the contents of multiple input BAM files, resulting in merged output sorted in coordinate order. Can also optionally filter reads based on the --read_filter command line argument.

Note that when PrintReads is used as part of the Base Quality Score Recalibration workflow, it takes the --BQSR engine argument, which is listed under Inherited Arguments > CommandLineGATK below.

###Dependencies

- GATK
- python



###Example

```
java -Xmx2g -jar GenomeAnalysisTK.jar \
   -R ref.fasta \
   -T PrintReads \
   -o output.bam \
   -I input1.bam \
   -I input2.bam \
   --read_filter MappingQualityZero

 // Prints the first 2000 reads in the BAM file
 java -Xmx2g -jar GenomeAnalysisTK.jar \
   -R ref.fasta \
   -T PrintReads \
   -o output.bam \
   -I input.bam \
   -n 2000

 // Downsamples BAM file to 25%
 java -Xmx2g -jar GenomeAnalysisTK.jar \
   -R ref.fasta \
   -T PrintReads \
   -o output.bam \
   -I input.bam \
   -dfrac 0.25
   
```

###Known issues

(will update later)

###Last updates

(will update later)

### test data
Reference : /genesis/extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite   
seq1 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R1_001.fastq 
seq2 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R2_001.fastq  
outfile : test.bam   

bowtie2 path : /genesis/extscratch/shahlab/raniba/Software/bowtie2/  
samtools path : /extscratch/shahlab/raniba/pipelines/miseq_pipeline/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools 


