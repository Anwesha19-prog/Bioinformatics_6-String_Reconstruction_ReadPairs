# Bioinformatics_6-String_Reconstruction_ReadPairs

# 📘 README: String Reconstruction from Read-Pairs

---

### 🔍 Problem Overview

In **genome sequencing**, paired-end reads are short reads that are sequenced from both ends of a DNA fragment. This problem asks you to reconstruct the original DNA string using these **paired reads**, each composed of two k-length sequences with a gap of known distance $d$ between them.

The problem is solved by constructing a **paired de Bruijn graph** and finding a valid path through it that respects the gap between paired reads.

---

### 🧠 Why Is This Problem Important?

* 💉 **Bioinformatics:** Reflects real-world genome assembly with paired-end reads
* 📊 **Data Reconstruction:** Combines partial and offset-aligned data into a full sequence
* 🔜 **Graph Algorithms:** Teaches graph traversal under additional constraints (gap alignment)

---

### 👈 Problem Statement

Given:

* Integers $k$ and $d$
* A collection of read pairs formatted as `k-mer1|k-mer2`

Return:

* A string whose (k,d)-mer composition corresponds to these read pairs

---

### 📅 Input Format

A text file (`input.txt`) like this:

```
4 2
GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT
```

---

### 📈 Output Format

A text file (`output.txt`) with the reconstructed string:

```
GTGGTCGTGAGATGTTGA
```

---

### ⚙️ How to Use

#### 🛠️ Requirements

* Python 3.x

#### ✨ Steps

1. Save the input in `input.txt`.
2. Run the script:

   ```bash
   python read_pairs_reconstruction.py
   ```
3. Check the result in `output.txt`

---

### 🧪 How It Works

1. Parses the read-pairs and builds a **paired de Bruijn graph**.
2. Each node is a pair of (k-1)-mers.
3. Edges represent valid transitions between read pairs.
4. An **Eulerian path** is found through this graph.
5. The output string is formed by merging the first and second sequences of the path with a $d$-length gap.

---

### 📁 Project Structure

```
read_pairs_reconstruction.py   # Python script
input.txt                      # Paired reads input
output.txt                     # Reconstructed string
README.md                      # This file
```

---

### 📆 Sample Run

**Input:**

```
4 2
GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT
```

**Output:**

```
GTGGTCGTGAGATGTTGA
```

---

### 📌 Notes

* Assumes a valid Eulerian path exists.
* Handles one correct reconstruction; other valid results may exist.
* Requires careful string merging based on k and d.

---

Next up: **Contig Generation from Reads** →
