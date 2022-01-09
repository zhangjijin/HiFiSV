# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:13:18 2022

@author: jijin
"""

import subprocess
import sys

def hifiasm(fastq,sample,threads):
        
    hifiasm_cmd = ' hifiasm -o {sample}.asm -t  {threads}  --primary {fastq} '.format(
        sample = sample,
        fastq = fastq,
        threads = threads)
    
    hifiasm_cmd2 = "awk '/^S/{{print \">\"$2;print $3}}' {sample}.asm.p_ctg.gfa > {sample}.asm.fa".format(
        sample = sample)
    
    print("Executing Hifiasm",end='\n',flush=True,file=sys.stderr)
    
    subprocess.call(hifiasm_cmd,shell=True,stdout=subprocess.DEVNULL)
    subprocess.call(hifiasm_cmd2,shell=True,stdout=subprocess.DEVNULL)
    
    print("DONE", file=sys.stderr)