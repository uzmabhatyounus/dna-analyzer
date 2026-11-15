# 🧬 DNA Sequence Analyzer

## 📌 Project Overview

A beginner-friendly bioinformatics project built with Python to analyze DNA sequences and perform fundamental sequence analysis operations.

The DNA Sequence Analyzer is a command-line application that accepts a DNA sequence from the user and performs operations such as nucleotide counting, GC content calculation, reverse complement generation, DNA-to-RNA transcription, and RNA-to-protein translation.

This project demonstrates the application of Python programming to biological sequence analysis.

## ✨ Features

- **DNA Validation:** Validates DNA sequences containing only A, T, G, and C.
- **Nucleotide Counting:** Counts the occurrences of each nucleotide.
- **Sequence Length:** Calculates the total number of nucleotides.
- **GC Content Calculation:** Calculates the percentage of guanine (G) and cytosine (C).
- **Reverse Complement:** Generates the reverse complement of a DNA sequence.
- **DNA Transcription:** Converts DNA into RNA by replacing thymine (T) with uracil (U).
- **Protein Translation:** Translates RNA codons into amino acids using the standard genetic code and stops at a stop codon.

## 🛠️ Technologies Used

- Python 3
- `collections.Counter`
- String manipulation
- Dictionaries and functions
- Basic bioinformatics concepts

## 📂 Project Structure

```text
dna-analyzer/
├── dna_analyzer.py
├── tests/
│   └── test_dna_analyzer.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3
- Git (optional, for cloning the repository)

Check your Python installation:

```bash
python3 --version
```

### Installation and Execution

1. Clone the repository:

```bash
git clone https://github.com/uzmabhatyounus/dna-analyzer.git
```

2. Navigate to the project directory:

```bash
cd dna-analyzer
```

3. Run the program:

```bash
python3 dna_analyzer.py
```

## 💻 Example Usage

### Input

```text
Enter your DNA sequence: ATGGCCATTGTA
```

### Example Output

```text
====== DNA SEQUENCE ANALYZER ======
DNA sequence:       ATGGCCATTGTA
Sequence length:    12
Nucleotide counts:  {'A': 3, 'T': 3, 'G': 4, 'C': 2}
GC percentage:      50.00%
Reverse complement: TACAATGGCCAT
RNA sequence:       AUGGCCAUUGUA
Protein sequence:   MAIV
Validation:         Valid DNA
===================================
```

## 🧪 Invalid Input Handling

The program validates input and rejects sequences containing invalid characters.

### Example

```text
Enter your DNA sequence: ATGX123
Invalid DNA sequence!
Enter a sequence containing only A, T, G and C.
```

## 🧬 Bioinformatics Concepts

- DNA nucleotide composition
- GC content analysis
- Complementary DNA strands
- Transcription from DNA to RNA
- Translation of RNA codons into amino acids
- The genetic code and stop codons

## 🎯 Learning Objectives

Through this project, I practiced:

- Writing reusable Python functions
- Working with strings, dictionaries, and counters
- Validating user input
- Implementing basic biological sequence analysis
- Applying Python to practical bioinformatics problems

## 🔮 Future Improvements

- Read DNA sequences from FASTA files
- Expand automated unit test coverage
- Support batch analysis of multiple sequences
- Implement DNA motif searching
- Generate detailed analysis reports
- Add command-line arguments for file-based analysis

## 👩‍💻 Author

**Uzma Usman**

Aspiring bioinformatics professional exploring Python programming, genomics, and computational biology.





This project is intended for educational purposes. Licensing terms can be specified by adding a `LICENSE` file to the repository.
