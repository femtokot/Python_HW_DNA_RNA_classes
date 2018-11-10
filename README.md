# Python_HW_DNA_RNA_classes
Contains two classes for work with DNA and RNA (home work python course)
DNA and RNA classes


Here I wrote two classes which should characterize DNA or RNA sequences. 
As input they accept only "ATGC" ("atcg") or "AUGC" ("aucg") repectively.
By reverse_complement  method you can convert sequences to reverse-complement
GC method calculates GC contend of nucleotide sequence

For DNA you can obtain the result of transcription by transcribe method

******************************************************************************************************
# Usage  

## Input - DNA or RNA sequence: 

```
x = Dna("tttttttaaaaaccc")
y = Rna ("uuAggcgcgu")
```
Uppercase and lowercase is acceptable. In the case of input sequence contaning symbols different from nucleotides error message will appear: 'Not DNA.' or 'Not RNA.'


## Calculating of GC content 

Example:
```
input   x.gc()  
output  20.0 

input   y.gc()
output  60.0
```

## Reverse-complement strand: 
```
For DNA:
input   x.reverse_complement() 
output  GGGTTTTTAAAAAAA      


For RNA:
input   y.reverse_complement()    
output  ACGCGCCUAA   
```
## Transcribtion DNA sequence to RNA sequence: 
DNA is coding strand!!!!!!!
Class Dna method

```
input   y.transcribe() 
output  UUUUUUUAAAAACCC
```
    
