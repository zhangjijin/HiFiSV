# HiFi_SV
* [HiFiSV](https://github.com/zhangjijin/HiFi_SV/blob/main/LOGO.png)
A robust pipeline for detecting genome SVs using PacBio HiFi resequencing data.
### 01_formatConveert
A series of scripts for converting to and from the aligned formats. (file formats include output file from LAST, MUMMER, Minimap2 and so on)
#### maf2sam
    maf-convert -f reference.dict sam -r 'ID:ID PL:PL SM:SM' INPUT.maf  > OUTPUT.sam
reference.dict:
    java -jar picard.jar CreateSequenceDictionary REFERENCE=INPUT.fa OUTPUT=reference.dict
#### sam2bam (sam from maf)
    sambamba view -h -S --format=bam INPUT.sam > OUTPUT.bam
    sambamba sort  INPUT.bam -o OUTPUT.sort.bam
#### sam2delta (sam from maf)
Before the format conversion, we need to adjust the Cigar in the Sam file:
```
awk 'BEGIN{OFS="\t"}{if($0~/^@/){print $0}else{gsub(/=/,"M",$6);gsub(/X/,"M",$6);print $0}}'  INPUT.sam > OUTPUT.sam
```
then:
```
python sam2delta.py INPUT.sam 
```
