from pipeline.gdd_agent import generate_gdd
from pipeline.code_agent import generate_phaser_code
from pipeline.validator import validate_code
from pipeline.cleaner import clean_html_output
from pipeline.correction_agent import correct_code

def run_pipeline(prompt: str):
   gdd = generate_gdd(prompt)

   
   code = generate_phaser_code(gdd)
   code = clean_html_output(code)
   
   for attempt in range(3):
      errors = validate_code(code)

      if errors:
         print(f"Attempt number:{attempt+1} , fixing errors:", errors)
         code = correct_code(code, errors)
         code = clean_html_output(code)
        
      else:
         print("code is valid:::")
         break
         
   return {
        "gdd": gdd,
        "code": code,
         "final_errors": validate_code(code)
    }