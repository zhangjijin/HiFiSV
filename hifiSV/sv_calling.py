# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:39:04 2021

@author: jijin
"""

import subprocess
import os
import sys

path = os.getcwd()  
file_path = str(path) + '/' + "outputVCF"
if os.path.exists(file_path) is False:
    os.mkdir(file_path)
#print(file_path)
    
def svim_calling(fa,aligner,sample,mindepth):
    
    svim_cmd = 'svim alignment {sample}.{aligner}.svim {sample}.{aligner}.bam  {fa} --sequence_alleles --minimum_depth {mindepth} '.format(
        aligner = aligner,
        sample = sample,
        fa = fa,
        mindepth = mindepth)
    
    
    svimvcf = 'mv {path}/{sample}.{aligner}.svim/variants.vcf {file_path}/{sample}.{aligner}.svim.vcf'.format(
        sample = sample,
        path = path,
        aligner= aligner,
        file_path= file_path)
    
    print("Executing SVIM",end='\n',flush=True,file=sys.stderr)
    subprocess.call(svim_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(svimvcf,shell=True,stdout=subprocess.DEVNULL)
    #print(svim_cmd)
    print("DONE", file=sys.stderr)
    
def pbsv_calling(fa,aligner,sample,threads):
    
    pbsv_cmd = 'pbsv discover {sample}.{aligner}.bam {sample}.{aligner}-pbsv.svsig.gz && pbsv call {fa} {sample}.{aligner}-pbsv.svsig.gz {sample}.{aligner}.pbsv.vcf -j {threads} --min-N-in-gap 1000 --filter-near-reference-gap 0 --ccs'.format(
        sample = sample,
        aligner = aligner,
        fa = fa,
        threads = threads)
    
    pbsvvcf = 'mv {sample}.{aligner}.pbsv.vcf {file_path}/ '.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    print("Executing pbsv",end='\n',flush=True,file=sys.stderr)
    subprocess.call(pbsv_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(pbsvvcf,shell=True,stdout=subprocess.DEVNULL)
    print(pbsv_cmd)
    print("DONE", file=sys.stderr)
    
    
def cutesv_calling(fa,aligner,sample,threads,mindepth):
    
    cutesv_cmd = ' mkdir {sample}.{aligner}-cuteSV & cuteSV {sample}.{aligner}.bam {fa} {sample}.{aligner}.cutesv.vcf {sample}.{aligner}-cuteSV -t {threads} -s {mindepth} --max_cluster_bias_INS 1000 --diff_ratio_merging_INS 0.9 --max_cluster_bias_DEL 1000 --diff_ratio_merging_DEL 0.5'.format(
        aligner = aligner,
        sample = sample,
        fa = fa,
        threads = threads,
        mindepth = mindepth)
    
    cutesvvcf = ' mv {sample}.{aligner}.cutesv.vcf  {file_path}/'.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    
    print("Executing cuteSV",end='\n',flush=True,file=sys.stderr)
    subprocess.call(cutesv_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(cutesvvcf,shell=True,stdout=subprocess.DEVNULL)
    print(cutesv_cmd)
    print("DONE", file=sys.stderr)
    
def sniffles_calling(aligner,sample,threads,mindepth):
    
    sniffles_cmd = 'sniffles -m {sample}.{aligner}.bam -v {sample}.{aligner}.sniffles.vcf -t {threads} -s {mindepth} --ccs_reads'.format(
       sample = sample,
       aligner = aligner,
       threads = threads,
       mindepth = mindepth)
    
    snifflesvcf = 'mv {sample}.{aligner}.sniffles.vcf  {file_path}/ '.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    
    
    print("Executing Sniffles",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(sniffles_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(snifflesvcf,shell=True,stdout=subprocess.DEVNULL)
    
    print(sniffles_cmd)
    print("DONE", file=sys.stderr)
    

    
def svim_calling2(fa,aligner,sample,mindepth):
    
    svim_cmd = 'svim alignment {sample}.{aligner}.align.svim {sample}.{aligner}.align.bam  {fa} --sequence_alleles --minimum_depth {mindepth} '.format(
        aligner = aligner,
        sample = sample,
        fa = fa,
        mindepth = mindepth)
    
    svimvcf = 'mv {path}/{sample}.{aligner}.align.svim/variants.vcf {file_path}/{sample}.{aligner}.align.svim.vcf'.format(
        sample = sample,
        path = path,
        aligner= aligner,
        file_path= file_path)
    
    print("Executing SVIM",end='\n',flush=True,file=sys.stderr)
    subprocess.call(svim_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(svimvcf,shell=True,stdout=subprocess.DEVNULL)
    print(svim_cmd)
    print("DONE", file=sys.stderr)
    
def pbsv_calling2(fa,aligner,sample,threads):
    
    pbsv_cmd = 'pbsv discover {sample}.{aligner}.align.bam {sample}.{aligner}.align.pbsv.svsig.gz && pbsv call {fa}  {sample}.{aligner}.align.pbsv.svsig.gz {sample}.{aligner}.align.pbsv.vcf -j {threads} --min-N-in-gap 1000 --filter-near-reference-gap 0 --ccs'.format(
        sample = sample,
        aligner = aligner,
        fa = fa,
        threads = threads)
    
    pbsvvcf = 'mv {sample}.{aligner}.align.pbsv.vcf {file_path}/ '.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    
    print("Executing pbsv",end='\n',flush=True,file=sys.stderr)
    subprocess.call(pbsv_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(pbsvvcf,shell=True,stdout=subprocess.DEVNULL)
    print(pbsv_cmd)
    print("DONE", file=sys.stderr)
    
    
def cutesv_calling2(fa,aligner,sample,threads,mindepth):
    
    cutesv_cmd = ' mkdir {sample}.{aligner}.align.cuteSV & cuteSV {sample}.{aligner}.align.bam {fa} {sample}.{aligner}.align.cutesv.vcf {sample}.{aligner}.align.cuteSV -t {threads} -s {mindepth} --max_cluster_bias_INS 1000 --diff_ratio_merging_INS 0.9 --max_cluster_bias_DEL 1000 --diff_ratio_merging_DEL 0.5'.format(
        aligner = aligner,
        sample = sample,
        fa = fa,
        threads = threads,
        mindepth = mindepth)
    
    cutesvvcf = ' mv {sample}.{aligner}.align.cutesv.vcf  {file_path}/'.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    
    print("Executing cuteSV",end='\n',flush=True,file=sys.stderr)
    subprocess.call(cutesv_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(cutesvvcf,shell=True,stdout=subprocess.DEVNULL)
    print(cutesv_cmd)
    print("DONE", file=sys.stderr)
    
def sniffles_calling2(aligner,sample,threads,mindepth):
    
    sniffles_cmd = 'sniffles -m {sample}.{aligner}.align.bam -v {sample}.{aligner}.align.sniffles.vcf -t {threads} -s {mindepth} --ccs_reads'.format(
       sample = sample,
       aligner = aligner,
       threads = threads,
       mindepth = mindepth)
    
    snifflesvcf = 'mv {sample}.{aligner}.align.sniffles.vcf  {file_path}/ '.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    
    print("Executing Sniffles",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(sniffles_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(snifflesvcf,shell=True,stdout=subprocess.DEVNULL)
    
    print(sniffles_cmd)
    print("DONE", file=sys.stderr)
    
def assemblytics(caller,aligner,sample,SURVIVOR):
    
    assemblytics_cmd = '{caller} {sample}.{aligner}.filter.delta {sample}.{aligner} 10000 50  1000000000'.format(
        caller = caller,
        aligner = aligner,
        sample = sample)
    
    assemblyticsvcf1 = ' {SURVIVOR} convertAssemblytics {sample}.{aligner}.Assemblytics_structural_variants.bed 50 {sample}.{aligner}.align.Assemblytics.vcf'.format(
        aligner = aligner,
        sample = sample,
        SURVIVOR = SURVIVOR)
    
    assemblyticsvcf2 = ' mv {sample}.{aligner}.align.Assemblytics.vcf {file_path}/ '.format(
        sample = sample,
        aligner = aligner,
        file_path= file_path)
    
    print("Executing Assemblytics",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(assemblytics_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(assemblyticsvcf1,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(assemblyticsvcf2,shell=True,stdout=subprocess.DEVNULL)

    print("DONE", file=sys.stderr)
    

def svim_asm(caller,aligner,sample,ref):
    
    svim_asm_cmd = '{caller} haploid {sample}.{aligner}.svimasm {sample}.{aligner}.align.bam {ref} '.format(
        caller = caller,
        aligner = aligner,
        sample = sample,
        ref = ref)
    
    svim_asmvcf = 'mv {sample}.{aligner}.svimasm/variants.vcf  {file_path}/{sample}.{aligner}.align.svimasm.vcf '.format(
        sample = sample,
        aligner = aligner,
        file_path = file_path)
    
    print("Executing SVIM-asm",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(svim_asm_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(svim_asmvcf,shell=True,stdout=subprocess.DEVNULL)

    print("DONE", file=sys.stderr)
    
    

    
    