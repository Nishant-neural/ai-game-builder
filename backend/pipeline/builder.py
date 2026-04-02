from pipeline.gdd_agent import generate_gdd
from pipeline.code_agent import generate_phaser_code
from pipeline.validator import validate_code
from utility.cleaner import clean_html_output
from pipeline.correction_agent import correct_code
from memory.memory_store import load_memory , save_memory, add_error

def run_pipeline(prompt: str):
   memory = load_memory()
   gdd = generate_gdd(prompt)

   
   code = generate_phaser_code(gdd)
   code = clean_html_output(code)
   
   prev_errors = None
   
   for attempt in range(3):
      errors = validate_code(code)

      if not errors:
         print("Success")
         break

      if prev_errors == errors:
         print(" No improvement — forcing stricter correction")

      for err in errors:
            add_error(memory, err)

      
      print(f"Attempt number:{attempt+1} , fixing errors:", errors)
      code = correct_code(code, errors , prev_errors)
      code = clean_html_output(code)
      prev_errors = errors
        
   save_memory(memory)      

   return {
        "gdd": gdd,
        "code": code,
         "final_errors": validate_code(code)
    }