# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:56:01 2022

@author: jijin
"""
import subprocess

import sys

def ngmlr_mapping(fq,fa,sample,threads):
    
    ngmlr_cmd = ' ngmlr  -t {threads}  -r {fa} -q {fq} -o {sample}.ngmlr.sam  --rg-id {sample} --rg-sm {sample} --rg-lb library --rg-pl PACBIO --rg-pu unit1'.format(
        threads = threads,
        fa = fa,
        fq = fq,
        sample = sample)
    
    ngmlr_sam = 'sambamba view -h -S --format=bam {sample}.ngmlr.sam > {sample}.ngmlr.tmp.bam'.format(
        sample = sample)
    
    ngmlr_sort = 'sambamba sort  -t {threads} {sample}.ngmlr.tmp.bam -o {sample}.ngmlr.bam'.format(
        threads = threads,
        sample = sample)
    
    ngmlr_rm = 'rm {sample}.ngmlr.tmp.bam {sample}.ngmlr.sam '.format(
        sample = sample)
    
    print("Executing NGMLR",end='\n',flush=True,file=sys.stderr)
    subprocess.call(ngmlr_cmd,shell=True,stdout=subprocess.DEVNULL)
    print(ngmlr_cmd)
    subprocess.call(ngmlr_sam,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(ngmlr_sort,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(ngmlr_rm,shell=True,stdout=subprocess.DEVNULL)
    print(ngmlr_sort)
    print(ngmlr_rm)
    print("DONE", file=sys.stderr)



def minimap2_mapping(fq,fa,sample,threads):
    
    minimap2_cmd = 'minimap2 --MD -ax asm20 -t {threads} {fa}  {fq} -o {sample}.minimap2.sam  -R \'@RG\\tID:{sample}\\tSM:{sample}\''.format(
        threads = threads,
        fa = fa,
        fq = fq,
        sample = sample)
    
    minimap2_sort = 'samtools sort  -o {sample}.minimap2.bam {sample}.minimap2.sam '.format(
        sample = sample)
    
    minimap2_index = 'samtools index {sample}.minimap2.bam'.format(
        sample = sample)
    
    minimap2_rm = 'rm {sample}.minimap2.sam'.format(
        sample = sample)
     
    print("Executing Minimap2",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(minimap2_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(minimap2_sort,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(minimap2_index,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(minimap2_rm,shell=True,stdout=subprocess.DEVNULL)
    
    print("DONE", file=sys.stderr)

def pbmm2_mapping(fq,fa,sample,threads):
    
    pbmm2_cmd = 'pbmm2 align -j {threads}  --preset CCS --sort --rg \'@RG\\tID:{sample}\\tSM:{sample}\'  {fa} {fq} > {sample}.pbmm2.bam '.format(
        threads = threads,
        fa = fa,
        fq = fq,
        sample = sample)
    
    pbmm2_index = 'samtools index {sample}.pbmm2.bam'.format(
        sample = sample)
    
    print("Executing pbmm2",end='\n',flush=True,file=sys.stderr)
  
    subprocess.call(pbmm2_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(pbmm2_index,shell=True,stdout=subprocess.DEVNULL)
    
    print(pbmm2_cmd)
    print(pbmm2_index)
    print("DONE", file=sys.stderr)