import turtle
import random

#  پنجره
win = turtle.Screen() # ساخت صحفه بازی
win.title("بازی مربع")
win.setup(width=600, height=600)
win.tracer(0)

#  لاکپشت
square = turtle.Turtle() # شی را میسازد
square.shape("turtle") # شکلش
square.color("red")
square.penup()

#  موانع
obstacles = []
for _ in range(3): # تعداد موانع
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("purple")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.goto(random.randint(-280, 280), random.randint(-280, 280)) # موقعیت موانع به صورت رندوم
    obstacles.append(obstacle) # میریزه تو لیست

# تنظیم امتیاز اولیه
score = 0

# تنظیم نمایش امتیاز
s_pen = turtle.Turtle()
s_pen.speed(0)
s_pen.color("black") # رنگ متن
s_pen.penup()
s_pen.hideturtle()
s_pen.goto(0, 260) # موقعیت متن
s_pen.write("امتیاز: {}".format(score), align="center", font=("Courier", 30, "normal"))# موقعیت و فونت متن

size = 1.0 # سایز لاکی

# تابع حرکت
def move():
    x = square.xcor() # موقعیت حرکت لاکپشت در لحظه
    y = square.ycor()

    global direction # در کدام جهت لاکپشت حرکت داشته باشد و مقدار شون رو در متغییر دایرکشن میریزه
    if direction == "up":
        square.sety(y + speed)
    elif direction == "down":
        square.sety(y - speed)
    elif direction == "left":
        square.setx(x - speed)
    elif direction == "right":
        square.setx(x + speed)

    # بررسی برخورد با دیوارهای صفحه
    if square.xcor() > 290 or square.xcor() < -290 or square.ycor() > 290 or square.ycor() < -290: # رد شدن لاکی از بالا و پاین و چپ و راست صحفه و این اندازه ها نسبت به کادر صحفه که گفتیم
        update_score(-5) # وقتی به دیوار میخوره 5 امتیاز کم میشه ینی 5تا 5تا
        if direction == "up": # وقتی از سمت بالا به دیوار برخورد کرد
            direction = "down" # برمیگرده پایین
        elif direction == "down":
            direction = "up"
        elif direction == "left":
            direction = "right"
        elif direction == "right":
            direction = "left"

    # بررسی برخورد با موانع
    for obstacle in obstacles:
        if square.distance(obstacle) < 20:
            obstacle.goto(random.randint(-280, 280), random.randint(-280, 280)) # ایجاد مانع جدید بعد از خوردن مانع قبلیش
            update_score(1)  # اضافه کردن امتیاز

    win.update() # صحفه رو ابدیت میکد

# تابع بروزرسانی امتیاز
def update_score(points):
    global size
    global score
    if score + points >= 0:# امتیاز قبل و با امتیاز بعدش جمع میکنهه اگر بزرگتر از 0 بود امتیاز ابدیت میشود
        score += points


    else:
        score = 0 # موقع برخورد به دیوار



    s_pen.clear() #  نوشته امتیاز را پاک
    s_pen.write("امتیاز: {}".format(score), align="center", font=("Courier", 24, "normal")) # ابدیت دوباره امتیاز

# تابع پایان بازی
def end():
    win.bye()  # بستن پنجره و پایان بازی


#  تعریف تابع‌های حرکت
def go_up():
    global direction
    direction = "up"

def go_down():
    global direction
    direction = "down"

def go_left():
    global direction
    direction = "left"

def go_right():
    global direction
    direction = "right"

#  اتصال توابع حرکت به کلیدهای صحفه کلید
win.listen() # منتظر کلید های صحفه کلید
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

speed = 0.2 # تایین سزعت حرکت لاکپشت
direction = "left" # هنگام شروع بازی لاکپشت اول به سمت چپ حرکت میکند



def rotate(): # چرخش لاک پشت
    if direction == "up": # وقتی دکمه بالا رو میزنیم سرش به جهت حرکتش باشه
        square.setheading(90)
    elif direction == "down":
        square.setheading(-90)
    elif direction == "left":
        square.setheading(180)
    elif direction == "right":
        square.setheading(0)

# حلقه اجرای بازی
while True: # حلقه اصلی بازی
    win.update() # آبدیت پنجره
    rotate()
    move() # تابع حرکت