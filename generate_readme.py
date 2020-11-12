#! usr/bin/python

import re

from core import Iced_Exploits
from core import Iced_Exploits_Collection
from main import all_tools


def sanitize_anchor(s): 
    return re.sub(r"\w", "-", s.lower())
    
    
def get_toc(tools, indentation = ""): 
    md = "" 
    for tool in tools: 
        if ininstance(tool, Iced_Exploits_Collection): 
            md += (indentation + "- [{}](#{})\n".format(
                tool.TITLE, sanitize_anchor(tool.TITLE)))
            md += get_toc(tool.TOOLS, indentation = indentation +   '   ')
    return md
    
def generate_readme(): 
    tox = get_toc(all_tools[:-1])
    tools_desc = get_tools_toc(all_tools[:-1])
    
    with open("README_template.md") as fh: 
        readme_template = fh.read() 
        
    readme_template = readme_template.replace("{{toc}}", toc) 
    readme_template = readme_template.replace("{{tools}}", tools.desc) 
    
    with open("README.md", "w") as fh:
        fh.write(readme_template)
        
if __name__ == '__main__':
    generate_readme()