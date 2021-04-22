# demonstrate template string functions
from string import Template

def main():

    # string format()
    s1 = "We're learnning {0} by {1}".format("Advanced Python", "Tutorial")
    print(s1)

    # template with placeholders
    template = Template("I am learnning ${title} by ${purpose}")
    s2 = template.substitute(title= "Advanced Python", purpose= "Tutorial")
    print(s2)
    
    # use the substitute method with a dictionary
    data = {
        "purpose" : "Tutorial",
        "title" : "Advanced Python" 
    }
    s3 = template.substitute(data)
    print(s3)


if __name__ == "__main__":
    main()