import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace CSS variables
new_vars = """:root {
    /* Primary - Yellow Theme */
    --primary: #FFB800;
    --primary-dark: #E5A600;
    --primary-light: #FFC933;
    --primary-pale: #FFF7DF;

    /* Secondary - Dark */
    --secondary: #2C2C2C;
    --secondary-dark: #1A1A1A;
    --secondary-light: #3D3D3D;

    /* Accent */
    --accent: #7BDCB5;
    --accent-light: #9CF3D1;

    /* Neutrals */
    --dark: #1A1A1A;
    --gray-dark: #4A4A4A;
    --gray: #7A7A7A;
    --gray-light: #B0B0B0;
    --light: #FFF9ED;
    --white: #FFFFFF;
    
    /* Backgrounds */
    --bg-cream: #FFFDF8;

    /* Typography */
    --font-heading: 'Poppins', sans-serif;
    --font-body: 'Poppins', sans-serif;

    /* Spacing */
    --section-padding: 80px;
    --container: 1200px;

    /* Effects */
    --shadow: 0 4px 15px rgba(255, 184, 0, 0.15);
    --shadow-lg: 0 12px 35px rgba(255, 184, 0, 0.2);
    --radius: 20px;
    --radius-lg: 32px;
}"""

css = re.sub(r':root\s*\{[^}]+\}', new_vars, css)

# Make body use bg-cream
css = css.replace('background: var(--white);', 'background: var(--bg-cream);')

# Increase roundness
css = css.replace('--radius: 8px;', '--radius: 20px;')
css = css.replace('--radius-lg: 16px;', '--radius-lg: 32px;')
css = css.replace('border-radius: 4px;', 'border-radius: 50px;')

# Update buttons to be very rounded and have subtle shadow
css = css.replace('border-radius: 50px;', 'border-radius: 50px;\n    box-shadow: 0 4px 15px rgba(255, 184, 0, 0.3);')

# The hero section should look like a giant pill or card
hero_updates = """
.hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding-top: 72px;
    margin: 20px;
    border-radius: 40px;
    overflow: hidden;
}
"""
css = css.replace('.hero {\n    position: relative;\n    min-height: 100vh;\n    display: flex;\n    align-items: center;\n    padding-top: 72px;\n}', hero_updates)


with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

