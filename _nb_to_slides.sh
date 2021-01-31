ls *-slides.ipynb | entr -s "jupyter nbconvert *-slides.ipynb --to slides --output-dir ."
