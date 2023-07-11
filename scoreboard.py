from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("data.txt") as file:
    contents = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(contents)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.penup()
    #     self.goto(0,0)
    #     self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




