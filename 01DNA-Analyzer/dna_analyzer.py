from collections import Counter

CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def validate_dna(dna):
    return bool(dna) and all(base in "ATGC" for base in dna)

def count_nucleotides(dna):
    counts = Counter(dna)
    return {base: counts[base] for base in "ATGC"}

def calculate_gc(dna):
    if not dna:
        raise ValueError("DNA sequence cannot be empty")

    return (dna.count("G") + dna.count("C")) / len(dna) * 100

def reverse_complement(dna):
    return  dna.translate(str.maketrans("ATGC", "TACG"))[::-1]

def transcribe_dna(dna):
    return dna.replace("T", 'U')   

def translate_dna(dna):
    rna = transcribe_dna(dna)
    protein = []
    for i in range(0, len(dna) -2, 3):
        codon = rna[i:i+3]
        amino_acid =CODON_TABLE[codon]

        if amino_acid == "*":
            break
        protein.append(amino_acid)
    return "".join(protein)

def analyze_dna():
    dna = input("Enter your DNA sequence: ")
    dna = dna.upper().strip()
    if not dna:
        print("Empty string. Please enter a DNA sequence.")
        return
    
    if not validate_dna(dna):
        print("Invalid DNA Sequence!")
        print("Enter a non-empty sequence containing only A, T, G and C.")
        return

    counts = count_nucleotides(dna)
    gc_percentage = calculate_gc(dna)
    complement = reverse_complement(dna)
    rna = transcribe_dna(dna)
    protein = translate_dna(dna)

    print("\n====== DNA SEQUENCE ANALYZER ======")
    print("DNA sequence:      ", dna)
    print("Sequence length:   ", len(dna))
    print("Nucleotide counts: ", counts)
    print(f"GC percentage:      {gc_percentage:.2f}%")
    print("Reverse complement:", complement)
    print("RNA sequence:      ", rna)
    print("Protein sequence:  ", protein)
    print("Validation:         Valid DNA")
    print("===================================")


if __name__ == "__main__":
    analyze_dna()
