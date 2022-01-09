# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:21:09 2022

@author: jijin
"""

import subprocess
import sys
import os

def samtodelta(sample,aligner ):
    
    
    script = os.path.join(sys.path[0], "sam2delta.py")
    
    samtodeltacmd= 'python {script} {sample}.{aligner}.align.sam '.format(
        script = script,
       sample = sample,
       aligner = aligner)
    
    mv_cmd = ' mv {sample}.{aligner}.align.sam.delta {sample}.{aligner}.filter.delta '.format(
       sample = sample,
       aligner = aligner)
    
    
    
    print("Process: convert sam to delta ",end='\n',flush=True,file=sys.stderr)
    #subprocess.call(awk_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(samtodeltacmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(mv_cmd,shell=True,stdout=subprocess.DEVNULL)
    #subprocess.call(rm_tmp,shell=True,stdout=subprocess.DEVNULL)
    print("DONE", file=sys.stderr)
    


def maftobam(ref,sample,aligner):
    
    picard_cmd = 'picard CreateSequenceDictionary REFERENCE={fa} OUTPUT=reference.dict'.format(
        fa = ref)
    
    maf_convert = 'maf-convert -f reference.dict sam -r \'ID:{sample} PL:{sample} SM:{sample}\' {sample}.{aligner}.maf  > {sample}.{aligner}.align.tmp.sam '.format(
        sample = sample,
        aligner = aligner)
    
    awk_cmd =  " awk 'BEGIN{{OFS=\"\\t\"}}{{if($0~/^@/){{print $0}}else{{gsub(/=/,\"M\",$6);gsub(/X/,\"M\",$6);split($3,a,\".\");$3=a[2];print $0}}}}' {sample}.{aligner}.align.tmp.sam > {sample}.{aligner}.align.sam  ".format(
       sample = sample,
       aligner = aligner)
    
    sambamba_view = 'sambamba view -h -S --format=bam {sample}.{aligner}.align.sam > {sample}.{aligner}.maf.bam'.format(
        sample = sample,
        aligner = aligner)
    
    sambamba_sort = 'sambamba sort  {sample}.{aligner}.maf.bam  -o {sample}.{aligner}.align.bam '.format(
        sample = sample,
        aligner = aligner)
    
    print("Process: convert maf to bam ",end='\n',flush=True,file=sys.stderr)
    subprocess.call(picard_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(maf_convert,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(awk_cmd,shell=True,stdout=subprocess.DEVNULL)    
    subprocess.call(sambamba_view,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(sambamba_sort,shell=True,stdout=subprocess.DEVNULL)
    print("DONE", file=sys.stderr)
    