def analyze_dna(sequence):
    # Make sure the sequence is uppercase
    sequence = sequence.upper()
    
    # Calculate the total length
    length = len(sequence)
    
    # Count each individual nucleotide base
    counts = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }
    
    # Calculate GC Content percentage
    gc_count = counts['G'] + counts['C']
    gc_percentage = (gc_count / length) * 100 if length > 0 else 0
    
    # Print the results
    print(f"--- DNA Analysis Results ---")
    print(f"Total Length: {length} bases")
    print(f"Base Counts -> A: {counts['A']}, T: {counts['T']}, G: {counts['G']}, C: {counts['C']}")
    print(f"GC Content: {gc_percentage:.2f}%")

# Test the analyzer with a sample sequence
sample_dna = "ATGCGATCGATCGATCGATCGATCGATC"
analyze_dna(sample_dna)
