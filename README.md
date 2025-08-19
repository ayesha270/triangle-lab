

# Triangle Class in Python

## Features

* **Constructor Overloading:**
  Supports creating triangles with different parameter combinations:

  * No parameters: equilateral triangle with side 1.0
  * One parameter: equilateral triangle with given side
  * Two parameters: isosceles triangle
  * Three parameters: general triangle
  * Clone constructor: create a copy of an existing triangle object

* **Right-Angled Check:**
  `isRightAngled()` method determines if the triangle satisfies the Pythagorean theorem.

* **Object Counting:**
  Static method `objectcount()` returns the total number of `Triangle` instances created.

* **String Representation:**
  Custom `__str__()` method for readable printing of triangle side lengths.

---

## Notes

* The class assumes valid positive side lengths but does not currently validate if sides can form a valid triangle.
* `isRightAngled()` uses a tolerance for floating-point comparison.
* Properties with getters and setters ensure side lengths remain positive.
* Designed primarily as an educational example demonstrating OOP concepts like constructor overloading, cloning, static methods, and encapsulation.

---

If you want me to add or adjust anything else, just say!
