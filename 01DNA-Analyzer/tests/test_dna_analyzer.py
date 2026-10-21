
import unittest

from dna_analyzer import (
    validate_dna,
    count_nucleotides,
    calculate_gc,
    reverse_complement,
    transcribe_dna,
    translate_dna,
)


class TestDNAAnalyzer(unittest.TestCase):

    # 1. DNA validation tests

    def test_valid_dna(self):
        self.assertTrue(validate_dna("ATGC"))

    def test_invalid_dna(self):
        self.assertFalse(validate_dna("ATGX"))

    def test_empty_dna(self):
        self.assertFalse(validate_dna(""))

    def test_lowercase_dna(self):
        # The validation function expects uppercase DNA.
        self.assertFalse(validate_dna("atgc"))

    def test_dna_with_numbers(self):
        self.assertFalse(validate_dna("ATG123"))

    # 2. Nucleotide counting tests

    def test_nucleotide_count(self):
        self.assertEqual(
            count_nucleotides("AATGC"),
            {"A": 2, "T": 1, "G": 1, "C": 1},
        )

    def test_nucleotide_count_all_same(self):
        self.assertEqual(
            count_nucleotides("AAAA"),
            {"A": 4, "T": 0, "G": 0, "C": 0},
        )

    def test_nucleotide_count_empty(self):
        self.assertEqual(
            count_nucleotides(""),
            {"A": 0, "T": 0, "G": 0, "C": 0},
        )

    # 3. GC percentage tests

    def test_gc_percentage(self):
        self.assertEqual(calculate_gc("ATGC"), 50.0)

    def test_gc_percentage_all_gc(self):
        self.assertEqual(calculate_gc("GGCC"), 100.0)

    def test_gc_percentage_no_gc(self):
        self.assertEqual(calculate_gc("AATT"), 0.0)

    def test_empty_gc_percentage(self):
        with self.assertRaises(ValueError):
            calculate_gc("")

    # 4. Reverse complement tests

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("AAGC"), "GCTT")

    def test_reverse_complement_single_base(self):
        self.assertEqual(reverse_complement("A"), "T")

    # 5. Transcription tests

    def test_transcription(self):
        self.assertEqual(transcribe_dna("ATGC"), "AUGC")

    def test_transcription_without_thymine(self):
        self.assertEqual(transcribe_dna("AGGC"), "AGGC")

    # 6. Translation tests

    def test_translation(self):
        self.assertEqual(translate_dna("ATGTTT"), "MF")

    def test_stop_codon(self):
        self.assertEqual(translate_dna("ATGTAA"), "M")

    def test_incomplete_codon(self):
        # The final incomplete codon is ignored.
        self.assertEqual(translate_dna("ATGT"), "M")

    def test_empty_translation(self):
        self.assertEqual(translate_dna(""), "")


if __name__ == "__main__":
    unittest.main()
