import re

with open('css/styles.css', 'r') as f:
    css = f.read()

old_css = """.header-actions {
        display: none !important;
    }"""
new_css = """.header-actions .btn {
        display: none !important;
    }"""

css = css.replace(old_css, new_css)

with open('css/styles.css', 'w') as f:
    f.write(css)
