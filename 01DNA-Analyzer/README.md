# 🧬 DNA Sequence Analyzer

A beginner-friendly bioinformatics project built with Python to analyze DNA sequences and perform basic sequence analysis operations.

## 📌 Project Overview

The DNA Sequence Analyzer is a command-line application that accepts a DNA sequence from the user and performs several basic bioinformatics operations, including nucleotide counting, GC content calculation, reverse complement generation, DNA-to-RNA transcription, and RNA-to-protein translation.

This project demonstrates the application of Python programming concepts to biological sequence analysis.

## ✨ Features

- **DNA Validation:** Checks whether the input contains only valid DNA nucleotides (A, T, G, C).
- **Nucleotide Counting:** Counts the occurrences of A, T, G, and C.
- **Sequence Length:** Calculates the total number of nucleotides.
- **GC Content Calculation:** Calculates the percentage of guanine (G) and cytosine (C) in the DNA sequence.
- **Reverse Complement:** Generates the reverse complement of the DNA sequence.
- **DNA Transcription:** Converts a DNA sequence into an RNA sequence by replacing T with U.
- **Protein Translation:** Translates RNA codons into amino acids using the standard genetic code and stops at a stop codon.

## 🛠️ Technologies Used

- Python 3
- `collections.Counter`
- String manipulation
- Dictionaries
- Functions
- Basic bioinformatics concepts

## 📂 Project Structure

```text
dna-analyzer/
├── dna_analyzer.py
├── tests/
│   └── test_dna_analyzer.py
└── README.md
```

_Note: The `tests/` directory is optional until you add your test file._

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your system.
- Git (optional, for cloning the repository).

Check your Python installation:

```bash
python3 --version
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/dna-analyzer.git
```

2. Navigate to the project directory:

```bash
cd dna-analyzer
```

3. Run the program:

```bash
python3 dna_analyzer.py
```

Replace `YOUR-USERNAME` with your GitHub username and adjust the repository name if necessary.

## 💻 Example Usage

### Input

```text
Enter your DNA sequence: ATGGCCATTGTA
```

### Output

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

_Note: The output values above illustrate the expected format; verify them against your program before publishing._

## 🧪 Example Invalid Input

```text
Enter your DNA sequence: ATGX123
Invalid DNA sequence!
Enter a sequence containing only A, T, G and C.
```

## 🧬 Bioinformatics Concepts

This project introduces several fundamental concepts in bioinformatics:

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

- Read DNA sequences from FASTA files.
- Add automated unit tests.
- Support batch analysis of multiple sequences.
- Add DNA motif searching.
- Generate a detailed analysis report.
- Add command-line arguments for file-based analysis.

## 👩‍💻 Author

**Your Name**

Aspiring bioinformatics learner exploring Python programming and computational biology.

## 📄 License

This project is available for educational purposes. Add a license file if you want to specify the terms under which others may use, modify, or distribute your code.
