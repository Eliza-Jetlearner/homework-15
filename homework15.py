import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

light = Actor('light', center = (randint(50,350),randint(50,350)))
robot = Actor('robot', center = (200,200))

def draw():
    screen.clear()
    light.draw()
    robot.draw()

def next_robot_target():
    x = light.x
    y = light.y
    robot.target = x,y

    target_angle = robot.angle_to(robot.target)
    target_angle += 360 * ((robot.angle - target_angle + 180) // 360)

    animate(
        robot,
        angle=target_angle,
        duration=0.3,
        on_finished=move_robot,
    )

def move_robot():
    anim = animate(
        robot,
        tween='accel_decel',
        pos=robot.target,
        duration=robot.distance_to(robot.target)/200,
        on_finished=move_light,
    )

def move_light():
    light.x = randint(50,350)
    light.y = randint(50,350)
    next_robot_target()

next_robot_target()
pgzrun.go()