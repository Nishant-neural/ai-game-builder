import re

def clean_html_output(output: str):
    # remove ```html
    output = re.sub(r"```html", "", output)

    # remove ```
    output = re.sub(r"```", "", output)

    return output.strip()