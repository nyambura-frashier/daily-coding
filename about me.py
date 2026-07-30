first_name="frashier"
last_name="mburu"
Age=18
height="5'4"
weight=67
university="jkuat"
course="computer science"

def myfunc():
    global course
    course="biomedical science"
myfunc()
print(f"""
first_name:{first_name}
last_name:{last_name}
Age:{Age}
height:{height}
Weight:{weight}
University:{university}
course:{course}""")

