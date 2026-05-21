import re

with open('css/styles.css', 'r') as f:
    css = f.read()

# Replace the current header override block
old_header = """/* Update Header */
.header {
    border-radius: 0 0 30px 30px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    margin: 0 20px;
    top: 10px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
}"""

new_header = """/* Update Header */
.header {
    border-radius: 0 0 30px 30px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    margin: 0 20px;
    top: 10px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.header.scrolled {
    margin: 0;
    top: 0;
    border-radius: 0;
    background: var(--primary);
    box-shadow: 0 10px 30px rgba(230, 121, 23, 0.3);
}

/* Hide topbar when scrolled */
.topbar {
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    max-height: 100px;
    opacity: 1;
    overflow: hidden;
}
.header.scrolled .topbar {
    max-height: 0;
    padding: 0;
    opacity: 0;
    border: none;
}

/* Nav links and logo animation */
.header .nav-link {
    transition: color 0.3s ease;
}
.header.scrolled .nav-link {
    color: var(--white) !important;
}
.header.scrolled .nav-link:hover {
    color: var(--light) !important;
}
.header.scrolled .nav-link::after {
    background: var(--white);
}
.header .logo img {
    transition: all 0.4s ease;
}
.header.scrolled .logo img {
    filter: brightness(0) invert(1);
    transform: scale(0.9);
}

/* Adjust dropdown menu links to stay dark */
.header.scrolled .dropdown-menu .nav-link {
    color: var(--gray-dark) !important;
}
.header.scrolled .dropdown-menu a:hover {
    color: var(--primary) !important;
}

/* Update header button when scrolled */
.header.scrolled .btn-primary {
    background: var(--white);
    color: var(--primary);
}
.header.scrolled .btn-primary:hover {
    background: var(--light);
}
"""

if old_header in css:
    css = css.replace(old_header, new_header)
else:
    # If not found exactly, just append it
    css += "\n" + new_header

with open('css/styles.css', 'w') as f:
    f.write(css)
