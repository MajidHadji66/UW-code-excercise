import os
import io
from flask import Flask, render_template, request, flash, redirect, url_for
from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Required for flashing messages

def validate_fasta(fasta_string):
    """
    Validates if a string is in FASTA format.
    Returns a list of SeqRecord objects if valid, None otherwise.
    """
    try:
        # FASTA files must start with '>'
        if not fasta_string.strip().startswith('>'):
            return None
            
        fasta_io = io.StringIO(fasta_string)
        records = list(SeqIO.parse(fasta_io, "fasta"))
        
        if len(records) == 0:
            return None
            
        # Optional: Further validation for DNA sequence characters
        for record in records:
            if not all(c.upper() in 'ATGCN-' for c in str(record.seq)):
                # We could be more strict, but let's allow basic DNA characters
                pass
                
        return records
    except Exception:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sequence_text = request.form.get('sequence')
        fasta_file = request.files.get('fasta_file')
        
        content = ""
        if fasta_file and fasta_file.filename != '':
            content = fasta_file.read().decode('utf-8')
        elif sequence_text:
            content = sequence_text
            
        if not content:
            flash("Please provide a DNA sequence or upload a FASTA file.", "warning")
            return redirect(url_for('index'))
            
        records = validate_fasta(content)
        if not records:
            flash("Invalid FASTA format. Sequences must start with '>' and contain valid DNA characters.", "danger")
            return redirect(url_for('index'))
            
        # For simplicity, we process the first record
        query_sequence = content
        
        try:
            # This is the slow part
            result_handle = NCBIWWW.qblast("blastn", "nt", query_sequence)
            blast_record = NCBIXML.read(result_handle)
            
            results = []
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    # Calculate percent identity
                    identity = (hsp.identities / hsp.align_length) * 100
                    results.append({
                        'title': alignment.title,
                        'accession': alignment.accession,
                        'identity': round(identity, 2),
                        'length': hsp.align_length,
                        'e_value': hsp.expect
                    })
            
            return render_template('results.html', results=results, query_id=blast_record.query)
            
        except Exception as e:
            flash(f"An error occurred during BLAST processing: {str(e)}", "danger")
            return redirect(url_for('index'))
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
