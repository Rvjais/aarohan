import re

with open('css/styles.css', 'r') as f:
    css = f.read()

# Fix outcome-label color
css = re.sub(r'\.outcome-label\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.outcome-label {\n    display: block;\n    font-size: 0.9rem;\n    color: var(--gray-dark);\n    margin-top: 4px;\n}', css)

# Fix impact-stats background
css = re.sub(r'\.impact-stats\s*\{[^}]*background:[^;]+;', 
             '.impact-stats {\n    background: transparent;', css)

# Fix impact-header h2
css = re.sub(r'\.impact-header h2\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.impact-header h2 {\n    font-size: clamp(2rem, 4vw, 2.6rem);\n    color: var(--dark);\n    margin: 16px 0;\n}', css)

# Fix impact-header p
css = re.sub(r'\.impact-header p\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.impact-header p {\n    font-size: 1.1rem;\n    color: var(--gray-dark);\n}', css)

# Fix impact-label
css = re.sub(r'\.impact-label\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.impact-label {\n    display: block;\n    font-size: 1.1rem;\n    font-weight: 600;\n    color: var(--dark);\n    margin-top: 16px;\n}', css)

# Fix impact-sub
css = re.sub(r'\.impact-sub\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.impact-sub {\n    display: block;\n    font-size: 0.85rem;\n    color: var(--gray-dark);\n    margin-top: 4px;\n}', css)

# Fix impact-primary card
css = re.sub(r'\.impact-card\.impact-primary\s*\{[^}]*background:[^;]+;', 
             '.impact-card.impact-primary {\n    background: #FFFFFF !important;', css)
css = re.sub(r'\.impact-primary \.impact-label,\s*\.impact-primary \.impact-sub\s*\{[^}]*\}', '', css)

# Fix highlight-item strong
css = re.sub(r'\.highlight-item strong\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.highlight-item strong {\n    display: block;\n    font-size: 1.1rem;\n    color: var(--dark);\n    margin-bottom: 4px;\n}', css)

# Fix highlight-item p
css = re.sub(r'\.highlight-item p\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.highlight-item p {\n    font-size: 0.9rem;\n    color: var(--gray-dark);\n}', css)

# Fix method-detail span
css = re.sub(r'\.method-detail span\s*\{[^}]*color:\s*var\(--primary-light\)[^}]*\}', 
             '.method-detail span {\n    font-size: 0.8rem;\n    color: var(--primary);\n    font-weight: 500;\n}', css)

# Fix impact-quote
css = re.sub(r'\.impact-quote\s*\{[^}]*background:\s*rgba\([^)]+\)[^}]*\}', 
             '.impact-quote {\n    margin-top: 60px;\n    padding: 40px;\n    background: #FFFFFF;\n    border-radius: 30px;\n    text-align: center;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.05);\n    border: none;\n}', css)

css = re.sub(r'\.impact-quote blockquote\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.impact-quote blockquote {\n    font-size: clamp(1.2rem, 3vw, 1.6rem);\n    color: var(--dark);\n    font-style: italic;\n}', css)

# Fix method-card text (again just in case)
css = re.sub(r'\.method-card h3\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.method-card h3 {\n    font-size: 1.15rem;\n    color: var(--dark);\n    margin-bottom: 12px;\n}', css)
css = re.sub(r'\.method-card p\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.method-card p {\n    font-size: 0.9rem;\n    color: var(--gray-dark);\n    line-height: 1.7;\n    margin-bottom: 16px;\n}', css)

with open('css/styles.css', 'w') as f:
    f.write(css)
