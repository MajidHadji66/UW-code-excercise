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

## Running the Application Locally

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8080
   ```



## Project Structure
- `app.py`: Main Flask application with dynamic port handling.
- `Dockerfile`: Containerization setup using Python 3.11-slim.
- `cloudbuild.yaml`: CI/CD pipeline definition for Google Cloud.
- `requirements.txt`: Project dependencies (Flask, Biopython, Gunicorn).
- `templates/`: HTML interface using Bootstrap 5.

## Technical Implementation
... (rest of the sections remain same) ...

This application is architected to prioritize user experience and biological data integrity.

### 1. Sequence Validation Logic
The application implements a robust multi-stage validation for DNA sequences:
- **Sanitization**: Leading/trailing whitespace is stripped.
- **Header Check**: Ensures the string starts with the standard FASTA `>` identifier.
- **Parsing**: Uses `Biopython's SeqIO` to verify the structure and extract sequence metadata.
- **Validation**: Confirms the sequence contains valid nucleotide characters (`A`, `T`, `G`, `C`, `N`).

### 2. Integration with NCBI BLAST
The core analysis utilizes the **NCBI BLAST API** via `NCBIWWW.qblast`. 
- **Parameters**: Currently configured for `blastn` (nucleotide-nucleotide BLAST) against the `core_nt` (Core Nucleotide) database.
- **Data Parsing**: XML results are parsed using `NCBIXML` to extract critical metrics such as **Accession ID**, **E-value**, and **Percent Identity**.

### 3. Key Design Decisions
- **Error Handling**: Comprehensive try-except blocks handle potential network timeouts or malformed inputs, providing user-friendly "flashed" notifications.
- **UI/UX**: Bootstrap 5 provides a responsive, clean interface with a loading overlay (defined in `index.html`) to manage the inherent latency of external API calls.

## Testing

To run the validation logic tests, use:
```bash
python test_validation.py
```

## Note on BLAST API
The NCBI BLAST API can be slow (sometimes several minutes) depending on sequence length and server load. The application includes a loading overlay while waiting for the response.
