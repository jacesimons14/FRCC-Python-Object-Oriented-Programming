"""
File student.py
Manages a student's name and test scores
"""


class Student:
    """Represents a student."""

    def __init__(self, name, number):
        """Constructor creates a Student with the given name
        and number of scores and sets all scores to 0."""
        self.__name = name
        self.__scores = []
        for count in range(number):
            self.__scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.__name

    def setScore(self, i, score):
        """Resets the nth score, counting from 1"""
        self.__scores[i-1] = score

    def getScore(self, i):
        """Returns the nth score, counting from 1"""
        return self.__scores[i-1]

    def getAverage(self):
        """Returns the average score"""
        return sum(self.__scores)/len(self.__scores)

    def getHighScore(self):
        """Returns the highest score"""
        return max(self.__scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.__name + "\nScores: " + " ".join(map(str, self.__scores))

    # ~ Jace's code ~

    def __lt__(self, student):
        """Returns the result of a less than operation on the provided student with itself"""
        return self.__name < student.__name

    def __le__(self, student):
        return self.__name <= student.__name

    def __gt__(self, student):
        return self.__name > student.__name

    def __ge__(self, student):
        return self.__name >= student.__name

    def __eq__(self, student):
        return self.__name == student.__name
