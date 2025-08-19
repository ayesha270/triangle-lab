
from triangle import Triangle  # your class is in triangle.py

def main():
    t1 = Triangle()
    print(t1)  # Triangle(1.0, 1.0, 1.0) - equilateral by default

    t2 = Triangle(5)
    print(t2)  # Triangle(5, 5, 5) - equilateral with side 5

    t3 = Triangle(3, 4)
    print(t3)  # Triangle(3, 3, 4) - isosceles

    t4 = Triangle(3, 4, 5)
    print(t4, "RightAngled:", t4.isRightAngled())  # Triangle(3, 4, 5) RightAngled: True

    t5 = Triangle(t4)  # clone
    print("Cloned:", t5)

    print("Total Triangle objects created:", Triangle.objectcount())

if __name__ == "__main__":
    main()
