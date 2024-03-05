
def main():
    # Lambdas can only contain 1 argument
    def addLamb():
        add = lambda x : x + 2
        print(add(5))
    # addLamb()

    def minusLamb():
        minus = lambda x : x - 2
        print(minus(10))
    # minusLamb()

    def multiplyLamb():
        minus = lambda x, y : x * y
        print(minus(15, 4))
    # multiplyLamb()

    def divideLamb():
        divide = lambda x, y : x / y
        print(divide(20, 5))
    # divideLamb()
        
    def powerLamb():
        power = lambda x, y : x ** y
        print(power(25, 2))
    # powerLamb()
    
    def reverseStrLamb():
        reverse = lambda s: s[::-1]
        print(reverse("hello"))
    # reverseStrLamb()

    def greetingLamb():
        greet = lambda name, greeting="Good Morning": f"{greeting}, {name}!"
        print(greet("Derek"))
    greetingLamb()



if __name__ == "__main__":
    main()