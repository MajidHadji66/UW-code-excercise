# BioBLAST: Bioinformatics BLAST Web Application

A Flask-based web application to perform DNA sequence validation and NCBI BLAST queries.

## Features
- Paste DNA sequences or upload FASTA files.
- Basic FASTA format validation.
- Integration with NCBI BLAST API (qblast).
- Formatted alignment results with Percent Identity, Accession ID, and E-value.
- Modern UI built with Bootstrap 5.

## Prerequisites
- Python 3.8+
- Recommended: A virtual environment

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Testing

To run the validation logic tests, use:
```bash
python test_validation.py
```

## Note on BLAST API
The NCBI BLAST API can be slow (sometimes several minutes). The application includes a loading overlay while waiting for the response. Be patient!
