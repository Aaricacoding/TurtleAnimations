from turtle import *

running = True

def stop():
    global running
    running = False

def main():
    global running
    clearscreen()
    bgcolor("gray30")
    tracer(False)
    shape("triangle")
    f = 0.793402
    phi = 9.064678
    s = 5
    c = 1

    # creating compound shape
    sh = Shape("compound")
    for i in range(10):
        shapesize(s)
        p = get_shapepoly()
        s *= f
        c *= f
        tilt(-phi)
        sh.addcomponent(p, "white", "black")

    register_shape("dancer", sh)
    shape("dancer")
    pu()

    running = True

    def dance():
        if running:
            fd(c)
            lt(phi)
            update()
            ontimer(dance, 10)

    onkey(stop, "q")
    listen()
    dance()
    done()

if __name__ == "__main__":
    main()
