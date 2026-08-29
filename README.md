# IEEE Task 0

Python exercises covering core language fundamentals (lists, loops, functions) and data analysis with NumPy, Pandas, and Matplotlib.

## Project Structure

```
IEEE_task0/
├── q1.py                              # List Analyzer
├── q2.py                              # Process List (copy, filter, sort)
├── q3.py                              # Prime check using for-else
├── numpy_basics.py                    # NumPy arrays and operations
├── pandas_analysis.py                 # Pandas CSV analysis
├── visualize_data.py                  # Matplotlib visualizations
├── student_performance.csv            # Input dataset
├── processed_student_performance.csv  # Output of pandas_analysis.py
├── final_scores.png                   # Output of visualize_data.py
├── study_vs_score.png                 # Output of visualize_data.py
├── score_distribution.png             # Output of visualize_data.py
├── custom_plot.png                    # Output of visualize_data.py
├── requirements.txt
└── README.md
```

## Setup

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd IEEE_task0
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate the virtual environment**

Windows (PowerShell):
```powershell
venv\Scripts\activate
```

Windows (Git Bash):
```bash
source venv/Scripts/activate
```

macOS / Linux:
```bash
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

## Running the Scripts

Each script can be run independently. Make sure the virtual environment is activated first.

**Q1 — List Analyzer**
```bash
python q1.py
```
Prompts for the number of elements, then the integers (space-separated on one line). Prints the largest, smallest, sum, even/odd counts, and the reversed list.

**Q2 — Process List**
```bash
python q2.py
```
Prompts for a list of integers. Returns a new list with negatives removed, `0` appended, sorted in ascending order — without modifying the original list.

**Q3 — Prime Check**
```bash
python q3.py
```
Runs `is_prime()` against a set of example values and prints the results.

**Q4 — NumPy Basics**
```bash
python numpy_basics.py
```
Creates sample NumPy arrays and demonstrates shape/dtype inspection, mean/max/min/std, vectorized operations, and Boolean indexing.

**Q5 — Pandas and CSV Analysis**
```bash
python pandas_analysis.py
```
Reads `student_performance.csv`, performs analysis (missing values, averages, filtering, sorting), and saves the result as `processed_student_performance.csv`.

> Requires `student_performance.csv` to be in the same folder as the script.

**Q6 — Visualizing the Data**
```bash
python visualize_data.py
```
Reads `processed_student_performance.csv` and generates four charts, saved as PNG files: `final_scores.png`, `study_vs_score.png`, `score_distribution.png`, and `custom_plot.png`.

> Requires `pandas_analysis.py` to be run first, since it depends on `processed_student_performance.csv`.

## Dependencies

See `requirements.txt`. Core libraries used: `numpy`, `pandas`, `matplotlib`.