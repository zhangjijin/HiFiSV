# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:51:05 2021

@author: jijin
"""

import argparse
import os 
from hifiSV import reads_mapping
from hifiSV import sv_calling
from hifiSV import contig_mapping
from hifiSV import format_convert
from hifiSV import assembly
parser = argparse.ArgumentParser() 
parser.add_argument('-m','--mode', type=str,help='The mode in which hifisv runs explains the visible README in detail', default='allrun')
parser.add_argument('-f','--fastq', type=str, default = None,help='the input ccs fastq file')
parser.add_argument('-r','--reference', type=str, default=None,help='the reference genome fasta file')
parser.add_argument('-d','--depth', type=int, default=5,help='estimation of sequencing depth')
parser.add_argument('-t','--threads', type=int, default=1,help='Number of running threads')
parser.add_argument('-s','--sample', help='Sample name', default='sample')
parser.add_argument("--min-depth",type = int,help = 'Minimum number of reads that support a SV',default=1)
args = parser.parse_args()

print(args)

def reads_main(fq,fa,sample,mindepth,threads):
    
    
    try:
        reads_mapping.ngmlr_mapping(fq,fa,sample,threads)
    except:
        print("NGMLR running error")
        pass
    
    try:
        reads_mapping.minimap2_mapping(fq,fa,sample,threads)
    except:
        print("Minimap2 running error")
        pass
    
    try:
        reads_mapping.pbmm2_mapping(fq,fa,sample,threads)
    except:
        print("pbmm2 running error")
        pass
    
    aligners1 = ['ngmlr','minimap2','pbmm2']
    aligners2 = ['pbmm2']
    aligners3 = ['ngmlr','minimap2']
    
    for aligner in aligners1:
        
        try:
            sv_calling.svim_calling(fa,aligner,sample,mindepth)
        except:
            print("svim after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in aligners2:
        
        try:
            sv_calling.pbsv_calling(fa,aligner,sample,mindepth)
        except:
            print("pbsv after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in aligners1:
        
        try:
            sv_calling.cutesv_calling(fa,aligner,sample,threads,mindepth)
        except:
            print("cuteSV after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in aligners3:
        
        try:
            sv_calling.sniffles_calling(aligner,sample,threads,mindepth)
        except:
            print("Sniffles after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
def assemblyfa(fq,sample,threads):
    try:
        assembly.hifiasm(fq,sample,threads)
    except:
        print("hifiasm running error")
        pass

def contig_align_svcalling(ref,query,threads,sample,assemblytics,SURVIVOR):
    
    try:
        contig_mapping.mummer_align(ref,query,sample,threads)
    except:
        print("Mummer running error")
        pass
    
    try:
        contig_mapping.minimap2_align(ref,query,threads,sample)
    except:
        print("Minimap2 running error")
        pass
    
    try:
        contig_mapping.last_align(ref,query,threads,sample)
    except:
        print("Last running error")
        pass
    
    try:
        contig_mapping.pbmm2_align(ref,query,threads,sample)
    except:
        print("Pbmm2 running error")
        pass
    
    
    try:
        contig_mapping.ngmlr_align(ref,query,threads,sample)
    except:
        print("NGMLR running error")
        pass
    
    for aligner in  ['last']:
        
        try:
            format_convert.maftobam(ref,sample,aligner)
        except:
            print("format_convert after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in  ['last']:
        
        try:
            format_convert.samtodelta(sample,aligner)
        except:
            print("format_convert after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in  ['ngmlr','minimap2']:
        
        try:
            format_convert.samtodelta(sample,aligner)
        except:
            print("format_convert after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    
    
    
    for aligner in ['ngmlr','minimap2','pbmm2','last']:
        
        try:
            sv_calling.svim_calling2(ref,aligner,sample,1)
        except:
            print("svim after {aligner} running error".format(aligner = aligner))
            pass
        continue
        
    for aligner in ['ngmlr','minimap2','pbmm2','last']:
        
        try:
            sv_calling.cutesv_calling2(ref,aligner,sample,threads,1)
        except:
            print("cutesv after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in ['ngmlr','minimap2','pbmm2','last']:
        
        try:
            sv_calling.svim_asm("svim-asm",aligner,sample,ref)
        except:
            print("cutesv after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in ['ngmlr','minimap2','mummer','last']:
        
        try:
            sv_calling.assemblytics(assemblytics,aligner,sample,SURVIVOR)
        except:
            print("Assemblytics after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in ['ngmlr']:
        
        try:
            sv_calling.sniffles_calling2(aligner,sample,threads,1)
        except:
            print("Sniffles after {aligner} running error".format(aligner = aligner))
            pass
        continue
    
    for aligner in ['pbmm2']:
        
        try:
            sv_calling.pbsv_calling2(ref,aligner,sample,threads)
        except:
            print("pbsv after {aligner} running error".format(aligner = aligner))
            pass
        continue

if __name__ == '__main__':
    if args.mode == 'allrun':
        
        reads_main(args.fastq, args.reference, args.sample, args.min_depth, args.threads)
        
        query = args.sample+'.asm.fa'
        path = os.getcwd()  
        query_path = str(path) + '/' + str(query)
    
        if os.path.exists(query_path) is False:
            assemblyfa(args.fastq,args.sample,args.threads)
        else:
            contig_align_svcalling(args.reference,query,args.threads,args.sample,'Assemblytics','SURVIVOR')
        
        
    elif args.mode == 'readmode':
        reads_main(args.fastq, args.reference, args.sample, args.min_depth, args.threads)
    elif args.mode == 'contigmode':
        query = args.sample+'.asm.fa'
        path = os.getcwd()  
        query_path = str(path) + '/' + str(query)
    
        if os.path.exists(query_path) is False:
            assemblyfa(args.fastq,args.sample,args.threads)
    
        contig_align_svcalling(args.reference,query,args.threads,args.sample,'Assemblytics','SURVIVOR')