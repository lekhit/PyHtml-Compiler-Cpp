
import sys
original_stdout = sys.stdout
output_file = open('pyout.txt', 'w')
sys.stdout = output_file
for i in range(3): 
  print(f"""
  div class="row":
    div class="col-lg-4 col-sm-12":
    div class="project-wrapper__text load-hidden":
      h3 class="project-wrapper__text-title":
        Project Title {i}
      div:
        p class="mb-4":
          Describe the project being very specific, you can use the Twitter standard: no more than 280 characters
          complement the information: the skills learned or reinforced in its realization and how you faced it, 
          prove to be proactive in the search for solutions.
      
      a rel="noreferrer" target="_blank" class="cta-btn cta-btn--hero" href="#!":
        See Live
      a rel="noreferrer" target="_blank" class="cta-btn text-color-main" href="#!":
        Source Code
    div class="col-lg-12 col-sm-12 mt-4":
     div class="project-wrapper__image load-hidden":
      a rel="noreferrer" href="#!" target="_blank":
        div data-tilt data-tilt-max="4" data-tilt-glare="true" data-tilt-max-glare="0.5" class="thumbnail rounded js-tilt":
          <img
            alt="Project Image"
            class="img-fluid"
            src="assets/project.jpg"
          />""")
      

sys.stdout = original_stdout
output_file.close()