import jinja2
from jinja2 import Environment, BaseLoader, PackageLoader

def page(template_filename, x, y, keys, var_dict):
    with open(template_filename, "r") as f:
        t = f.read()
    
    # this is kind of important, because it will set up
    # that the base_template.html referenced in "extending_template.html"
    # will be searched in "templates" in this folder, because
    # this script is called "main" and jinja will search in the 
    # "templates" folder in the same dir as "main" by default.
    T = jinja2.Environment(loader=PackageLoader("main")).from_string(t)
    
    x = str(x)+"mm"
    y = str(y)+"mm"
    
    # keyword args are 'how you define variables in the template'.
    # *because* I'm using x,y, keys, var_dict here, they are usable
    # in the template. they are not predefined.
    html = T.render(x=x, y=y, keys=keys, var_dict=var_dict)

    return html

def build(template_fn,output_fn):
    # DIN A4 page measurements
    x, y = (210, 297)

    var_dict = {
            "html title": "my example page", 
            "my first list": [
        "hello", "there", "beautiful", "world"],
            "my second list":[
        "milk","eggs","bread"],
            }
    keys = ["my first list","my second list"]
    
    my_html = page(template_fn,x,y,keys,var_dict)
    with open(output_fn,"w") as f:
        f.write(my_html)
        
def main():
    
    # this is to demonstrate the use of variables.
    build("template.html",output_fn="my_hello_world.html")
    
    # this is to demonstrate the use of blocks and replacing blocks.
    build("extending_template.html",output_fn="my_extended_hello_world.html")
    

if __name__ == "__main__":
    main()
