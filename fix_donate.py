import re

with open('css/styles.css', 'r') as f:
    css = f.read()

# Fix donate background
css = re.sub(r'\.donate\s*\{[^}]*background:[^;]+;', 
             '.donate {\n    background: transparent;', css)

# Fix donate subtitle
css = re.sub(r'\.donate-content \.section-subtitle\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.donate-content .section-subtitle {\n    color: var(--gray-dark);\n}', css)

# Fix info-block
css = re.sub(r'\.info-block\s*\{[^}]*background:\s*rgba\([^)]+\)[^}]*border:[^;]+;', 
             '.info-block {\n    padding: 24px;\n    background: #FFFFFF;\n    border-radius: var(--radius);\n    border: none;\n    box-shadow: 0 5px 15px rgba(0,0,0,0.05);', css)

# Fix info-block headings and text
css = re.sub(r'\.info-block h4\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.info-block h4 {\n    color: var(--dark);\n    font-size: 1rem;\n    margin-bottom: 12px;\n}', css)

css = re.sub(r'\.info-block p\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.info-block p {\n    font-size: 0.9rem;\n    color: var(--gray-dark);\n    margin-bottom: 6px;\n}', css)

# Fix tax-info
css = re.sub(r'\.tax-info\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.tax-info {\n    display: flex;\n    justify-content: center;\n    gap: 16px;\n    flex-wrap: wrap;\n    font-size: 0.85rem;\n    color: var(--gray-dark);\n}', css)

# Fix donate-inkind
css = re.sub(r'\.donate-inkind\s*\{[^}]*background:\s*rgba\([^)]+\)[^}]*border:[^;]+;', 
             '.donate-inkind {\n    padding: 32px;\n    background: #FFFFFF;\n    border-radius: var(--radius-lg);\n    border: none;\n    box-shadow: 0 10px 30px rgba(0,0,0,0.05);', css)

css = re.sub(r'\.donate-inkind h4\s*\{[^}]*color:\s*var\(--white\)[^}]*\}', 
             '.donate-inkind h4 {\n    color: var(--dark);\n    font-size: 1.1rem;\n    margin-bottom: 20px;\n}', css)

css = re.sub(r'\.inkind-list span\s*\{[^}]*color:\s*rgba\([^)]+\)[^}]*\}', 
             '.inkind-list span {\n    font-size: 0.95rem;\n    color: var(--gray-dark);\n}', css)


with open('css/styles.css', 'w') as f:
    f.write(css)
