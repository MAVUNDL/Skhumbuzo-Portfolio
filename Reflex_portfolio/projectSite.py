import reflex as rx
from Reflex_portfolio.sharedComponents import customize_profile, contact


class Projects:
    def __init__(self):
        self.navigation = customize_profile()

    @staticmethod
    def projects_view():
        return rx.flex(
            rx.card(
                size="5",
                width="35em",
                height="35em",
            ),
            rx.card(
                size="5",
                width="35em",
                height="35em",
            ),
            direction="row",
            width="100%",
            spacing="9",
            padding_top="100px",
            justify="center",
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
            background="url('/6929472_3451499.jpg')",
            width="100%",
            height="100em",
        )
