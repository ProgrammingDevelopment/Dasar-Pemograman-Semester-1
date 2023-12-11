class StudentIntroduction:
    def __init__(self, name, university, major, year):
        self.name = name
        self.university = university
        self.major = major
        self.year = year

    def display_introduction(self):
        print("============================================================")
        print("           Introduction-My Self-As-Student-Undergraduate")
        print("=============================================================")
        print(f"Name: {self.name}")
        print(f"University: {self.university}")
        print(f"Major: {self.major}")
        print(f"Year: {self.year}")
        print("\n")
        print("Hello, everyone! I am a computer science undergraduate student, and I would like to share a bit about myself.")
        print("I am passionate about technology, coding, and problem-solving. My academic journey and explore on role Science and environment Technology.")
        print("aspects of computer science, and I am eager to learn and contribute to the world of technology.")
        print("Feel free to connect with me and explore the exciting world of computer science together!")
        print("\n")
        print("Thank You For your Interseted")
        print("===================================")

if __name__ == "__main__":
    # Replace the placeholders with your actual information
    student_name = "My name is Swandaru tirta sandhika"
    university_name = "bina sarana informatics university"
    major = "Computer Science at department Informatics"
    current_year = "junior degree / entry-Level"

    # Create an instance of the introduction
    student_intro = StudentIntroduction(student_name, university_name, major, current_year)

    # Display the introduction
    student_intro.display_introduction()
