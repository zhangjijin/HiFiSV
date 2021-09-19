# HiFi_SV
A robust pipeline for detecting genome SVs using PacBio HiFi resequencing data.
### 01_formatConveert
A series of scripts for converting to and from the aligned formats.
#### maf2sam
    maf-convert -f reference.dict sam -r 'ID:ID PL:PL SM:SM' INPUT.maf  > OUTPUT.sam
