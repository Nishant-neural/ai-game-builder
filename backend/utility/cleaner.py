import re

def clean_html_output(output):
  

    output = re.sub(r"```html", "", output)
    output = re.sub(r"```", "", output)

   
    if "Changes made:" in output:
        output = output.split("Changes made:")[0]

    return output.strip()