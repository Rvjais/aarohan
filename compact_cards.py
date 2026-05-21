import re

with open('css/styles.css', 'r') as f:
    css = f.read()

# Remove grid-row: span 2 from impact-primary
css = css.replace('grid-row: span 2;', '')

# Reduce padding on impact-card
css = css.replace('padding: 32px 24px;', 'padding: 20px 16px;')

# Reduce impact-icon size
css = css.replace('width: 80px;\n    height: 80px;', 'width: 50px;\n    height: 50px;')
css = css.replace('font-size: 40px;', 'font-size: 24px;')
css = css.replace('margin: 0 auto 20px auto;', 'margin: 0 auto 12px auto;')

# Reduce outcome-number font size a bit to fit compact cards
css = css.replace('font-size: 3rem;', 'font-size: 2.2rem;')
css = css.replace('font-size: 2rem;', 'font-size: 1.8rem;')

# Reduce gaps in the grid if needed to make them more tightly packed
css = css.replace('gap: 24px;', 'gap: 16px;')

with open('css/styles.css', 'w') as f:
    f.write(css)
