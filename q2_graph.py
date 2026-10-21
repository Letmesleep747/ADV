from operator import indexOf
import os

# Simple function to clear the previous history in terminal after a function
def pause():
    input("\nPress enter to return...")
    os.system("cls" if os.name == 'nt' else 'clear')

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self, vertex):
        # Add a new vertex function
        if vertex not in self.adjacency_list: # to check if the vertex exists
            self.adjacency_list[vertex] = []

    def addEdge(self, source, destination):
        # Create a new edge one vertex with another
        if source not in self.adjacency_list: # to check if both vertex exists
            print("Source vertex does not exist.")
            return

        if destination not in self.adjacency_list: # to check if both vertex exists
            print("Destination vertex does not exist.")
            return

        # Avoid duplicate edges
        if destination not in self.adjacency_list[source]:
            self.adjacency_list[source].append(destination)

    def listIncomingAdjacentVertex(self, vertex):
        # Find all vertices that have an edge pointing to this vertex
        incoming = []

        # vertex doesn't exists
        if vertex not in self.adjacency_list:
            return incoming

        # vertices that have an edge pointing to this vertex
        for source in self.adjacency_list:
            if vertex in self.adjacency_list[source]:
                incoming.append(source)

        return incoming

    def listOutgoingAdjacentVertex(self, vertex):
        # Return all vertices that are reachable from this vertex
        if vertex not in self.adjacency_list:
            return []

        return self.adjacency_list[vertex]


class Course:
    # Course object, represents a single course

    # Constructor
    def __init__(self, courseCode, courseName, creditHours, level):
        self.courseCode = courseCode
        self.courseName = courseName
        self.creditHours = creditHours
        self.level = level

    def displayDetails(self):
        print(f"Course Code: {self.courseCode}")
        print(f"Course Name: {self.courseName}")
        print(f"Credit Hours: {self.creditHours}")
        print(f"Level: {self.level}")


def main():
    # Create five Course objects

    # Dictionary Data Type to store the courses information
    courses = {
        "CS101": Course("CS101", "Introduction to Programming", 3, "Core"),
        "CS201": Course("CS201", "Data Structures", 3, "Core"),
        "CS301": Course("CS301", "Algorithms", 3, "Core"),
        "CS302": Course("CS302", "Database Systems", 3, "Core"),
        "CS401": Course("CS401", "Software Engineering", 4, "Elective")
    }

    # Create a course graph object
    courseGraph = Graph()

    for code in courses: # add the courses into the graph
        courseGraph.addVertex(code)

    # Source (left) = prerequisite, destination (right) = course requiring it
    courseGraph.addEdge("CS101", "CS201")
    courseGraph.addEdge("CS101", "CS302")
    courseGraph.addEdge("CS201", "CS301")
    courseGraph.addEdge("CS201", "CS401")
    courseGraph.addEdge("CS302", "CS401")
    courseGraph.addEdge("CS301", "CS401")

    # Main Program Loop
    while True:
        print("\n!-!-!- X University Course Prerequisite System -!-!-!")
        print("1. View All Courses")
        print("2. View Course Details")
        print("3. View Prerequisites of a Course")
        print("4. View Courses Unlocked by a Course")
        print("5. Add a New Course")
        print("6. Exit")

        choice = input("Enter choice: ")

        # List all the courses names and codes
        if choice == "1":
            print("\nAvailable Courses:")

            for course in courses.values():
                print(f"{course.courseCode} --> {course.courseName}")

            pause()

        # View the details of a course
        elif choice == "2":
            code = input("Enter course code: ").strip().upper()

            if code in courses:
                print("\nCourse Details:")
                courses[code].displayDetails()
            else:
                print("Course not found.")

            pause()

        # View the list of prerequisites for a course
        elif choice == "3":
            code = input("Enter course code: ").strip().upper()

            if code not in courses:
                print("Course not found.")
                continue

            prerequisites = courseGraph.listIncomingAdjacentVertex(code)

            print(f"\nPrerequisites for {courses[code].courseName}:")

            if prerequisites:
                for prerequisite in prerequisites:
                    print(
                        f"- {courses[prerequisite].courseCode} "
                        f"({courses[prerequisite].courseName})"
                    )
            else:
                print("No prerequisites.")

            pause()

        # View the list of courses unlocked by a course
        elif choice == "4":
            code = input("Enter course code: ").strip().upper()

            if code not in courses:
                print("Course not found.")
                continue

            unlocked = courseGraph.listOutgoingAdjacentVertex(code)

            print(f"\nCourses unlocked by {courses[code].courseName}:")

            if unlocked:
                for next_code in unlocked:
                    print(
                        f"- {courses[next_code].courseCode} "
                        f"({courses[next_code].courseName})"
                    )
            else:
                print("This course does not unlock any other courses.")

            pause()

        # Add a new course
        elif choice == "5":

            inputCode = input("Enter course code: ").strip().upper()
            
            if inputCode in courses:
                print("Course already exists.")
                pause()
                continue

            inputName = input("Enter course name: ").strip()

            try:
                inputCreditHours = int(input("Enter course credit hours: "))
                if inputCreditHours < 1:
                    print("Invalid credit hours, must be at least 1.")
                    continue

            except ValueError:
                print("Invalid credit hours, must be a number.")
                continue

            inputLevel = input("Enter course level (CORE/ELECTIVE): ").strip().upper()
            if inputLevel != "CORE" and inputLevel != "ELECTIVE":
                print("Invalid level. Please enter CORE or ELECTIVE.")
                continue

            # Add the new course into the dictionary
            courses[inputCode] = Course(inputCode, inputName, inputCreditHours, inputLevel)
            
            courseGraph.addVertex(inputCode) # add the new coourse into the graph

            print(f"The new course {inputCode} - {inputName} has been added successfully!")


        # Exit bye
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        # Invalid choice check
        else:
            print("Invalid choice. Please try again.")

# Main func
if __name__ == "__main__":
    main()
