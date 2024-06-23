import reflex as rx


def customize_profile():
    return rx.badge(
        rx.hstack(
            rx.flex(
                rx.link(
                    rx.icon(
                        "flower",
                        size=25,
                    ),
                    href="/"
                ),
                rx.text(
                    "Skhumbuzo Bembe",
                ),
                direction="row",
                spacing="2"
            ),
            rx.flex(
                rx.text(
                    "Menu",
                ),
                rx.chakra.menu(
                    rx.chakra.menu_button(
                        rx.icon(
                            "text",
                        )
                    ),
                    rx.chakra.menu_list(
                        rx.chakra.menu_item(
                            rx.link(
                                "About me",
                                href="/about-me",
                            )
                        ),
                        rx.chakra.menu_divider(),
                        rx.chakra.menu_item(
                            rx.link(
                                "Projects",
                                href="/projects",
                            )
                        ),
                        rx.chakra.menu_divider(),
                        rx.chakra.menu_item(
                            "Resume"
                        )
                    )
                ),
                direction="row",
                spacing="2"
            ),
            width="100%",
            justify_content="space-between",
        ),
        size="3",
        color_scheme="gray",
        width="50%",
        height="3em",
        border_radius="10px",
    )


def contact(padding_: str):
    return rx.container(
        rx.hstack(
            rx.divider(margin="0px"),
            rx.link(
                rx.icon_button(
                    rx.icon(
                        tag="github",
                    ),
                    variant="soft",
                    size="3",
                ),
                href="https://github.com/MAVUNDL",
                is_external=True,
                button=True,
            ),
            rx.link(
                rx.icon_button(
                    rx.icon(
                        tag="linkedin",
                    ),
                    variant="soft",
                    size="3",
                ),
                href="https://www.linkedin.com/in/skhumbuzo-bembe-736602233",
                is_external=True,
                button=True,
            ),
            rx.link(
                rx.icon_button(
                    rx.icon(
                        tag="mail",
                    ),
                    variant="soft",
                    size="3",
                ),
                href="sikhumbuzobembe184@gmail.com",
                is_external=True,
                button=True,
            ),
            rx.divider(margin="0px"),
            width="100%",
            spacing="8",
            padding_top="60px"
        ),
        padding_top=padding_
    ),
