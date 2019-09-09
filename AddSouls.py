# coding=utf-8
from SoulLib import Soul


def add_xy():
    Soul(1, '心眼', 'XY1-1', 'null', control_resistance=3, speed=2, critical_damage=11, health_percentage=8)

    Soul(2, '心眼', 'XY2-1', 'damage', damage_absolute=52, damage_percentage=8, critical_damage=7, control_chance=4)
    Soul(2, '心眼', 'XY2-2', 'damage', damage_absolute=49, damage_percentage=8, defence_absolute=5, critical_damage=7)
    Soul(2, '心眼', 'XY2-3', 'damage', control_resistance=7, critical_damage=18, health_percentage=3, health_absolute=112)
    Soul(2, '心眼', 'XY2-4', 'speed', damage_absolute=22, damage_percentage=5, speed=14, defence_absolute=5)
    Soul(2, '心眼', 'XY2-5', 'damage', damage_percentage=8, control_resistance=4, speed=3, health_percentage=11)

    Soul(3, '心眼', 'XY3-1', 'null', control_resistance=4, critical_damage=3, speed=10, critical_chance=9)
    Soul(3, '心眼', 'XY3-2', 'null', damage_absolute=25, control_resistance=3, speed=17, health_absolute=111)
    Soul(3, '心眼', 'XY3-3', 'null', damage_percentage=13, control_resistance=3, health_percentage=3, control_chance=4)

    Soul(4, '心眼', 'XY4-1', 'damage', control_resistance=8, critical_damage=10, control_chance=8, health_absolute=91)
    Soul(4, '心眼', 'XY4-2', 'damage', defence_percentage=3, speed=3, defence_absolute=4, critical_damage=15)
    Soul(4, '心眼', 'XY4-3', 'damage', damage_percentage=13, defence_absolute=4, control_chance=4, health_absolute=107)

    Soul(5, '心眼', 'XY5-1', 'null', control_resistance=7, speed=3, critical_damage=15, health_absolute=107)
    Soul(5, '心眼', 'XY5-2', 'null', damage_percentage=12, defence_percentage=3, critical_damage=7, health_absolute=100)
    Soul(5, '心眼', 'XY5-3', 'null', damage_absolute=24, critical_damage=4, critical_chance=9, control_resistance=13)
    Soul(5, '心眼', 'XY5-4', 'null', critical_damage=3, defence_percentage=3, critical_chance=6, control_resistance=15)
    Soul(5, '心眼', 'XY5-5', 'null', damage_absolute=50, damage_percentage=5, critical_damage=11, health_absolute=111)

    Soul(6, '心眼', 'XY6-1', 'critical_damage',
         damage_percentage=5, critical_damage=11, health_percentage=6, control_chance=4)
    Soul(6, '心眼', 'XY6-2', 'critical_chance',
         damage_absolute=25, control_resistance=11, defence_absolute=4, critical_damage=14)
    Soul(6, '心眼', 'XY6-3', 'damage', damage_absolute=49, control_resistance=3, speed=3, control_chance=14)


def add_mw():
    Soul(1, '鸣屋', 'MW1-1', 'null', critical_damage=4, defence_percentage=3, critical_chance=13, health_absolute=98)
    Soul(1, '鸣屋', 'MW1-2', 'null', defence_absolute=4, critical_damage=15, control_chance=7, health_absolute=93)
    Soul(1, '鸣屋', 'MW1-3', 'null', critical_damage=3, critical_chance=14, health_percentage=3, health_absolute=192)
    Soul(1, '鸣屋', 'MW1-4', 'null', damage_percentage=5, critical_damage=4, speed=11, critical_chance=3)

    Soul(2, '鸣屋', 'MW2-1', 'damage', defence_percentage=3, defence_absolute=4, critical_damage=18, health_absolute=207)
    Soul(2, '鸣屋', 'MW2-2', 'speed', damage_absolute=96, control_resistance=4, critical_chance=8, health_percentage=3)

    Soul(3, '鸣屋', 'MW3-1', 'null', damage_absolute=25, critical_damage=21, control_chance=3, health_absolute=97)
    Soul(3, '鸣屋', 'MW3-2', 'null', damage_percentage=3, control_resistance=11, speed=3, control_chance=14)
    Soul(3, '鸣屋', 'MW3-3', 'null', speed=8, defence_absolute=9, critical_chance=8, health_percentage=3)
    Soul(3, '鸣屋', 'MW3-4', 'null', control_resistance=18, defence_percentage=6, defence_absolute=4, critical_chance=3)

    Soul(4, '鸣屋', 'MW4-1', 'health', damage_percentage=3, speed=6, critical_chance=8, health_percentage=8)
    Soul(4, '鸣屋', 'MW4-2', 'damage', damage_absolute=89, defence_percentage=5, critical_chance=5, control_chance=4)

    Soul(5, '鸣屋', 'MW5-1', 'null', speed=16, defence_absolute=4, critical_damage=4, health_absolute=99)
    Soul(5, '鸣屋', 'MW5-2', 'null', damage_absolute=25, damage_percentage=11, critical_chance=8, control_resistance=4)
    Soul(5, '鸣屋', 'MW5-3', 'null', critical_damage=11, speed=3, defence_absolute=4, critical_chance=8)
    Soul(5, '鸣屋', 'MW5-4', 'null', damage_percentage=3, speed=3, health_percentage=3, control_chance=21)

    Soul(6, '鸣屋', 'MW6-1', 'critical_chance',
         damage_absolute=50, damage_percentage=11, defence_absolute=5, critical_chance=5)
    Soul(6, '鸣屋', 'MW6-2', 'defence', damage_absolute=26, damage_percentage=3, speed=3, control_chance=22)
    Soul(6, '鸣屋', 'MW6-3', 'critical_chance', damage_percentage=5, defence_percentage=5, speed=8, defence_absolute=9)
    Soul(6, '鸣屋', 'MW6-4', 'damage', damage_percentage=16, critical_damage=4, critical_chance=3, health_absolute=110)


def add_z():
    Soul(1, '狰', 'Z1-1', 'null', control_resistance=18, speed=2, health_percentage=6, control_chance=3)
    Soul(1, '狰', 'Z1-2', 'null', damage_absolute=25, defence_percentage=6, critical_damage=18, critical_chance=3)
    Soul(1, '狰', 'Z1-3', 'null', damage_percentage=3, critical_chance=10, health_percentage=2, health_absolute=308)

    Soul(2, '狰', 'Z2-1', 'damage', critical_damage=4, critical_chance=8, health_percentage=8, control_chance=7)
    Soul(2, '狰', 'Z2-2', 'speed', damage_percentage=3, critical_damage=14, critical_chance=5, health_absolute=219)
    Soul(2, '狰', 'Z2-3', 'damage', damage_absolute=26, defence_percentage=3, speed=5, critical_chance=13)
    Soul(2, '狰', 'Z2-4', 'damage', control_resistance=3, critical_damage=4, speed=16, critical_chance=3)
    Soul(2, '狰', 'Z2-5', 'damage', damage_absolute=23, critical_damage=10, critical_chance=5, health_absolute=294)

    Soul(3, '狰', 'Z3-1', 'null', damage_absolute=27, control_resistance=11, speed=8, critical_damage=7)
    Soul(3, '狰', 'Z3-2', 'null', defence_percentage=3, speed=11, critical_chance=3, control_chance=11)
    Soul(3, '狰', 'Z3-3', 'null', damage_percentage=3, defence_percentage=6, critical_chance=11, health_absolute=103)
    Soul(3, '狰', 'Z3-4', 'null', damage_absolute=21, critical_damage=3, critical_chance=11, health_percentage=2)

    Soul(4, '狰', 'Z4-1', 'health', damage_absolute=96, defence_percentage=3, critical_damage=11, critical_chance=3)
    Soul(4, '狰', 'Z4-2', 'damage', control_resistance=7, defence_absolute=9, critical_chance=11, control_chance=3)
    Soul(4, '狰', 'Z4-3', 'damage', damage_percentage=8, defence_absolute=9, critical_chance=8, health_percentage=2)
    Soul(4, '狰', 'Z4-4', 'control_resistance',
         control_resistance=4, critical_damage=18, health_percentage=2, health_absolute=215)
    Soul(4, '狰', 'Z4-5', 'health', critical_damage=7, defence_percentage=3, speed=11, critical_chance=2)
    Soul(4, '狰', 'Z4-6', 'damage', damage_percentage=3, control_resistance=4, health_percentage=5, control_chance=17)

    Soul(5, '狰', 'Z5-1', 'null', damage_percentage=5, defence_percentage=3, critical_damage=18, control_chance=3)
    Soul(5, '狰', 'Z5-2', 'null', defence_percentage=3, speed=3, critical_chance=14, health_absolute=215)
    Soul(5, '狰', 'Z5-3', 'null', damage_absolute=23, speed=6, critical_chance=11, control_chance=8)
    Soul(5, '狰', 'Z5-4', 'null', damage_absolute=45, control_resistance=15, critical_chance=3, health_absolute=97)
    Soul(5, '狰', 'Z5-5', 'null', damage_percentage=3, speed=10, health_percentage=3, control_chance=11)
    Soul(5, '狰', 'Z5-6', 'null', damage_absolute=46, control_resistance=4, defence_absolute=4, control_chance=18)


def add_lrd():
    Soul(1, '轮入道', 'LR1-1', 'null', control_resistance=3, defence_absolute=9, critical_chance=13, control_chance=3)
    Soul(1, '轮入道', 'LR1-2', 'null', damage_percentage=16, defence_absolute=5, critical_damage=3, health_absolute=96)
    Soul(1, '轮入道', 'LR1-3', 'null', control_resistance=7, defence_percentage=3, critical_chance=11, control_chance=3)

    Soul(2, '轮入道', 'LR2-1', 'speed', damage_absolute=25, defence_percentage=3, critical_damage=7, control_resistance=11)
    Soul(2, '轮入道', 'LR2-2', 'speed', damage_absolute=66, critical_damage=4, critical_chance=8, control_resistance=7)
    Soul(2, '轮入道', 'LR2-3', 'damage', damage_absolute=26, damage_percentage=11, control_chance=11, control_resistance=4)
    Soul(2, '轮入道', 'LR2-4', 'speed', speed=2, defence_absolute=5, health_percentage=8, control_chance=7)

    Soul(3, '轮入道', 'LR3-1', 'null', damage_absolute=25, speed=9, critical_chance=11, control_chance=3)
    Soul(3, '轮入道', 'LR3-2', 'null', damage_percentage=3, control_resistance=18, speed=2, critical_damage=3)
    Soul(3, '轮入道', 'LR3-3', 'null', damage_percentage=5, critical_damage=8, speed=8, critical_chance=3)
    Soul(3, '轮入道', 'LR3-4', 'null', damage_absolute=25, speed=14, health_percentage=3, control_chance=7)

    Soul(4, '轮入道', 'LR4-1', 'defence', defence_percentage=5, speed=13, defence_absolute=5, health_percentage=3)
    Soul(4, '轮入道', 'LR4-2', 'health', damage_absolute=23, speed=14, health_percentage=2, health_absolute=96)
    Soul(4, '轮入道', 'LR4-3', 'damage', control_resistance=3, speed=3, defence_absolute=14, health_percentage=8)

    Soul(5, '轮入道', 'LR5-1', 'null', damage_absolute=52, speed=11, critical_chance=5, health_percentage=3)
    Soul(5, '轮入道', 'LR5-2', 'null', damage_absolute=47, critical_damage=14, speed=5, critical_chance=3)
    Soul(5, '轮入道', 'LR5-3', 'null', damage_absolute=23, speed=14, defence_absolute=4, control_chance=3)

    Soul(6, '轮入道', 'LR6-1', 'health', control_resistance=4, speed=13, defence_absolute=5, control_chance=7)


def add_fy():
    Soul(1, '蝠翼', 'LR1-1', 'null', speed=10, defence_absolute=8, critical_chance=6, health_absolute=104)
    Soul(1, '蝠翼', 'LR1-2', 'null', critical_damage=7, defence_absolute=9, critical_chance=8, health_absolute=100)

    Soul(2, '蝠翼', 'LR2-1', 'speed', defence_percentage=3, speed=3, defence_absolute=18, control_chance=7)

    Soul(3, '蝠翼', 'LR3-1', 'null', critical_damage=15, defence_percentage=2, critical_chance=3, health_percentage=5)
    Soul(3, '蝠翼', 'LR3-2', 'null', control_resistance=4, speed=16, health_percentage=3, health_absolute=93)

    Soul(4, '蝠翼', 'LR4-1', 'damage', damage_absolute=22, speed=11, critical_damage=4, health_percentage=6)
    Soul(4, '蝠翼', 'LR4-2', 'damage', damage_percentage=3, defence_absolute=9, critical_chance=9, health_percentage=5)

    Soul(5, '蝠翼', 'LR5-1', 'null', damage_absolute=53, defence_absolute=4, critical_chance=11, health_absolute=202)

    Soul(6, '蝠翼', 'LR6-1', 'damage', damage_percentage=5, defence_percentage=3, speed=13, critical_chance=3)


def add_kg():
    Soul(1, '狂骨', 'KG1-1', 'null', damage_absolute=51, speed=3, critical_chance=14, health_percentage=3)

    Soul(2, '狂骨', 'KG2-1', 'damage', control_resistance=4, defence_percentage=3, speed=11, critical_chance=5)


def add_ps():
    Soul(1, "破势", 'PS1-1', 'null', damage_percentage=3, defence_percentage=2, critical_chance=13, health_percentage=2)
    Soul(1, "破势", 'PS1-2', 'null', control_resistance=7, speed=11, defence_absolute=5, critical_chance=5)
    Soul(1, "破势", 'PS1-3', 'null', damage_percentage=3, control_resistance=4, speed=3, critical_chance=16)
    Soul(1, "破势", 'PS1-4', 'null', control_resistance=3, speed=3, critical_chance=11, control_chance=11)

    Soul(2, "破势", 'PS2-1', 'health', damage_absolute=23, damage_percentage=3, critical_chance=14, control_resistance=3)
    Soul(2, "破势", 'PS2-2', 'speed', control_resistance=15, speed=5, defence_absolute=4, control_chance=4)
    Soul(2, "破势", 'PS2-3', 'speed', damage_percentage=3, defence_percentage=3, health_percentage=2, control_chance=15)
    Soul(2, "破势", 'PS2-4', 'speed', control_resistance=3, critical_chance=8, control_chance=4, health_absolute=213)
    Soul(2, "破势", 'PS2-5', 'damage', damage_absolute=22, damage_percentage=14, critical_chance=2, health_percentage=5)
    Soul(2, "破势", 'PS2-6', 'damage', critical_damage=3, defence_percentage=3, critical_chance=8, health_percentage=11)
    Soul(2, "破势", 'PS2-7', 'damage', control_resistance=3, critical_damage=14, control_chance=8, health_absolute=204)
    Soul(2, "破势", 'PS2-8', 'damage', critical_damage=4, speed=10, critical_chance=6, health_absolute=197)
    Soul(2, "破势", 'PS2-9', 'health', damage_percentage=3, speed=14, critical_chance=3, health_percentage=5)

    Soul(3, "破势", 'PS3-1', 'null', damage_percentage=11, defence_percentage=2, critical_damage=4, health_percentage=5)
    Soul(3, "破势", 'PS3-2', 'null', defence_absolute=9, critical_damage=14, health_percentage=3, control_chance=4)
    Soul(3, "破势", 'PS3-3', 'null', damage_percentage=6, critical_damage=4, critical_chance=11, control_resistance=4)
    Soul(3, "破势", 'PS3-4', 'null', damage_absolute=25, damage_percentage=5, critical_damage=7, control_resistance=15)
    Soul(3, "破势", 'PS3-5', 'null', damage_percentage=3, critical_damage=4, speed=14, critical_chance=3)
    Soul(3, "破势", 'PS3-6', 'null', critical_damage=7, speed=5, critical_chance=5, health_absolute=191)
    Soul(3, "破势", 'PS3-7', 'null', critical_damage=11, critical_chance=2, control_chance=15, health_absolute=100)

    Soul(4, "破势", 'PS4-1', 'damage', damage_percentage=6, defence_absolute=10, critical_chance=5, control_chance=7)
    Soul(4, "破势", 'PS4-2', 'damage', damage_percentage=5, defence_percentage=3, critical_chance=8, health_percentage=3)
    Soul(4, "破势", 'PS4-3', 'damage', control_resistance=3, critical_damage=22, defence_absolute=5, critical_chance=3)
    Soul(4, "破势", 'PS4-4', 'health', damage_absolute=27, speed=14, damage_percentage=5, health_absolute=112)
    Soul(4, "破势", 'PS4-5', 'health', critical_damage=4, defence_percentage=2, speed=8, critical_chance=10)
    Soul(4, "破势", 'PS4-6', 'health', critical_damage=11, critical_chance=2, control_chance=7, health_absolute=324)
    Soul(4, "破势", 'PS4-7', 'damage', control_resistance=3, defence_percentage=8, critical_chance=6, health_percentage=3)
    Soul(4, "破势", 'PS4-8', 'control_resistance',
         damage_absolute=47, damage_percentage=3, defence_absolute=9, critical_damage=14)
    Soul(4, "破势", 'PS4-9', 'damage', damage_percentage=3, defence_percentage=3, critical_damage=10, control_chance=10)

    Soul(5, "破势", 'PS5-1', 'null', damage_absolute=23, defence_percentage=5, damage_percentage=7, critical_chance=8)
    Soul(5, "破势", 'PS5-2', 'null', damage_absolute=100, critical_damage=4, critical_chance=5, control_resistance=3)
    Soul(5, "破势", 'PS5-3', 'null', damage_percentage=3, critical_damage=15, control_chance=7, health_absolute=195)
    Soul(5, "破势", 'PS5-4', 'null', damage_absolute=74, critical_damage=11, critical_chance=3, control_resistance=7)
    Soul(5, "破势", 'PS5-5', 'null', defence_percentage=3, speed=13, health_percentage=3, control_chance=3)
    Soul(5, "破势", 'PS5-6', 'null', damage_percentage=8, defence_percentage=3, speed=5, critical_chance=5)

    Soul(6, "破势", 'PS6-1', 'critical_damage',
         damage_absolute=23, damage_percentage=11, critical_damage=8, health_percentage=2)
    Soul(6, "破势", 'PS6-2', 'critical_damage', damage_absolute=22, damage_percentage=9, speed=11, health_percentage=2)
    Soul(6, "破势", 'PS6-3', 'critical_chance',
         defence_percentage=2, critical_chance=5, health_percentage=2, health_absolute=325)
    Soul(6, "破势", 'PS6-4', 'critical_chance',
         damage_percentage=3, critical_chance=10, health_percentage=3, control_chance=4)
    Soul(6, "破势", 'PS6-5', 'damage', damage_absolute=49, damage_percentage=3, critical_chance=11, health_percentage=3)
    Soul(6, "破势", 'PS6-6', 'critical_damage', damage_percentage=3, speed=3, defence_absolute=14, critical_chance=8)
    Soul(6, "破势", 'PS6-7', 'damage', damage_percentage=3, speed=3, defence_absolute=9, critical_chance=11)


def add_shn():
    Soul(1, "伤魂鸟", 'SH1-1', 'null', critical_damage=8, defence_absolute=9, critical_chance=5, health_absolute=212)
    Soul(2, "伤魂鸟", 'SH2-1', 'damage', defence_percentage=3, critical_damage=15, control_chance=11, health_absolute=100)
    Soul(6, "伤魂鸟", 'SH6-1', 'critical_chance', damage_absolute=25, damage_percentage=3, speed=6, critical_damage=10)
    Soul(6, "伤魂鸟", 'SH6-2', 'critical_damage', defence_percentage=3, speed=2, critical_chance=8, health_absolute=209)


def add_wq():
    Soul(1, "网切", 'WQ1-1', 'null', damage_percentage=8, speed=3, defence_absolute=9, critical_chance=8)
    Soul(2, "网切", 'WQ2-1', 'damage', critical_damage=4, defence_percentage=8, defence_absolute=4, critical_chance=6)
    Soul(2, "网切", 'WQ2-2', 'health', damage_absolute=51, critical_damage=11, critical_chance=9, health_absolute=96)
    Soul(4, "网切", 'WQ4-1', 'damage', critical_damage=7, defence_percentage=2, critical_chance=5, health_absolute=196)
    Soul(5, "网切", 'WQ5-1', 'null', damage_percentage=5, control_resistance=4, critical_chance=8, control_chance=11)
    Soul(5, "网切", 'WQ5-2', 'null', critical_damage=12, defence_absolute=5, critical_chance=6, health_absolute=319)
    Soul(6, "网切", 'WQ6-1', 'critical_damage', control_resistance=4, defence_percentage=3, speed=8, control_chance=11)


def add_sw():
    Soul(1, '三味', 'SW1-1', 'null', defence_percentage=3, speed=3, critical_damage=14, health_percentage=5)
    Soul(1, '三味', 'SW1-2', 'null', critical_damage=14, defence_percentage=8, critical_chance=3, control_resistance=4)
    Soul(1, '三味', 'SW1-3', 'null', damage_percentage=8, defence_percentage=3, critical_chance=8, control_resistance=3)
    Soul(1, '三味', 'SW1-4', 'null', control_resistance=11, defence_percentage=2, defence_absolute=4, critical_chance=8)

    Soul(2, '三味', 'SW2-1', 'speed', damage_percentage=5, control_resistance=3, speed=13, defence_absolute=5)
    Soul(2, '三味', 'SW2-2', 'speed', damage_absolute=25, control_resistance=12, defence_absolute=4, critical_damage=7)
    Soul(2, '三味', 'SW2-3', 'speed', speed=5, critical_chance=9, control_chance=4, health_absolute=99)
    Soul(2, '三味', 'SW2-4', 'damage', defence_percentage=6, speed=3, critical_damage=18, health_percentage=3)

    Soul(3, '三味', 'SW3-1', 'null', critical_damage=11, defence_percentage=3, defence_absolute=5, critical_chance=5)
    Soul(3, '三味', 'SW3-2', 'null', defence_absolute=9, critical_chance=11, control_chance=4, health_absolute=2017)
    Soul(3, '三味', 'SW3-3', 'null', damage_percentage=3, control_resistance=15, speed=3, critical_chance=8)
    Soul(3, '三味', 'SW3-4', 'null', damage_percentage=8, critical_damage=7, critical_chance=2, health_percentage=5)

    Soul(4, '三味', 'SW4-1', 'damage', control_resistance=22, critical_damage=4, health_percentage=3, health_absolute=102)
    Soul(4, '三味', 'SW4-2', 'damage', damage_percentage=14, defence_percentage=3, control_chance=3, health_absolute=105)
    Soul(4, '三味', 'SW4-3', 'health', damage_absolute=24, critical_damage=14, speed=8, critical_chance=3)
    Soul(4, '三味', 'SW4-4', 'damage', damage_percentage=5, critical_chance=11, control_chance=4, health_absolute=101)
    Soul(4, '三味', 'SW4-5', 'damage', control_resistance=7, speed=5, critical_chance=9, health_percentage=5)

    Soul(5, '三味', 'SW5-1', 'null', damage_absolute=50, critical_damage=3, critical_chance=13, health_absolute=93)
    Soul(5, '三味', 'SW5-2', 'null', damage_percentage=11, defence_percentage=3, defence_absolute=5, critical_chance=8)
    Soul(5, '三味', 'SW5-3', 'null', defence_percentage=3, speed=3, critical_chance=13, health_absolute=203)
    Soul(5, '三味', 'SW5-4', 'null', defence_percentage=2, speed=8, defence_absolute=5, critical_chance=8)

    Soul(6, '三味', 'SW6-1', 'critical_damage',
         control_resistance=4, critical_damage=11, control_chance=7, health_absolute=210)
    Soul(6, '三味', 'SW6-2', 'critical_damage', damage_absolute=22, control_resistance=7, speed=3, critical_chance=14)


def add_zn():
    Soul(1, '针女', 'ZN1-1', 'null', critical_damage=4, speed=6, defence_absolute=4, critical_chance=10)
    Soul(1, '针女', 'ZN1-2', 'null', damage_percentage=3, control_resistance=18, critical_damage=7, health_absolute=95)
    Soul(1, '针女', 'ZN1-3', 'null', damage_absolute=22, damage_percentage=10, speed=3, critical_chance=5)
    Soul(1, '针女', 'ZN1-4', 'null', damage_percentage=3, critical_damage=11, defence_absolute=5, critical_chance=5)
    Soul(1, '针女', 'ZN1-5', 'null', control_resistance=17, speed=3, health_percentage=3, control_chance=6)
    Soul(1, '针女', 'ZN1-6', 'null', damage_absolute=27, speed=5, control_chance=15, health_absolute=92)
    Soul(1, '针女', 'ZN1-7', 'null', control_resistance=7, speed=13, critical_chance=2, health_absolute=100)

    Soul(2, '针女', 'ZN2-1', 'damage', control_resistance=3, speed=17, critical_damage=3, health_percentage=3)
    Soul(2, '针女', 'ZN2-2', 'damage',
         damage_percentage=11, control_resistance=4, critical_chance=3, health_absolute=325)
    Soul(2, '针女', 'ZN2-3', 'damage', damage_absolute=48, critical_damage=14, critical_chance=3, health_absolute=192)
    Soul(2, '针女', 'ZN2-4', 'damage', speed=2, critical_damage=11, health_percentage=5, health_absolute=103)
    Soul(2, '针女', 'ZN2-5', 'damage', control_resistance=11, critical_damage=7, speed=5, critical_chance=5)
    Soul(2, '针女', 'ZN2-6', 'speed', speed=2, critical_chance=3, health_percentage=8, control_chance=11)
    Soul(2, '针女', 'ZN2-7', 'damage', damage_percentage=8, defence_absolute=5, critical_damage=7, health_percentage=6)
    Soul(2, '针女', 'ZN2-8', 'health', damage_percentage=3, critical_damage=7, critical_chance=11, control_resistance=7)
    Soul(2, '针女', 'ZN2-9', 'health', critical_damage=7, defence_percentage=3, speed=8, critical_chance=5)
    Soul(2, '针女', 'ZN2-10', 'damage', defence_percentage=5, speed=8, critical_chance=6, control_chance=3)

    Soul(3, '针女', 'ZN3-1', 'null', critical_damage=14, defence_percentage=5, critical_chance=2, control_resistance=4)
    Soul(3, '针女', 'ZN3-2', 'null', damage_percentage=3, control_resistance=10, defence_absolute=5, critical_chance=10)
    Soul(3, '针女', 'ZN3-3', 'null', damage_percentage=8, control_resistance=7, speed=3, critical_damage=11)
    Soul(3, '针女', 'ZN3-4', 'null', damage_percentage=5, control_resistance=7, defence_absolute=4, critical_chance=11)
    Soul(3, '针女', 'ZN3-5', 'null', damage_absolute=23, speed=8, critical_chance=8, health_percentage=6)
    Soul(3, '针女', 'ZN3-6', 'null', control_resistance=7, speed=3, defence_absolute=4, critical_damage=15)
    Soul(3, '针女', 'ZN3-7', 'null', damage_absolute=23, critical_damage=11, critical_chance=9, control_resistance=7)
    Soul(3, '针女', 'ZN3-8', 'null', damage_absolute=22, damage_percentage=3, control_chance=21, health_absolute=94)
    Soul(3, '针女', 'ZN3-9', 'null', critical_damage=18, defence_percentage=5, speed=3, critical_chance=3)
    Soul(3, '针女', 'ZN3-10', 'null', control_resistance=8, critical_damage=14, critical_chance=3, health_percentage=3)

    Soul(4, '针女', 'ZN4-1', 'damage', critical_damage=3, speed=8, critical_chance=3, health_percentage=8)
    Soul(4, '针女', 'ZN4-2', 'damage', speed=8, defence_absolute=4, critical_chance=11, control_chance=3)
    Soul(4, '针女', 'ZN4-3', 'damage', damage_absolute=51, damage_percentage=14, critical_damage=4, control_chance=3)
    Soul(4, '针女', 'ZN4-4', 'damage', damage_percentage=6, defence_absolute=4, critical_damage=11, health_percentage=3)
    Soul(4, '针女', 'ZN4-5', 'damage', damage_absolute=71, control_resistance=14, speed=2, critical_damage=3)
    Soul(4, '针女', 'ZN4-6', 'damage', critical_damage=7, critical_chance=3, control_chance=10, health_absolute=95)

    Soul(5, '针女', 'ZN5-1', 'null', damage_absolute=45, damage_percentage=3, critical_damage=4, critical_chance=13)
    Soul(5, '针女', 'ZN5-2', 'null', damage_absolute=26, damage_percentage=2, critical_chance=14, health_absolute=111)
    Soul(5, '针女', 'ZN5-3', 'null', damage_absolute=25, damage_percentage=3, critical_damage=14, control_resistance=7)
    Soul(5, '针女', 'ZN5-4', 'null', speed=11, critical_damage=11, health_percentage=3, health_absolute=113)
    Soul(5, '针女', 'ZN5-5', 'null', control_resistance=11, critical_damage=3, critical_chance=3, control_chance=15)
    Soul(5, '针女', 'ZN5-6', 'null', critical_damage=7, defence_percentage=9, speed=3, critical_chance=6)

    Soul(6, '针女', 'ZN6-1', 'critical_chance',
         damage_percentage=3, critical_damage=19, control_chance=4, health_absolute=101)
    Soul(6, '针女', 'ZN6-2', 'critical_chance', damage_absolute=50, speed=5, health_percentage=8, control_chance=8)
    Soul(6, '针女', 'ZN6-3', 'critical_chance',
         control_resistance=15, critical_damage=3, defence_absolute=4, critical_chance=2)
    Soul(6, '针女', 'ZN6-4', 'damage', damage_percentage=3, critical_damage=15, critical_chance=5, health_percentage=3)
    Soul(6, '针女', 'ZN6-5', 'critical_chance',
         control_resistance=14, critical_chance=3, health_percentage=8, control_chance=3)
    Soul(6, '针女', 'ZN6-6', 'critical_chance',
         damage_percentage=5, control_resistance=4, critical_chance=11, control_chance=7)
    Soul(6, '针女', 'ZN6-7', 'critical_chance',
         control_chance=11, critical_damage=11, health_percentage=5, health_absolute=105)
    Soul(6, '针女', 'ZN6-8', 'critical_chance',
         defence_percentage=5, defence_absolute=5, critical_chance=5, control_chance=7)


def add_sy():
    Soul(1, '树妖', 'SY1-1', 'null', speed=3, critical_chance=11, health_percentage=5, health_absolute=109)

    Soul(2, '树妖', 'SY2-1', 'speed', damage_absolute=73, critical_damage=3, speed=3, critical_chance=6)
    Soul(2, '树妖', 'SY2-2', 'speed', control_resistance=8, speed=11, defence_absolute=8, health_absolute=103)

    Soul(4, '树妖', 'SY4-1', 'control', control_resistance=7, critical_chance=3, control_chance=15, health_absolute=95)
    Soul(4, '树妖', 'SY4-2', 'damage', damage_absolute=22, critical_damage=18, critical_chance=5, control_chance=4)
    Soul(4, '树妖', 'SY4-3', 'control_resistance', damage_absolute=26, control_resistance=7, speed=8, critical_chance=6)

    Soul(5, '树妖', 'SY5-1', 'null', speed=11, critical_chance=5, health_percentage=3, health_absolute=192)

    Soul(6, '树妖', 'SY6-1', 'damage', defence_percentage=3, speed=17, defence_absolute=4, critical_damage=4)
    Soul(6, '树妖', 'SY6-1', 'defence', damage_absolute=24, damage_percentage=5, speed=14, health_absolute=92)


def add_th():
    Soul(1, '薙魂', 'TH1-1', 'null', control_resistance=11, defence_percentage=6, speed=5, control_chance=7)
    Soul(1, '薙魂', 'TH1-2', 'null', critical_damage=7, critical_chance=9, health_percentage=3, control_chance=7)
    Soul(1, '薙魂', 'TH1-3', 'null', damage_percentage=3, defence_percentage=3, speed=16, defence_absolute=5)
    Soul(1, '薙魂', 'TH1-4', 'null', critical_damage=18, speed=3, critical_chance=3, health_percentage=5)
    Soul(1, '薙魂', 'TH1-5', 'null', damage_absolute=52, control_resistance=4, critical_chance=14, health_percentage=3)

    Soul(2, '薙魂', 'TH2-1', 'speed', damage_percentage=3, speed=5, defence_absolute=4, critical_chance=9)
    Soul(2, '薙魂', 'TH2-2', 'speed', damage_absolute=26, damage_percentage=2, defence_absolute=14, critical_chance=11)

    Soul(3, '薙魂', 'TH3-1', 'null', critical_damage=18, defence_absolute=5, critical_chance=3, control_chance=4)
    Soul(3, '薙魂', 'TH3-2', 'null', control_resistance=4, speed=5, critical_chance=5, health_percentage=8)
    Soul(3, '薙魂', 'TH3-3', 'null', control_resistance=14, defence_percentage=6, defence_absolute=4, critical_damage=7)

    Soul(4, '薙魂', 'TH4-1', 'damage', speed=11, critical_chance=8, control_chance=3, health_absolute=92)
    Soul(4, '薙魂', 'TH4-2', 'control_resistance',
         damage_percentage=9, defence_percentage=5, defence_absolute=5, control_chance=7)
    Soul(4, '薙魂', 'TH4-3', 'damage', damage_absolute=46, control_resistance=8, speed=11, critical_chance=2)
    Soul(4, '薙魂', 'TH4-4', 'damage', control_resistance=7, critical_damage=8, critical_chance=8, control_chance=7)

    Soul(5, '薙魂', 'TH5-1', 'null', damage_absolute=76, critical_damage=10, speed=3, critical_chance=3)
    Soul(5, '薙魂', 'TH5-2', 'null', damage_absolute=23, speed=8, critical_damage=8, health_percentage=8)
    Soul(5, '薙魂', 'TH5-3', 'null', control_resistance=7, speed=11, critical_damage=8, control_chance=3)
    Soul(5, '薙魂', 'TH5-4', 'null', control_resistance=15, speed=5, critical_chance=3, health_absolute=107)

    Soul(6, '薙魂', 'TH6-1', 'critical_chance', damage_absolute=26, speed=6, critical_chance=3, health_percentage=8)
    Soul(6, '薙魂', 'TH6-2', 'health', damage_absolute=24, control_resistance=18, control_chance=7, health_absolute=97)
    Soul(6, '薙魂', 'TH6-3', 'health', damage_absolute=25, defence_percentage=3, speed=6, health_percentage=14)
    Soul(6, '薙魂', 'TH6-4', 'critical_chance',
         damage_absolute=22, control_resistance=11, defence_absolute=5, critical_chance=5)


def add_zl():
    Soul(1, '钟灵', 'ZL1-1', 'null', speed=5, critical_chance=5, control_chance=11, health_absolute=107)
    Soul(1, '钟灵', 'ZL1-2', 'null', damage_percentage=2, control_resistance=4, health_percentage=3, control_chance=17)
    Soul(1, '钟灵', 'ZL1-3', 'null', critical_damage=4, speed=5, critical_chance=11, health_absolute=199)
    Soul(1, '钟灵', 'ZL1-4', 'null', critical_damage=4, speed=8, critical_chance=6, control_chance=8)

    Soul(2, '钟灵', 'ZL2-1', 'speed', damage_absolute=49, defence_percentage=3, health_percentage=3, control_chance=18)
    Soul(2, '钟灵', 'ZL2-2', 'speed', defence_percentage=8, speed=3, defence_absolute=9, critical_chance=3)
    Soul(2, '钟灵', 'ZL2-3', 'health', damage_absolute=49, speed=8, defence_absolute=5, control_chance=11)

    Soul(3, '钟灵', 'ZL3-1', 'null', damage_percentage=6, speed=5, defence_absolute=5, control_chance=11)

    Soul(4, '钟灵', 'ZL4-1', 'health', speed=16, critical_damage=4, health_percentage=3, health_absolute=113)
    Soul(4, '钟灵', 'ZL4-2', 'damage', control_resistance=11, defence_absolute=9, health_percentage=3, control_chance=11)

    Soul(5, '钟灵', 'ZL5-1', 'null', control_resistance=8, defence_percentage=3, speed=13, health_absolute=94)
    Soul(5, '钟灵', 'ZL5-2', 'null', damage_percentage=5, control_resistance=4, health_percentage=3, control_chance=18)
    Soul(5, '钟灵', 'ZL5-3', 'null', control_resistance=18, defence_absolute=4, control_chance=7, health_absolute=101)
    Soul(5, '钟灵', 'ZL5-4', 'null', control_resistance=18, critical_chance=6, control_chance=4, health_absolute=102)

    Soul(6, '钟灵', 'ZL6-1', 'defence', damage_percentage=3, control_resistance=7, health_percentage=3, control_chance=15)


def add_jj():
    Soul(1, '镜姬', 'JJ1-1', 'null', critical_damage=8, defence_percentage=3, critical_chance=8, control_resistance=7)
    Soul(1, '镜姬', 'JJ1-2', 'null', speed=6, defence_absolute=5, critical_damage=17, health_percentage=3)
    Soul(1, '镜姬', 'JJ1-3', 'null', damage_percentage=11, speed=3, defence_absolute=8, critical_damage=4)
    Soul(1, '镜姬', 'JJ1-4', 'null', speed=11, defence_absolute=5, critical_chance=2, health_absolute=94)

    Soul(2, '镜姬', 'JJ2-1', 'health', control_resistance=15, critical_damage=3, defence_absolute=4, critical_chance=3)
    Soul(2, '镜姬', 'JJ2-2', 'speed', damage_absolute=48, control_resistance=11, speed=8, control_chance=4)
    Soul(2, '镜姬', 'JJ2-3', 'speed', control_resistance=10, critical_damage=4, health_percentage=8, health_absolute=104)

    Soul(3, '镜姬', 'JJ3-1', 'null', control_resistance=7, defence_absolute=4, critical_chance=5, control_chance=11)
    Soul(3, '镜姬', 'JJ3-2', 'null', damage_percentage=3, control_resistance=4, speed=6, critical_chance=13)
    Soul(3, '镜姬', 'JJ3-3', 'null', control_resistance=10, critical_damage=4, critical_chance=8, control_chance=8)

    Soul(4, '镜姬', 'JJ4-1', 'control_resistance', damage_absolute=24, speed=3, critical_chance=13, health_absolute=216)
    Soul(4, '镜姬', 'JJ4-2', 'health', control_resistance=14, defence_percentage=3, defence_absolute=9, critical_chance=3)

    Soul(5, '镜姬', 'JJ5-1', 'null', critical_damage=4, speed=9, critical_chance=8, control_chance=7)
    Soul(5, '镜姬', 'JJ5-2', 'null', control_resistance=3, defence_percentage=3, speed=11, critical_damage=12)


def add_bf():
    Soul(1, '被服', 'BF1-1', 'null', damage_percentage=3, speed=14, defence_absolute=10, critical_damage=3)
    Soul(3, '被服', 'BF3-1', 'null', damage_percentage=6, critical_damage=4, critical_chance=11, control_resistance=4)
    Soul(4, '被服', 'BF4-1', 'control', damage_absolute=48, defence_absolute=4, control_chance=11, health_absolute=309)
    Soul(5, '被服', 'BF5-1', 'null', control_resistance=7, speed=6, defence_absolute=4, control_chance=15)


def add_np():
    Soul(2, '涅槃之火', 'NP2-1', 'speed', control_resistance=3, defence_percentage=3, speed=3, health_absolute=398)
    Soul(2, '涅槃之火', 'NP2-2', 'speed', critical_damage=11, speed=10, defence_absolute=5, critical_chance=3)
    Soul(4, '涅槃之火', 'NP4-1', 'control', damage_absolute=24, control_resistance=11, speed=11, critical_chance=2)
    Soul(6, '涅槃之火', 'NP6-1', 'damage', damage_absolute=24, damage_percentage=3, speed=16, health_absolute=105)


def add_dz():
    Soul(1, '地藏像', 'DZ1-1', 'null', control_resistance=3, critical_damage=11, speed=7, critical_chance=6)
    Soul(1, '地藏像', 'DZ1-2', 'null', critical_damage=7, defence_absolute=4, critical_chance=12, control_chance=7)
    Soul(1, '地藏像', 'DZ1-3', 'null', control_resistance=7, critical_chance=11, health_percentage=6, control_chance=4)
    Soul(1, '地藏像', 'DZ1-4', 'null', damage_absolute=27, defence_percentage=3, speed=11, defence_absolute=14)

    Soul(2, '地藏像', 'DZ2-1', 'speed', damage_percentage=13, defence_percentage=3, control_chance=7, control_resistance=4)
    Soul(2, '地藏像', 'DZ2-2', 'speed', damage_absolute=24, damage_percentage=3, health_percentage=3, control_chance=17)

    Soul(3, '地藏像', 'DZ3-1', 'null', defence_percentage=16, control_resistance=4, critical_chance=3, control_chance=3)
    Soul(3, '地藏像', 'DZ3-2', 'null', damage_absolute=23, control_resistance=15, health_percentage=3, health_absolute=93)
    Soul(3, '地藏像', 'DZ3-3', 'null', damage_percentage=5, control_resistance=7, defence_absolute=5, critical_chance=11)

    Soul(4, '地藏像', 'DZ4-1', 'control_resistance',
         damage_absolute=46, damage_percentage=10, defence_absolute=5, control_chance=3)
    Soul(4, '地藏像', 'DZ4-2', 'defence', speed=13, critical_damage=3, health_percentage=5, health_absolute=103)
    Soul(4, '地藏像', 'DZ4-3', 'health',
         damage_percentage=3, defence_percentage=8, damage_absolute=5, control_resistance=14)
    Soul(4, '地藏像', 'DZ4-4', 'damage', damage_percentage=3, speed=3, critical_chance=14, control_chance=7)

    Soul(5, '地藏像', 'DZ5-1', 'null', damage_percentage=3, control_resistance=12, defence_absolute=5, control_chance=15)

    Soul(6, '地藏像', 'DZ6-1', 'critical_chance', speed=14, critical_damage=3, control_chance=4, health_absolute=108)


def add_mm():
    Soul(1, '木魅', 'MM1-1', 'null', control_resistance=4, speed=13, critical_damage=3, control_chance=7)
    Soul(1, '木魅', 'MM1-2', 'null', damage_absolute=77, defence_percentage=3, speed=8, control_resistance=7)

    Soul(2, '木魅', 'MM2-1', 'speed', damage_percentage=5, control_resistance=11, defence_absolute=10, control_chance=7)
    Soul(2, '木魅', 'MM2-2', 'speed', defence_percentage=5, speed=8, control_chance=3, health_absolute=99)

    Soul(3, '木魅', 'MM3-1', 'null', critical_damage=4, speed=16, defence_absolute=4, critical_chance=2)
    Soul(3, '木魅', 'MM3-2', 'null', damage_percentage=3, defence_percentage=3, control_chance=11, control_resistance=14)
    Soul(3, '木魅', 'MM3-3', 'null', control_resistance=4, defence_absolute=5, critical_chance=11, health_absolute=209)

    Soul(4, '木魅', 'MM4-1', 'control_resistance', damage_percentage=3, speed=3, critical_chance=14, control_chance=3)

    Soul(5, '木魅', 'MM5-1', 'null', damage_percentage=5, defence_percentage=8, critical_chance=8, control_resistance=4)
    Soul(5, '木魅', 'MM5-2', 'null', damage_percentage=3, control_resistance=7, control_chance=3, health_absolute=312)

    Soul(6, '木魅', 'MM6-1', 'critical_chance', damage_absolute=49, damage_percentage=3, speed=11, health_percentage=3)


def add_rn():
    Soul(1, '日女巳时', 'RN1-1', 'null', damage_absolute=24, defence_percentage=3, speed=16, critical_chance=3)
    Soul(1, '日女巳时', 'RN1-2', 'null', damage_absolute=26, critical_damage=4, speed=5, critical_chance=10)
    Soul(1, '日女巳时', 'RN1-3', 'null', critical_damage=3, health_percentage=2, critical_chance=17, control_resistance=3)

    Soul(2, '日女巳时', 'RN2-1', 'damage',
         damage_percentage=5, control_resistance=4, critical_chance=9, health_percentage=8)
    Soul(2, '日女巳时', 'RN2-2', 'speed', speed=3, defence_absolute=5, critical_damage=11, control_chance=8)

    Soul(3, '日女巳时', 'RN3-1', 'null', critical_damage=4, defence_absolute=4, critical_chance=11, health_percentage=8)
    Soul(3, '日女巳时', 'RN3-2', 'null', control_resistance=4, defence_percentage=3, speed=14, critical_chance=5)

    Soul(4, '日女巳时', 'RN4-1', 'damage', damage_percentage=3, control_resistance=7, critical_chance=11, control_chance=4)

    Soul(5, '日女巳时', 'RN5-1', 'null', damage_absolute=22, control_resistance=11, critical_chance=8, health_percentage=5)
    Soul(5, '日女巳时', 'RN5-2', 'null', damage_percentage=3, critical_damage=15, speed=5, critical_chance=3)

    Soul(6, '日女巳时', 'RN6-1', 'critical_damage',
         damage_percentage=5, critical_damage=11, critical_chance=2, health_absolute=94)
    Soul(6, '日女巳时', 'RN6-2', 'damage', speed=2, defence_absolute=4, critical_chance=8, health_percentage=8)


def add_fz():
    Soul(1, '反枕', 'FZ1-1', 'null', control_resistance=4, speed=2, critical_chance=6, control_chance=15)
    Soul(2, '反枕', 'FZ2-1', 'damage', control_resistance=4, defence_percentage=2, control_chance=15, health_absolute=203)
    Soul(3, '反枕', 'FZ3-1', 'null', damage_percentage=3, defence_percentage=5, critical_damage=14, critical_chance=6)
    Soul(4, '反枕', 'FZ4-1', 'damage', control_resistance=4, speed=14, critical_damage=7, health_absolute=99)
    Soul(5, '反枕', 'FZ5-1', 'null', damage_absolute=49, critical_chance=3, control_chance=18, health_absolute=99)
    Soul(5, '反枕', 'FZ5-2', 'null', damage_percentage=5, control_resistance=4, critical_chance=13, control_chance=4)
    Soul(6, '反枕', 'FZ6-1', 'critical_damage',
         critical_damage=4, health_percentage=2, critical_chance=11, health_absolute=289)


def add_zc():
    Soul(1, '招财猫', 'ZC1-1', 'null', speed=8, critical_chance=8, health_percentage=5, health_absolute=113)
    Soul(1, '招财猫', 'ZC1-2', 'null', critical_damage=7, defence_percentage=3, critical_chance=11, health_percentage=6)
    Soul(1, '招财猫', 'ZC1-3', 'null', defence_percentage=2, speed=8, defence_absolute=9, critical_damage=8)
    Soul(1, '招财猫', 'ZC1-4', 'null', damage_absolute=51, control_resistance=7, control_chance=14, health_absolute=95)
    Soul(1, '招财猫', 'ZC1-5', 'null', control_resistance=11, defence_percentage=8, speed=3, control_chance=7)

    Soul(2, '招财猫', 'ZC2-1', 'health', damage_percentage=2, speed=6, defence_absolute=10, critical_chance=8)
    Soul(2, '招财猫', 'ZC2-2', 'speed', defence_percentage=3, defence_absolute=4, critical_damage=15, control_chance=7)
    Soul(2, '招财猫', 'ZC2-3', 'speed', speed=8, defence_absolute=4, critical_damage=14, health_absolute=107)
    Soul(2, '招财猫', 'ZC2-4', 'damage', damage_absolute=47, critical_damage=3, critical_chance=10, control_resistance=7)
    Soul(2, '招财猫', 'ZC2-5', 'health', damage_absolute=50, critical_damage=4, critical_chance=8, health_absolute=300)

    Soul(3, '招财猫', 'ZC3-1', 'null', defence_percentage=8, speed=11, control_chance=4, health_absolute=108)

    Soul(4, '招财猫', 'ZC4-1', 'control', control_resistance=4, defence_percentage=5, speed=3, health_percentage=11)
    Soul(4, '招财猫', 'ZC4-2', 'health', critical_damage=7, critical_chance=3, health_percentage=10, control_chance=3)
    Soul(4, '招财猫', 'ZC4-3', 'control', damage_absolute=46, defence_percentage=6, speed=6, control_chance=3)
    Soul(4, '招财猫', 'ZC4-1', 'health', damage_absolute=25, defence_absolute=9, critical_chance=11, health_percentage=3)

    Soul(5, '招财猫', 'ZC5-1', 'null', damage_absolute=25, defence_percentage=5, critical_chance=5, control_resistance=15)
    Soul(5, '招财猫', 'ZC5-2', 'null', damage_absolute=27, defence_absolute=5, critical_damage=17, health_percentage=3)
    Soul(5, '招财猫', 'ZC5-3', 'null', speed=8, defence_absolute=13, health_percentage=5, health_absolute=106)
    Soul(5, '招财猫', 'ZC5-4', 'null', damage_absolute=23, damage_percentage=3, speed=8, health_absolute=188)

    Soul(6, '招财猫', 'ZC6-1', 'damage', speed=8, defence_absolute=9, critical_chance=5, control_chance=4)
    Soul(6, '招财猫', 'ZC6-2', 'health', damage_absolute=46, critical_damage=3, speed=8, critical_chance=8)
    Soul(6, '招财猫', 'ZC6-3', 'health', damage_absolute=22, damage_percentage=8, speed=11, control_resistance=4)
    Soul(6, '招财猫', 'ZC6-4', 'damage', control_resistance=4, health_percentage=3, speed=16, defence_absolute=4)


def add_xyh():
    Soul(1, '雪幽魂', 'XH1-1', 'null', damage_percentage=6, control_resistance=14, health_percentage=5, control_chance=3)
    Soul(1, '雪幽魂', 'XH1-2', 'null', damage_absolute=24, defence_percentage=3, critical_chance=9, control_chance=14)
    Soul(2, '雪幽魂', 'XH2-1', 'speed', damage_absolute=26, damage_percentage=5, speed=11, control_chance=7)
    Soul(3, '雪幽魂', 'XH3-1', 'null', damage_absolute=26, control_resistance=14, speed=6, control_chance=4)
    Soul(3, '雪幽魂', 'XH3-2', 'null', damage_absolute=26, control_chance=18, health_percentage=3, health_absolute=198)
    Soul(3, '雪幽魂', 'XH3-3', 'null', damage_percentage=5, critical_chance=3, control_chance=18, health_absolute=95)
    Soul(4, '雪幽魂', 'XH4-1', 'control', damage_percentage=2, control_resistance=3, speed=3, control_chance=15)
    Soul(5, '雪幽魂', 'XH5-1', 'null', defence_percentage=6, speed=8, health_percentage=3, control_chance=11)
    Soul(6, '雪幽魂', 'XH6-1', 'critical_chance', damage_absolute=23, defence_percentage=6, speed=3, critical_chance=13)
    Soul(6, '雪幽魂', 'XH6-1', 'critical_damage', damage_absolute=48, control_resistance=4, speed=13, defence_absolute=5)


def add_my():
    Soul(1, '魅妖', 'MY1-1', 'null', speed=3, critical_chance=10, health_percentage=2, control_chance=11)
    Soul(2, '魅妖', 'MY2-1', 'damage', damage_absolute=25, damage_percentage=6, critical_damage=14, health_absolute=105)
    Soul(3, '魅妖', 'MY3-1', 'null', damage_percentage=14, speed=3, critical_chance=3, control_chance=7)
    Soul(3, '魅妖', 'MY3-2', 'null', control_resistance=7, speed=11, defence_absolute=5, critical_chance=3)
    Soul(3, '魅妖', 'MY3-3', 'null', critical_damage=11, speed=8, critical_chance=3, health_percentage=2)
    Soul(4, '魅妖', 'MY4-1', 'damage', control_resistance=10, speed=5, critical_chance=3, control_chance=11)
    Soul(4, '魅妖', 'MY4-2', 'control', damage_percentage=3, defence_percentage=3, defence_absolute=5, critical_damage=17)
    Soul(5, '魅妖', 'MY5-1', 'null', damage_absolute=45, control_resistance=7, critical_damage=3, control_chance=14)
    Soul(6, '魅妖', 'MY6-1', 'critical_chance',
         critical_damage=4, defence_percentage=3, critical_chance=8, health_absolute=200)


def add_zz():
    Soul(1, '珍珠', 'ZZ1-1', 'null', damage_percentage=11, control_resistance=3, critical_chance=3, control_chance=7)
    Soul(2, '珍珠', 'ZZ2-1', 'speed', damage_percentage=2, control_resistance=8, defence_absolute=14, health_percentage=3)
    Soul(3, '珍珠', 'ZZ3-1', 'null', damage_absolute=24, control_resistance=14, speed=5, defence_absolute=9)
    Soul(4, '珍珠', 'ZZ4-1', 'health', control_resistance=17, defence_percentage=3, critical_chance=5, control_chance=4)
    Soul(5, '珍珠', 'ZZ5-1', 'null', damage_absolute=47, damage_percentage=3, critical_chance=2, health_percentage=8)


def add_hl():
    Soul(1, '火灵', 'HL1-1', 'null', control_resistance=11, defence_percentage=3, speed=10, control_chance=4)
    Soul(1, '火灵', 'HL1-2', 'null', defence_percentage=3, speed=3, defence_absolute=9, health_percentage=14)
    Soul(1, '火灵', 'HL1-3', 'null', damage_absolute=24, damage_percentage=5, critical_chance=3, control_resistance=18)
    Soul(2, '火灵', 'HL2-1', 'health', damage_percentage=5, control_resistance=14, critical_damage=4, control_chance=7)
    Soul(2, '火灵', 'HL2-2', 'damage', critical_damage=14, speed=5, critical_chance=3, health_absolute=211)
    Soul(3, '火灵', 'HL3-1', 'null', damage_percentage=8, control_resistance=14, defence_absolute=5, critical_chance=3)
    Soul(3, '火灵', 'HL3-2', 'null', damage_percentage=8, critical_damage=10, critical_chance=5, health_percentage=3)
    Soul(3, '火灵', 'HL3-3', 'null', damage_percentage=2, critical_damage=18, critical_chance=3, control_resistance=7)
    Soul(3, '火灵', 'HL3-4', 'null', defence_percentage=3, speed=8, health_percentage=3, control_chance=11)
    Soul(4, '火灵', 'HL4-1', 'control_resistance',
         control_resistance=15, critical_damage=4, defence_absolute=5, critical_chance=3)
    Soul(4, '火灵', 'HL4-2', 'health', damage_percentage=3, control_resistance=15, defence_absolute=5, control_chance=11)
    Soul(5, '火灵', 'HL5-1', 'null', damage_percentage=3, critical_chance=11, control_chance=11, health_absolute=110)
    Soul(5, '火灵', 'HL5-2', 'null', damage_percentage=5, control_resistance=4, critical_chance=11, control_chance=7)
    Soul(5, '火灵', 'HL5-3', 'null', critical_damage=4, critical_chance=3, health_percentage=14, health_absolute=207)
    Soul(6, '火灵', 'HL6-1', 'health', speed=3, defence_absolute=5, critical_damage=11, health_percentage=11)
    Soul(6, '火灵', 'HL6-2', 'damage', defence_absolute=4, critical_chance=5, health_percentage=5, control_chance=11)


def add_bj():
    Soul(1, '蚌精', 'BJ1-1', 'null', control_resistance=4, speed=3, critical_chance=16, health_percentage=3)
    Soul(1, '蚌精', 'BJ1-2', 'null', critical_damage=17, speed=2, critical_chance=2, control_chance=7)
    Soul(1, '蚌精', 'BJ1-3', 'null', damage_percentage=5, control_resistance=7, critical_chance=3, control_chance=15)

    Soul(2, '蚌精', 'BJ2-1', 'speed', damage_absolute=47, defence_percentage=3, defence_absolute=13, control_resistance=4)
    Soul(2, '蚌精', 'BJ2-2', 'health', control_resistance=11, critical_damage=7, control_chance=11, health_absolute=94)
    Soul(2, '蚌精', 'BJ2-3', 'speed', control_resistance=4, speed=14, critical_chance=3, health_absolute=94)
    Soul(2, '蚌精', 'BJ2-4', 'speed', damage_percentage=10, speed=3, health_percentage=5, control_chance=4)

    Soul(3, '蚌精', 'BJ3-1', 'null', control_resistance=15, speed=2, defence_absolute=8, health_percentage=5)
    Soul(3, '蚌精', 'BJ3-2', 'null', damage_percentage=5, speed=11, critical_chance=6, control_chance=3)
    Soul(3, '蚌精', 'BJ3-3', 'null', speed=2, critical_chance=3, health_percentage=11, control_chance=10)
    Soul(3, '蚌精', 'BJ3-4', 'null', damage_percentage=3, defence_percentage=3, speed=13, critical_chance=2)
    Soul(3, '蚌精', 'BJ3-5', 'null', control_chance=19, critical_chance=3, health_percentage=3, health_absolute=94)

    Soul(4, '蚌精', 'BJ4-1', 'control', damage_absolute=23, speed=3, control_chance=14, health_absolute=101)
    Soul(4, '蚌精', 'BJ4-2', 'control', damage_absolute=50, speed=5, defence_absolute=9, control_chance=4)
    Soul(4, '蚌精', 'BJ4-3', 'damage', damage_percentage=15, critical_damage=3, critical_chance=3, control_resistance=4)
    Soul(4, '蚌精', 'BJ4-4', 'damage', control_resistance=7, critical_damage=7, critical_chance=5, control_chance=7)

    Soul(5, '蚌精', 'BJ5-1', 'null', defence_percentage=3, defence_absolute=4, critical_chance=16, control_chance=4)
    Soul(5, '蚌精', 'BJ5-2', 'null', control_resistance=8, defence_percentage=3, critical_damage=4, control_chance=11)
    Soul(5, '蚌精', 'BJ5-3', 'null', damage_absolute=47, speed=12, control_chance=4, health_absolute=95)
    Soul(5, '蚌精', 'BJ5-4', 'null', damage_absolute=48, damage_percentage=5, speed=6, critical_chance=5)

    Soul(6, '蚌精', 'BJ6-1', 'health', damage_absolute=23, critical_damage=4, critical_chance=3, control_chance=19)
    Soul(6, '蚌精', 'BJ6-2', 'critical_chance', damage_percentage=3, speed=3, critical_damage=10, health_absolute=309)
    Soul(6, '蚌精', 'BJ6-3', 'defence', control_resistance=7, speed=8, health_percentage=8, health_absolute=108)
    Soul(6, '蚌精', 'BJ6-4', 'critical_damage',
         defence_absolute=4, critical_damage=4, control_chance=19, health_absolute=101)


def add_wl():
    Soul(1, '魍魉之匣', 'WL1-1', 'null', speed=14, defence_absolute=9, health_percentage=3, control_chance=4)
    Soul(1, '魍魉之匣', 'WL1-2', 'null', damage_absolute=26, defence_absolute=14, critical_damage=7, control_chance=10)
    Soul(1, '魍魉之匣', 'WL1-3', 'null', damage_absolute=47, damage_percentage=3, speed=8, control_resistance=11)
    Soul(1, '魍魉之匣', 'WL1-4', 'null', control_resistance=4, critical_damage=7, critical_chance=10, health_absolute=206)

    Soul(2, '魍魉之匣', 'WL2-1', 'speed',
         control_resistance=11, defence_percentage=8, critical_chance=3, health_percentage=3)
    Soul(2, '魍魉之匣', 'WL2-2', 'damage', damage_absolute=46, damage_percentage=8, critical_damage=7, critical_chance=6)
    Soul(2, '魍魉之匣', 'WL2-3', 'speed', control_chance=7, critical_chance=3, health_percentage=8, health_absolute=97)
    Soul(2, '魍魉之匣', 'WL2-4', 'speed', control_resistance=3, health_percentage=3, critical_chance=3, control_chance=22)

    Soul(3, '魍魉之匣', 'WL3-1', 'null', control_resistance=3, critical_chance=6, control_chance=18, health_absolute=114)
    Soul(3, '魍魉之匣', 'WL3-2', 'null', damage_absolute=25, control_resistance=21, control_chance=4, health_absolute=113)

    Soul(4, '魍魉之匣', 'WL4-1', 'control_resistance',
         damage_absolute=95, damage_percentage=3, critical_chance=3, control_resistance=3)
    Soul(4, '魍魉之匣', 'WL4-2', 'control', critical_damage=4, speed=5, critical_chance=5, control_chance=14)

    Soul(5, '魍魉之匣', 'WL5-1', 'null', control_resistance=3, health_percentage=3, speed=10, critical_damage=7)
    Soul(5, '魍魉之匣', 'WL5-2', 'null', damage_absolute=22, speed=3, control_chance=21, health_absolute=106)
    Soul(5, '魍魉之匣', 'WL5-3', 'null', damage_absolute=51, control_resistance=11, critical_chance=6, health_absolute=210)
    Soul(5, '魍魉之匣', 'WL5-4', 'null', damage_percentage=5, speed=3, control_chance=17, health_absolute=102)

    Soul(6, '魍魉之匣', 'WL6-1', 'damage', damage_percentage=6, speed=14, critical_chance=3, control_chance=3)
    Soul(6, '魍魉之匣', 'WL6-2', 'critical_damage',
         control_resistance=4, critical_damage=3, critical_chance=11, control_chance=4)


def add_fh():
    Soul(1, '返魂香', 'FH1-1', 'null', damage_absolute=25, control_resistance=14, health_percentage=5, control_chance=4)
    Soul(1, '返魂香', 'FH1-2', 'null', speed=2, critical_chance=11, health_percentage=3, control_chance=7)
    Soul(1, '返魂香', 'FH1-3', 'null', speed=6, critical_chance=3, control_chance=15, health_absolute=191)

    Soul(2, '返魂香', 'FH2-1', 'speed', defence_percentage=3, critical_chance=3, control_chance=11, health_absolute=200)
    Soul(2, '返魂香', 'FH2-2', 'speed', damage_absolute=48, critical_damage=7, health_percentage=3, control_chance=15)
    Soul(2, '返魂香', 'FH2-3', 'damage', control_resistance=7, speed=8, critical_damage=7, control_chance=3)

    Soul(3, '返魂香', 'FH3-1', 'null', defence_percentage=3, speed=11, critical_chance=3, control_chance=4)

    Soul(4, '返魂香', 'FH4-1', 'control_resistance', damage_percentage=6, speed=8, defence_absolute=4, critical_chance=6)
    Soul(4, '返魂香', 'FH4-2', 'damage', damage_percentage=2, critical_damage=15, speed=5, critical_chance=3)

    Soul(5, '返魂香', 'FH5-1', 'null', damage_absolute=47, critical_chance=3, control_chance=18, health_absolute=93)
    Soul(5, '返魂香', 'FH5-2', 'null', control_resistance=8, critical_damage=14, critical_chance=3, control_chance=7)
    Soul(5, '返魂香', 'FH5-3', 'null', defence_absolute=4, critical_chance=8, health_percentage=2, control_chance=11)
    Soul(5, '返魂香', 'FH5-4', 'null', control_resistance=4, critical_damage=11, speed=6, critical_chance=6)

    Soul(6, '返魂香', 'FH6-1', 'critical_chance',
         control_resistance=7, defence_percentage=11, speed=3, health_percentage=5)
    Soul(6, '返魂香', 'FH6-2', 'health', control_resistance=3, speed=11, critical_chance=3, health_percentage=3)


def add_hkl():
    Soul(1, '荒骷髅', 'HK1-1', 'null',
         critical_damage=7, defence_percentage=8, speed=3, critical_chance=9, damage_percentage=8)
    Soul(1, '荒骷髅', 'HK1-2', 'null',
         defence_percentage=6, speed=3, defence_absolute=13, critical_damage=7, critical_chance=8)
    Soul(1, '荒骷髅', 'HK1-3', 'null',
         critical_damage=4, defence_percentage=5, critical_chance=6, control_resistance=8, damage_percentage=8)

    Soul(2, '荒骷髅', 'HK2-1', 'health',
         critical_damage=19, speed=5, critical_chance=2, control_chance=3, control_resistance=8)
    Soul(2, '荒骷髅', 'HK2-2', 'speed',
         damage_percentage=3, speed=7, critical_damage=4, health_absolute=402, health_percentage=8)
    Soul(2, '荒骷髅', 'HK2-3', 'damage', damage_percentage=14, defence_percentage=3, critical_chance=10, control_chance=3)
    Soul(2, '荒骷髅', 'HK2-4', 'speed', damage_percentage=5, defence_percentage=5, speed=5, control_chance=18)
    Soul(2, '荒骷髅', 'HK2-5', 'damage',
         damage_absolute=26, speed=3, critical_damage=11, health_percentage=5, critical_chance=8)

    Soul(3, '荒骷髅', 'HK3-1', 'null', speed=3, defence_absolute=4, critical_chance=14, control_chance=3, damage_percentage=8)
    Soul(4, '荒骷髅', 'HK4-1', 'control', damage_absolute=74, defence_percentage=5, speed=3, control_chance=12)

    Soul(5, '荒骷髅', 'HK5-1', 'null', damage_absolute=27, speed=11, critical_chance=2, control_chance=3, damage_percentage=8)
    Soul(5, '荒骷髅', 'HK5-2', 'null', control_resistance=19, speed=5, critical_chance=11, health_percentage=3)
    Soul(5, '荒骷髅', 'HK5-3', 'null',
         damage_absolute=27, critical_damage=7, speed=6, critical_chance=10, health_percentage=8)

    Soul(6, '荒骷髅', 'HK6-1', 'critical_chance',
         control_resistance=7, defence_absolute=4, critical_damage=10, health_percentage=11)
    Soul(6, '荒骷髅', 'HK6-2', 'critical_damage',
         control_resistance=4, critical_damage=11, speed=2, critical_chance=8, defence_percentage=16)


def add_all_souls():
    add_xy()
    add_mw()
    add_z()
    add_lrd()
    add_fy()
    add_kg()
    add_ps()
    add_shn()
    add_wq()
    add_sw()
    add_zn()
    add_sy()
    add_th()
    add_zl()
    add_jj()
    add_bf()
    add_np()
    add_dz()
    add_mm()
    add_rn()
    add_fz()
    add_zc()
    add_xyh()
    add_my()
    add_zz()
    add_hl()
    add_bj()
    add_wl()
    add_fh()
    add_hkl()

