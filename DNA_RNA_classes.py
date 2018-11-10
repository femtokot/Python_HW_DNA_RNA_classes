
class Dna(str):
    def __new__(cls, value):
        if not set(value).issubset(set("ATGCatgc")):
            raise ValueError("Not DNA.")
        return super().__new__(cls, value)

    def gc (self):                    # GC content in %
        gc_number = 0
        for nucleotide in self:
            if nucleotide in "GCgc":
                gc_number += 1
        print((gc_number/len(self)) * 100)

    def reverse_complement(self):      # invert to reverse-complement strand
        rev_comp_seq = ""
        for nucleotide in self:
            if nucleotide in "Aa":
                rev_comp_seq = 'T' + rev_comp_seq
            if nucleotide in "Tt":
                rev_comp_seq = 'A' + rev_comp_seq
            if nucleotide in "Gg":
                rev_comp_seq = 'C' +rev_comp_seq
            if nucleotide in "Cc":
                rev_comp_seq = 'G' + rev_comp_seq
        print(rev_comp_seq)

    def transcribe(self):            # transcribes DNA to RNA
        transcribed = ''
        for nucleotide in self:
            if nucleotide in "Aa":
                transcribed = transcribed + 'A'
            if nucleotide in "Tt":
                transcribed = transcribed + 'U'
            if nucleotide in "Gg":
                transcribed = transcribed + 'G'
            if nucleotide in "Cc":
                transcribed = transcribed + 'C'
        print(transcribed)



class Rna(str):
     def __new__(cls, value):
        if not set(value).issubset(set("AUGCaugc")):
            raise ValueError("Not RNA.")
        return super().__new__(cls, value)

     def gc(self):                                  # GC content in %
        gc_number = 0
        for nucleotide in self:
            if nucleotide in "GCgc":
                gc_number += 1
        print( (gc_number / len(self)) * 100)

     def reverse_complement(self):                 # transcribes DNA to RNA
        rev_comp_seq = ""
        for nucleotide in self:
            if nucleotide in "Aa":
                rev_comp_seq = 'U' + rev_comp_seq
            if nucleotide in "Uu":
                rev_comp_seq = 'A' + rev_comp_seq
            if nucleotide in "Gg":
                rev_comp_seq = 'C' + rev_comp_seq
            if nucleotide in "Cc":
                rev_comp_seq = 'G' + rev_comp_seq
        print(rev_comp_seq)

x = Rna('uuAggcgcgu')
x.gc()
x.reverse_complement()
y=Dna('tttttttaaaaaccc')
y.gc()
y.transcribe()
y.reverse_complement()
