from collections import Counter


def validate_dna(dna):
    return len(dna) > 0 and all(base in "ATGC" for base in dna)

def dna_count(dna):
    return dict(Counter(dna))

def calculate_gc(dna):
    return round((dna.count("G") + dna.count('C')) / len(dna) * 100)

def reverse_compliment(dna):
    return  dna.translate(str.maketrans("ATGC", "TACG"))[::-1]

def transcribe_dna(dna):
    return dna.replace("T", 'U')   
def analyze_dna():
    dna = input("Enter your DNA sequence: ")
    dna = dna.upper()

    if not validate_dna(dna):
        print("Invalid DNA Sequence ")
        print("Enter a non-empty sequence containing only A, T, G and C.")
        return 
    print(dna_count(dna))
    print(calculate_gc(dna))
    print(reverse_compliment(dna))
    print(transcribe_dna(dna))
    

if __name__ == "__main__":
    analyze_dna()