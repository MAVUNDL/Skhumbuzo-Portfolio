import reflex as rx
from Reflex_portfolio.sharedComponents import customize_profile, contact


class Projects:
    def __init__(self):
        self.navigation = customize_profile()

    @staticmethod
    def projects_view():
        return rx.flex(
            rx.box(
                rx.heading(
                    "Smart to do App UI",
                    align="center",
                    padding_bottom="20px",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src='/Screenshot (112).png',
                            width={"base": "100%", "md": "48%"},
                            margin_bottom={"base": "20px", "md": "0"},
                        ),
                        rx.image(
                            src='/Screenshot (113).png',
                            width={"base": "100%", "md": "48%"},
                        ),
                        spacing="6",
                        width="100%",
                        height="auto",
                        justify="center",
                        align="center",
                        wrap="wrap",
                    ),
                    rx.center(
                        rx.text(
                            "The Smart To-Do Application is designed for efficient task management, built using the Flet framework. Key features include task creation with customizable categories, SQLite database integration for persistent storage, responsive UI, category management, task completion tracking, and smooth animations.",
                           width="59%",
                        ),
                    ),
                    rx.link(
                        "click here to view the project details",
                        href="https://github.com/MAVUNDL/Smart-to-do-UI.git"
                    ),
                    width="100%",
                    height="auto",
                    justify="center",
                    align="center",
                    wrap="wrap",
                ),
                size="5",
                width={"base": "90%", "md": "35em"},
                height="auto",
                margin="auto",
                justify_content="center",
                align_content="center",
                padding_top="50px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading(
                        "SpaceShip-and-UFO Game",
                        align="center",
                        padding_bottom="20px",
                        padding_right="70px"
                    ),
                    rx.image(
                        src='/Screenshot (19).png',
                        height="100%",
                        width="50%",
                    ),
                    rx.text(
                        "This is a simple game created using the Pygame library in Python. The game involves a player controlling a character to shoot down moving enemies while avoiding collisions and staying within the game boundaries.",
                        as_="p",
                        justify="center",
                        width="59%",
                    ),
                    rx.link(
                        "click here to view the project details",
                        href="https://github.com/MAVUNDL/SpaceShip-and-UFO.git"
                    ),
                    justify="center",
                    align="center",
                ),
                size="5",
                width={"base": "90%", "md": "35em"},
                height="auto",
                margin="auto",
                justify_content="center",
                align_content="center",
                padding_top="100px",
                padding_bottom="70px",
            ),
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Python GUI Application",
                        align="center",
                        padding_bottom="20px",
                        padding_right="70px"
                    ),
                    rx.image(
                        src='/Screenshot (14).png',
                        height="100%",
                        width="50%",
                    ),
                    rx.text(
                        "This application is a GUI (Graphical User Interface) built with Python. It uses the customtkinter library to create a user-friendly interface for user authentication (login and sign-up).",
                        as_="p",
                        justify="center",
                        width="59%",
                    ),
                    rx.link(
                        "click here to view the project details",
                        href="https://github.com/MAVUNDL/Basic_login_system.git"
                    ),
                    justify="center",
                    align="center",
                ),
                size="5",
                width={"base": "90%", "md": "35em"},
                height="auto",
                margin="auto",
                justify_content="center",
                align_content="center",
                padding_top="100px",
                padding_bottom="70px",
            ),
            rx.box(
                rx.link(
                    rx.heading(
                        "Visit my GitHub Profile for more Projects",
                        style={
                            "background": "radial-gradient(circle at 10% 20%, rgb(126, 70, 195) 0%, rgb(156, 236, 247) 90%)",
                            "-webkit-background-clip": "text",
                            "color": "transparent"
                        },
                        size="9",
                        justify="center",
                        align="center",
                    ),
                    href="https://github.com/MAVUNDL"
                ),
                size="5",
                width={"base": "90%", "md": "35em"},
                height="auto",
                margin="auto",
                justify_content="center",
                align_content="center",
                padding_top="50px",
                padding_bottom="100px",
            ),
            direction="column",
            width="100%",
            spacing="9",
            padding_top="100px",
            justify="center",
            align="center",
        )

    def main_container(self):
        return rx.box(
            rx.vstack(
                rx.center(
                    self.navigation,
                    width="100%",
                    padding_top="80px"
                ),
                self.projects_view(),
                width="100%",
            ),
            overflow="auto",
            background="url('/6929472_3451499.jpg')  no-repeat center center fixed",
            background_size="cover",
            width="100vw",
            height="100vh",
            position="fixed",
            top="0",
            left="0",
            z_index="-1",
        )
