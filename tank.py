import random
import time
import wrap
rr=random.randint(50,550)
timepulfly=time.time()
timebonus=time.time()
star=False
gs=True
wrap.world.create_world(600, 600)

tank1=wrap.sprite.add("battle_city_tanks",200,100,"tank_enemy_size1_green1")
pul = wrap.sprite.add("battle_city_items", -30, rr, "bullet")

wrap.sprite.set_angle(pul,90)

wrap.sprite.set_size(pul,50,50)

wrap.sprite.add_text("0",550,50,text_color=[200,123,54],font_size=50)
@wrap.on_key_always(wrap.K_LEFT,wrap.K_RIGHT)
def angle(keys):
    a = wrap.sprite.get_angle(tank1)
    number= -10 if wrap.K_LEFT in keys else 10
    wrap.sprite.set_angle(tank1,a+number)

@wrap.on_key_always(wrap.K_UP,wrap.K_DOWN,delay=20)
def move(keys):
    a=wrap.sprite.get_angle(tank1)
    number= 3 if wrap.K_UP in keys else -3
    wrap.sprite.move_at_angle(tank1, a, number)

@wrap.always()
def pulfly():
    global timepulfly,rr
    wrap.sprite.move_at_angle_point(pul,700,rr,25)
    x=wrap.sprite.get_x(pul)
    print(x)

    if x>=700 and time.time() - timepulfly >= 5:
        timepulfly=time.time()
        rr=random.randint(50,550)
        wrap.sprite.move_to(pul,-30,rr)
@wrap.always()
def bonus():
    global timebonus, star,gs

    if time.time() - timebonus >= 2 and star==False:
        gs=wrap.sprite.add("battle_city_items",random.randint(50,550),random.randint(50,550),"block_gift_star")
        timebonus=time.time()
        star=True
    if time.time() - timebonus>=4 and star==True:
        wrap.sprite.remove(gs)
        star=False
        timebonus=time.time()

@wrap.always()
def bonuscontrol():


