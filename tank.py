import random
import time
import wrap
rr=random.randint(50,550)
timepulfly=time.time()
timebonus=time.time()
star=False
gs=True
a=0
b=0
cost=True
wrap.world.create_world(600, 600)

tank1=wrap.sprite.add("battle_city_tanks",200,100,"tank_player_size1_green1")
pul = wrap.sprite.add("battle_city_items", -30, rr, "bullet")

wrap.sprite.set_angle(pul,90)

wrap.sprite.set_size(pul,50,50)

text=wrap.sprite.add_text(str(a),550,50,text_color=[200,123,54],font_size=50)
text2=wrap.sprite.add_text(str(b),575,50,text_color=[100,250,54],font_size=50)
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

    if x>=700 and time.time() - timepulfly >= 5:
        timepulfly=time.time()
        rr=random.randint(50,550)
        wrap.sprite.move_to(pul,-30,rr)
        wrap.sprite.show(pul)
@wrap.always()
def bonus():
    global timebonus, star,gs,a,cost

    if time.time() - timebonus >= 2 and star==False:
        cost=random.choice(["block_gift_star","block_gift_tank"])
        gs=wrap.sprite.add("battle_city_items",random.randint(50,550),random.randint(50,550),cost)
        timebonus=time.time()
        star=True
    if (time.time() - timebonus>=10 and star==True) or\
            (wrap.sprite.is_collide_sprite(tank1,gs) and star==True):
        wrap.sprite.hide(gs)
        star=False
        timebonus=time.time()
        if cost=="block_gift_star" and wrap.sprite.is_collide_sprite(tank1,gs):
            costume()
        if cost=="block_gift_tank" and wrap.sprite.is_collide_sprite(tank1,gs):
            life()

def costume():
    global a
    if a<3:
        a = a+1
        wrap.sprite.set_costume(tank1,"tank_player_size"+str(a+1)+"_green1")
        wrap.sprite_text.set_text(text, str(a))

def life():
    global b
    b=b+1
    wrap.sprite_text.set_text(text2, str(b))

@wrap.always()
def shot():
    global a, b, pul
    if not wrap.sprite.is_collide_sprite(tank1,pul) or not wrap.sprite.is_visible(pul):
        return
    if a>0:
        a=a-1
        wrap.sprite_text.set_text(text, str(a))
        wrap.sprite.set_costume(tank1, "tank_player_size" + str(a + 1) + "_green1")

    elif a==0 and b>0:
        b = b - 1
        wrap.sprite_text.set_text(text2, str(b))

    wrap.sprite.hide(pul)






