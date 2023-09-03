
import sys
original_stdout = sys.stdout
output_file = open('pyout.txt', 'w')
sys.stdout = output_file
for i in range(10):
    print(f"""
              div class={i}:
                  hello world
                        div class={i+1}:
                            hi hello world
    """)

sys.stdout = original_stdout
output_file.close()