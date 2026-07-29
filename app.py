#מספר רנדומלי
# מילון של שחקנים ומספר הניצחונות שלהם
# נתיב שמקבל מספר מהפרונט
# בדיקה האם תקין
# מילון עם שם השחקן ומספר הנסיונות בלוג
#שליחה האם ניחוש נכון או לא  והודעה מתאימה כל פעם
# טיפול במקרה שהשחקן כתב אותיות או סימנים
from flask import Flask
from random import randint


app = Flask(__name__, template_folder='.')

player_dict = {}
player_wins = {}


target = randint(1,100)


def post_massag(massag):
    return massag
def choice_num():
    return target

def check_num(num):
    if num == choice_num():
        return True
    if num != choice_num():
        return False

def check_only_num(num):
    return num.isdigit() and int(num) > 0


@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.route("/game/<name>/<num>")
def play(name,num):
    global target

    if not check_only_num(num):
        return post_massag("sorry only num")

    num_int = int(num)

    if name not in player_dict:
        player_dict[name] = []
    player_dict[name].append(num_int)

    if num_int == choice_num():
        player_wins[name] = player_wins.get(name, 0) + 1
        msg = f"win! congratulations {name}, you guessed the number!"
        target = randint(1, 100)
    elif num_int < choice_num():
        msg = "המספר קטן מדי נסה גדול יותר"
    else:
        msg = "המספר גדול מדי נסה קטן יותר"


    return f"{msg}"





if __name__ == "__main__":
    app.run(debug=True)






