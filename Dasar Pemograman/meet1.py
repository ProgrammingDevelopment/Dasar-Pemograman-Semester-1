class StudentPortfolio:
    def __init__(self, name, role, linkedin, github, instagram):
        self.name = name
        self.role = role
        self.linkedin = linkedin
        self.github = github
        self.instagram = instagram

    def display_basic_info(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"LinkedIn: {self.linkedin}")
        print(f"GitHub: {self.github}")
        print(f"Instagram: {self.instagram}")
        print("\n")

    def display_hr_interest(self):
        print("### Metting 1, adopt by use python use technology on Bina sarana informatics University ###")
        print("As a computer science student, I have a keen interest in leveraging technology for Science Humanity and improvement skills.")
        print("I believe in creating innovative solutions to streamline HR processes and enhance employee experiences.")
        print("My programming skills, combined with an understanding of HR practices, make me well-equipped for this.")
        print("\n")

if __name__ == "__main__":
    # Build placeholder with actual information
    print("========================================================\n")
    student_name = "Swandaru tirta Sandhika"
    student_role = "Undergraduate in Computer Science Department Information Technology"
    linkedin_url = "www.linkedin.com/in/swandaru-tirta-sandhika"
    github_url =   "https://github.com/swandrax"
    instagram_url = "https://www.instagram.com/your-instagram"
    print("========================================================\n")

    # Create an instance of the portfolio
    student_portfolio = StudentPortfolio(student_name, student_role, linkedin_url, github_url, instagram_url)

    # Display basic information
    student_portfolio.display_basic_info()

    # Display creative design for HR interest
    student_portfolio.display_hr_interest()
