# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:10:43 2021

@author: jijin
"""

import subprocess
import sys

def mummer_align(ref,query,sample,threads):
    ## mummer version > 4.0
    nucmer_cmd = 'nucmer --mum  -t {threads} {ref} {query} -p {sample}.mummer '.format(
        ref = ref,
        query = query,
        sample = sample,
        threads=threads)
        

    nucmer_filter = 'delta-filter -1 {sample}.mummer.delta > {sample}.mummer.filter.delta'.format(
        sample = sample)
    
    nucmer_show_coords = 'show-coords -THrd  {sample}.mummer.filter.delta >  {sample}.mummer.filter.coords '.format(
        sample = sample)
        
    print("Executing Mummer",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(nucmer_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(nucmer_filter,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(nucmer_show_coords,shell=True,stdout=subprocess.DEVNULL)
    
    print("DONE", file=sys.stderr)
    
    
def minimap2_align(ref,query,threads,sample):
    
    minimap2_align = ' minimap2 -a -x asm5 --cs -r2k -t {threads}  {ref}  {query} > {sample}.minimap2.align.sam '.format(
        ref = ref,
        query = query,
        threads = threads,
        sample = sample)
    
 
    
    minimap2_sam = 'sambamba view -h -S --format=bam {sample}.minimap2.align.sam > {sample}.minimap2.align.tmp.bam'.format(
        sample = sample)
    
    minimap2_sort = 'sambamba sort  -t {threads} {sample}.minimap2.align.tmp.bam -o {sample}.minimap2.align.bam'.format(
        threads = threads,
        sample = sample)
    
    print("Executing Minimap2",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(minimap2_align,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(minimap2_sam,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(minimap2_sort,shell=True,stdout=subprocess.DEVNULL)
    
    print("DONE", file=sys.stderr)
    
def last_align(ref,query,threads,sample):
    
    last_1 = 'lastdb -P{threads} -uNEAR -R01 {sample} {ref}'.format(
        ref = ref,
        sample = sample,
        threads = threads)
    
    last_2 = 'last-train -P{threads} --revsym --matsym --gapsym -E0.05 -C2 {sample} {query} > {sample}.last.mat '.format(
        query = query,
        sample = sample,
        threads = threads)
    
    last_3 = 'lastal -m50 -E0.05 -P{threads} -C2 -p {sample}.last.mat {sample} {query} | last-split -m1 > {sample}.last.tmp.maf '.format(
        query = query,
        threads=threads,
        sample = sample)
    
    last_4 = 'maf-swap {sample}.last.tmp.maf | awk \'/^s/ {{$2 = (++s % 2 ? "{sample}" : "") $2}} 1\' | last-split -m1 | maf-swap > {sample}.last.maf'.format(
        sample = sample)
    
    print("Executing LAST",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(last_1,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(last_2,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(last_3,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(last_4,shell=True,stdout=subprocess.DEVNULL)
    
    print("DONE", file=sys.stderr)
    
def pbmm2_align(ref,query,threads,sample):
    pbmm2_align = 'pbmm2 align -j {threads}  --preset CCS --sort --rg \'@RG\\tID:{sample}\\tSM:{sample}\'  {ref} {query} > {sample}.pbmm2.align.bam '.format(
        threads = threads,
        ref = ref,
        query = query,
        sample = sample)
    pbmm2_index = 'samtools index {sample}.pbmm2.align.bam'.format(
        sample = sample)
    
    print("Executing pbmm2",end='\n',flush=True,file=sys.stderr)
  
    subprocess.call(pbmm2_align,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(pbmm2_index,shell=True,stdout=subprocess.DEVNULL)
    

    print("DONE", file=sys.stderr)
    
def ngmlr_align(ref,query,threads,sample):
    
    ngmlr_cmd = ' ngmlr  -t {threads}  -r {fa} -q {fq} -o {sample}.ngmlr.align.sam  --rg-id {sample} --rg-sm {sample} --rg-lb library --rg-pl PACBIO --rg-pu unit1'.format(
        threads = threads,
        fa = ref,
        fq = query,
        sample = sample)
    
    ngmlr_sam = 'sambamba view -h -S --format=bam {sample}.ngmlr.align.sam > {sample}.ngmlr.align.tmp.bam'.format(
        sample = sample)
    
    ngmlr_sort = 'sambamba sort  -t {threads} {sample}.ngmlr.align.tmp.bam -o {sample}.ngmlr.align.bam'.format(
        threads = threads,
        sample = sample)
    
    ngmlr_rm = 'rm {sample}.ngmlr.align.tmp.bam'.format(
        sample = sample)
    
    print("Executing NGMLR",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(ngmlr_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(ngmlr_sam,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(ngmlr_sort,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(ngmlr_rm,shell=True,stdout=subprocess.DEVNULL)
    
    print("DONE", file=sys.stderr)
    

    

    
