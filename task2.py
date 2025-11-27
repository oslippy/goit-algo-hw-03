import turtle


def koch_segment(length: float, level: int) -> None:
    if level == 0:
        turtle.forward(length)
        return
    length /= 3
    koch_segment(length, level - 1)
    turtle.left(60)
    koch_segment(length, level - 1)
    turtle.right(120)
    koch_segment(length, level - 1)
    turtle.left(60)
    koch_segment(length, level - 1)


def koch_snowflake(length: float, level: int) -> None:
    for _ in range(level):
        koch_segment(length, level)
        turtle.right(120)


def main() -> None:
    turtle.setup(width=800, height=800)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-250, 150)
    turtle.pendown()

    koch_snowflake(500, 3)

    turtle.done()


if __name__ == "__main__":
    main()
