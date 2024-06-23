import reflex as rx
from Reflex_portfolio.sharedComponents import customize_profile,contact


class AboutMePage:
    def __init__(self):
        self.MenuBar = customize_profile()
        self.introduction = None
        self.education = None
        self.skills = None
        self.experience = None

    @staticmethod
    def topic(text: str):
        return rx.heading(
            text,
            size="9",
            style={
                "background": "radial-gradient(circle at 10% 20%, rgb(126, 70, 195) 0%, rgb(156, 236, 247) 90%)",
                "-webkit-background-clip": "text",
                "color": "transparent"
            },
            padding_left="300px",
            padding_top="40px"
        )

    def Introduction(self) -> rx.Component:
        return rx.container(
            self.topic("About Me"),
            rx.text(
                "I am an aspiring software developer with a deep passion for programming. As a third-year Mathematical Science student specializing in Mathematics and Computer Science (Extended) at the University of Johannesburg, I am driven by the transformative power of technology and the endless possibilities it offers.",
                as_="p",
                justify="center",
                padding_top="25px"

            ),
            self.topic("Education"),
            rx.text(
                "I am currently pursuing a BSc in Mathematical Science, focusing on Mathematics and Computer Science. My academic journey has equipped me with a strong foundation in both theoretical and practical aspects of these fields.",
                as_="p",
                justify="center",
                padding_top="25px"
            ),
            self.topic("Skills"),
            rx.text(
                " I am proficient in several programming languages, including C++, Java, and Python. My expertise extends to procedural and object-oriented programming, with ongoing efforts to deepen my knowledge in Java and Python's object-oriented paradigms. Additionally, I have the following skills:",
                as_="p",
                justify="center",
                padding_top="25px"
            ),
            rx.blockquote(
                rx.text.strong("C++:"),
                " Strong foundation in both procedural and object-oriented programming.",
                margin_top="20px",
            ),
            rx.blockquote(
                rx.text.strong("Java:"),
                " Proficient in object-oriented design, design patterns, and advanced file handling",
                margin_top="20px",
            ),
            rx.blockquote(
                rx.text.strong("Java GUI:"),
                " Proficient in JavaFX for creating graphical user interfaces.",
                margin_top="20px",
            ),
            rx.blockquote(
                rx.text.strong("Python Frameworks:"),
                " Familiar with Python frameworks such as Reflex (also known as Pynecone) for web applications and Flet for desktop and mobile applications.",
                margin_top="20px",
            ),
            rx.blockquote(
                rx.text.strong("GUI Development:"),
                " Experienced with Python libraries such as customtkinter, tkinter, and ttkbootstrap.",
                margin_top="20px",
            ),
            self.topic("Knowledge"),
            rx.text(
                "My studies have provided me with a comprehensive understanding of various mathematical disciplines, including Differential and Integral Calculus, Applied Mathematics (Mechanics and Statics), and Statistics. I have experience in both descriptive and inferential statistics and am currently advancing my skills in Data Analysis using R.",
                as_="p",
                justify="center",
                padding_top="25px"
            ),
            self.topic("Collaboration"),
            rx.text(
                "I thrive in collaborative environments and am dedicated to continuous learning and problem-solving. I am eager to leverage technology to innovate and drive positive change. I am open to internships, research collaborations, and projects in mathematics, computer science, and data analysis.",
                as_="p",
                justify="center",
                padding_top="25px"
            ),
            self.topic("Contact"),
            contact("10px"),
            width="100%",
            justify_content="center",
            padding_left="50px",
            padding_top="20px"
        )

    def Main_page(self):
        return rx.box(
            rx.vstack(
                rx.center(
                    self.MenuBar,
                    width="100%",
                    padding_top="80px"
                ),
                self.Introduction(),
                width="100%",
            ),
            background="url('/6929472_3451499.jpg')",
            width="100%",
            height="100em",
        )
