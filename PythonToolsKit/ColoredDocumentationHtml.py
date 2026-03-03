#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This package implements tools to build python package and tools.
#    Copyright (C) 2026  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This package implements tools to build python package and tools.
This module implements a tool to generate a custom pydoc HTML
page for a colored HTML documentation.
"""

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This package implements tools to build python package and tools.
"""
license = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/PythonToolsKit"

copyright = """
PythonToolsKit  Copyright (C) 2026  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
__license__ = license
__copyright__ = copyright

__all__ = []

# python3 -m zipapp -c -p "/usr/bin/env python3" PythonToolsKit
# python3 -m zipapp . -o "../ColoredDocumentationHtml.pyz" -c -p "/usr/bin/env python3" -m "ColoredDocumentationHtml:main"

import os
import re
import sys
import pydoc
import importlib
from pathlib import Path

CUSTOM_CSS = """
<style>
body {
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-family: "Segoe UI", Roboto, Arial, sans-serif;
    padding: 2rem;
}

/* Main container tables */
table.section {
    border-radius: 8px;
    margin-bottom: 2rem;
    padding: 0.5rem;
}

/* ===== COLOR PER SECTION CATEGORY ===== */
.title-decor { background-color: #3a3d1e !important; }
.functions-decor { background-color: #3a1e3d !important; }
.data-decor { background-color: #1e3a3d !important; }
.author-decor { background-color: #3d2e1e !important; }
.index-decor { background-color: #1e3d2f !important; }

/* Code blocks */
pre {
    background-color: #2d2d2d;
    padding: 1rem;
    border-radius: 6px;
    overflow-x: auto;
}

/* Links */
a { color: #4ec9b0; text-decoration: none; }
a:hover { text-decoration: underline; }
</style>
"""

def sanitize_html(html: str) -> str:
    """
    Sanitize HTML by:
    - Removing sensitive parts of file: links (like full paths)
    - Keeping the filename intact
    """

    def clean_file_link(match):
        # Full <a> tag
        full_tag = match.group(0)
        # Extract inner text (e.g., full path)
        inner_text_match = re.search(r'>(.*?)<', full_tag)
        if not inner_text_match:
            return full_tag
        inner_text = inner_text_match.group(1)
        # Keep only the filename
        filename = os.path.basename(inner_text)
        # Return tag with filename only
        return f'<a>{filename}</a>'

    # Match only <a href="file:...">...</a>
    html = re.sub(r'<a\s+href="file:[^"]*">.*?</a>', clean_file_link, html, flags=re.DOTALL)

    return html

def generate_colored_pydoc(module_name: str, output_file: str | None = None):
    """
    Generate a full HTML documentation page for a Python module,
    inject custom CSS styling, and sanitize local file paths.
    """

    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        print(f"Error: could not import module '{module_name}'")
        print(e)
        sys.exit(1)

    html_doc = pydoc.HTMLDoc()
    content = html_doc.document(module)
    content = sanitize_html(content)
    full_page = html_doc.page(
        title=f"Documentation - {module_name}",
        contents=CUSTOM_CSS + content
    )

    if output_file is None:
        output_file = f"{module_name}.html"

    output_path = Path(output_file).resolve()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_page)

    print(f"Documentation successfully generated: {output_path}")

def main() -> int:
    """
    The main function to start the script from the command line.
    """

    if len(sys.argv) < 2:
        print("Usage: python generate_pydoc_colored.py <module_name> [output_file]")
        sys.exit(1)

    module_name = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    generate_colored_pydoc(module_name, output_file)
    return 0

if __name__ == "__main__":
    sys.exit(main())