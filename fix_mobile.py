import re

with open('css/styles.css', 'r') as f:
    css = f.read()

# 1. Fix Header on Mobile
# Hide topbar and header actions (Donate button) on mobile to save space
mobile_fixes = """
    /* Mobile Header Fixes */
    .topbar {
        display: none !important;
    }
    .header-actions {
        display: none !important;
    }
    .hamburger {
        display: flex !important;
    }
    .header-inner {
        height: 60px;
    }
    
    /* Mobile Hero Fixes */
    .hero-content {
        padding: 15px;
        background: transparent !important;
        border: none !important;
        backdrop-filter: none !important;
    }
    .hero-title {
        font-size: 1.5rem !important;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 0.9rem !important;
        margin-bottom: 20px;
        line-height: 1.4;
    }
    .hero-cta {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .hero-cta .btn {
        width: 100%;
        padding: 12px;
        font-size: 0.9rem;
    }
"""

css = css.replace('.hero-title {\n        font-size: 1.8rem;\n    }', mobile_fixes)

# 2. Fix hero-content background globally (since we are back to orange theme)
css = css.replace('background: rgba(0, 0, 0, 0.4);', 'background: transparent;')
css = css.replace('border: 1px solid rgba(255,255,255,0.2);', 'border: none;')

with open('css/styles.css', 'w') as f:
    f.write(css)
