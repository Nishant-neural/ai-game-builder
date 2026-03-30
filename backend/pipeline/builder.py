from pipeline.gdd_agent import generate_gdd
from pipeline.code_agent import generate_phaser_code
from pipeline.validator import validate_code
from pipeline.cleaner import clean_html_output

def run_pipeline(prompt: str):
   gdd = generate_gdd(prompt)

   for attempt in range(3):
      code = generate_phaser_code(gdd)
      code = clean_html_output(code)

      errors = validate_code(code)

      if errors:
         print("Retrying due to errors:", errors)

      else:
         break
         
   return {
        "gdd": gdd,
        "code": code,
         "errors": errors
    }