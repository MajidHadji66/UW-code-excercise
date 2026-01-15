import unittest
from app import validate_fasta

class TestFastaValidation(unittest.TestCase):
    def test_valid_fasta(self):
        valid_fasta = ">Test_Sequence\nATGCATGCATGC"
        result = validate_fasta(valid_fasta)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, "Test_Sequence")

    def test_invalid_fasta_no_header(self):
        invalid_fasta = "ATGCATGCATGC"
        result = validate_fasta(invalid_fasta)
        self.assertIsNone(result)

    def test_empty_string(self):
        result = validate_fasta("")
        self.assertIsNone(result)

    def test_multiple_records(self):
        multi_fasta = ">Seq1\nATGC\n>Seq2\nGCTA"
        result = validate_fasta(multi_fasta)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
