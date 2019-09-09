# coding=utf-8


class Soul:
    soul_list = [[], [], [], [], [], []]

    def __init__(self, position, soul_type, soul_code, main_property='default', speed=0, critical_chance=0,
                 critical_damage=0, damage_percentage=0,  damage_absolute=0, health_percentage=0, health_absolute=0,
                 defence_percentage=0, defence_absolute=0, control_chance=0, control_resistance=0):
        self.code = soul_code
        self.equipped = False
        self.ignored = False

        self.position = position
        self.soul_type = soul_type
        self.speed = speed
        self.critical_chance = critical_chance
        self.critical_damage = critical_damage
        self.damage_percentage = damage_percentage
        self.damage_absolute = damage_absolute
        self.health_percentage = health_percentage
        self.health_absolute = health_absolute
        self.defence_percentage = defence_percentage
        self.defence_absolute = defence_absolute
        self.control_chance = control_chance
        self.control_resistance = control_resistance
        self.main_property = main_property
        if main_property == 'critical_chance':
            self.critical_chance += 55
        elif main_property == 'critical_damage':
            self.critical_damage += 89
        elif main_property == 'health':
            self.health_percentage += 55
        elif main_property == 'defence':
            self.defence_percentage += 55
        elif main_property == 'damage':
            self.damage_percentage += 55
        elif main_property == 'speed':
            self.speed += 57
        elif main_property == 'control':
            self.control_chance += 55
        elif main_property == 'control_resistance':
            self.control_resistance += 55

        self.soul_list[self.position - 1].append(self)


class Pair:
    pair_dictionary = {
        (1, 2): [], (1, 3): [], (1, 4): [], (1, 5): [], (1, 6): [],
        (2, 3): [], (2, 4): [], (2, 5): [], (2, 6): [], (3, 4): [],
        (3, 5): [], (3, 6): [], (4, 5): [], (4, 6): [], (5, 6): []
    }

    def __init__(self, soul_1, soul_2):
        self.position = (soul_1.position, soul_2.position)
        self.member = (soul_1, soul_2)
        self.soul_type = soul_1.soul_type

        self.speed = soul_1.speed + soul_2.speed
        self.critical_chance = soul_1.critical_chance + soul_2.critical_chance
        self.critical_damage = soul_1.critical_damage + soul_2.critical_damage
        self.damage_percentage = soul_1.damage_percentage + soul_2.damage_percentage
        self.damage_absolute = soul_1.damage_absolute + soul_2.damage_absolute
        self.health_percentage = soul_1.health_percentage + soul_2.health_percentage
        self.health_absolute = soul_1.health_absolute + soul_2.health_absolute
        self.defence_percentage = soul_1.defence_percentage + soul_2.defence_percentage
        self.defence_absolute = soul_1.defence_absolute + soul_2.defence_absolute
        self.control_chance = soul_1.control_chance + soul_2.control_chance
        self.control_resistance = soul_1.control_resistance + soul_2.control_resistance
        self.pair_dictionary[self.position].append(self)

    @classmethod
    def generate(cls):
        cls.pair_dictionary = {
            (1, 2): [], (1, 3): [], (1, 4): [], (1, 5): [], (1, 6): [],
            (2, 3): [], (2, 4): [], (2, 5): [], (2, 6): [], (3, 4): [],
            (3, 5): [], (3, 6): [], (4, 5): [], (4, 6): [], (5, 6): []
        }
        for position_number_1 in range(6):
            for position_number_2 in range(position_number_1 + 1, 6):
                for soul_1 in Soul.soul_list[position_number_1]:
                    for soul_2 in Soul.soul_list[position_number_2]:
                        if soul_1.soul_type == soul_2.soul_type and \
                                not (soul_1.equipped or soul_2.equipped or soul_1.ignored or soul_2.ignored):
                            Pair(soul_1, soul_2)
        for position_number_1 in range(6):
            for position_number_2 in range(position_number_1 + 1, 6):
                for soul_1 in Soul.soul_list[position_number_1]:
                    soul_1.ignored = False
                for soul_2 in Soul.soul_list[position_number_2]:
                    soul_2.ignored = False


class Suit:
    suit_dictionary = {
        (1, 2, 3, 4): [(5, 6), []], (1, 2, 3, 5): [(4, 6), []], (1, 2, 3, 6): [(4, 5), []],
        (1, 2, 4, 5): [(3, 6), []], (1, 2, 4, 6): [(3, 5), []], (1, 2, 5, 6): [(3, 4), []],
        (1, 3, 4, 5): [(2, 6), []], (1, 3, 4, 6): [(2, 5), []], (1, 3, 5, 6): [(2, 4), []],
        (1, 4, 5, 6): [(2, 3), []], (2, 3, 4, 5): [(1, 6), []], (2, 3, 4, 6): [(1, 5), []],
        (2, 3, 5, 6): [(1, 4), []], (2, 4, 5, 6): [(1, 3), []], (3, 4, 5, 6): [(1, 2), []]
    }

    def __init__(self, pair_1, pair_2):
        self.position = (pair_1.position[0], pair_1.position[1], pair_2.position[0], pair_2.position[1])
        self.member = (pair_1.member[0], pair_1.member[1], pair_2.member[0], pair_2.member[1])
        self.soul_type = pair_1.soul_type

        self.speed = pair_1.speed + pair_2.speed
        self.critical_chance = pair_1.critical_chance + pair_2.critical_chance
        self.critical_damage = pair_1.critical_damage + pair_2.critical_damage
        self.damage_percentage = pair_1.damage_percentage + pair_2.damage_percentage
        self.damage_absolute = pair_1.damage_absolute + pair_2.damage_absolute
        self.health_percentage = pair_1.health_percentage + pair_2.health_percentage
        self.health_absolute = pair_1.health_absolute + pair_2.health_absolute
        self.defence_percentage = pair_1.defence_percentage + pair_2.defence_percentage
        self.defence_absolute = pair_1.defence_absolute + pair_2.defence_absolute
        self.control_chance = pair_1.control_chance + pair_2.control_chance
        self.control_resistance = pair_1.control_resistance + pair_2.control_resistance

        self.suit_dictionary[self.position][1].append(self)

    @classmethod
    def generate(cls, suit_type_filter):
        cls.suit_dictionary = {
            (1, 2, 3, 4): [(5, 6), []], (1, 2, 3, 5): [(4, 6), []], (1, 2, 3, 6): [(4, 5), []],
            (1, 2, 4, 5): [(3, 6), []], (1, 2, 4, 6): [(3, 5), []], (1, 2, 5, 6): [(3, 4), []],
            (1, 3, 4, 5): [(2, 6), []], (1, 3, 4, 6): [(2, 5), []], (1, 3, 5, 6): [(2, 4), []],
            (1, 4, 5, 6): [(2, 3), []], (2, 3, 4, 5): [(1, 6), []], (2, 3, 4, 6): [(1, 5), []],
            (2, 3, 5, 6): [(1, 4), []], (2, 4, 5, 6): [(1, 3), []], (3, 4, 5, 6): [(1, 2), []]
        }
        for pair_position_1 in Pair.pair_dictionary:
            for pair_position_2 in Pair.pair_dictionary:
                if pair_position_1[1] < pair_position_2[0]:
                    for pair_1 in Pair.pair_dictionary[pair_position_1]:
                        if suit_type_filter != [''] and (pair_1.soul_type not in suit_type_filter):
                            continue
                        for pair_2 in Pair.pair_dictionary[pair_position_2]:
                            if pair_1.soul_type == pair_2.soul_type:
                                Suit(pair_1, pair_2)


class Equip:
    equip_dictionary = {
        "阴摩罗": ['damage', []], "心眼": ['damage', []], "鸣屋": ['damage', []], "狰": ['damage', []],
        "轮入道": ['damage', []], "蝠翼": ['damage', []], "狂骨": ['damage', []], "镇墓兽": ['critical', []],
        "破势": ['critical', []], "伤魂鸟": ['critical', []], "网切": ['critical', []], "三味": ['critical', []],
        "针女": ['critical', []], "树妖": ['health', []], "薙魂": ['health', []], "钟灵": ['health', []],
        "镜姬": ['health', []], "被服": ['health', []], "涅槃之火": ['health', []], "地藏像": ['health', []],
        "木魅": ['defence', []], "日女巳时": ['defence', []], "反枕": ['defence', []], "招财猫": ['defence', []],
        "雪幽魂": ['defence', []], "魅妖": ['defence', []], "珍珠": ['defence', []], "火灵": ['control', []],
        "蚌精": ['control', []], "魍魉之匣": ['control_resistance', []], "幽谷响": ['control_resistance', []],
        "返魂香": ['control_resistance', []], "骰子鬼": ['control_resistance', []], '荒骷髅': ['null', []]
    }

    def __init__(self, suit, pair):
        self.soul_type = suit.soul_type
        self.side_soul_type = pair.soul_type
        self.member = suit.member + pair.member
        self.speed = suit.speed + pair.speed
        self.critical_chance = suit.critical_chance + pair.critical_chance
        self.critical_damage = suit.critical_damage + pair.critical_damage
        self.damage_percentage = suit.damage_percentage + pair.damage_percentage
        self.damage_absolute = suit.damage_absolute + pair.damage_absolute
        self.health_percentage = suit.health_percentage + pair.health_percentage
        self.health_absolute = suit.health_absolute + pair.health_absolute
        self.defence_percentage = suit.defence_percentage + pair.defence_percentage
        self.defence_absolute = suit.defence_absolute + pair.defence_absolute
        self.control_chance = suit.control_chance + pair.control_chance
        self.control_resistance = suit.control_resistance + pair.control_resistance

        self.health_absolute += 2052
        self.damage_absolute += 486
        self.defence_absolute += 104

        if self.equip_dictionary[suit.soul_type][0] == 'damage':
            self.damage_percentage += 15
        elif self.equip_dictionary[suit.soul_type][0] == 'critical':
            self.critical_chance += 15
        elif self.equip_dictionary[suit.soul_type][0] == 'health':
            self.health_percentage += 15
        elif self.equip_dictionary[suit.soul_type][0] == 'defence':
            self.defence_percentage += 15
        elif self.equip_dictionary[suit.soul_type][0] == 'control':
            self.control_chance += 15
        elif self.equip_dictionary[suit.soul_type][0] == 'control_resistance':
            self.control_resistance += 15

        if self.equip_dictionary[pair.soul_type][0] == 'damage':
            self.damage_percentage += 15
        elif self.equip_dictionary[pair.soul_type][0] == 'critical':
            self.critical_chance += 15
        elif self.equip_dictionary[pair.soul_type][0] == 'health':
            self.health_percentage += 15
        elif self.equip_dictionary[pair.soul_type][0] == 'defence':
            self.defence_percentage += 15
        elif self.equip_dictionary[pair.soul_type][0] == 'control':
            self.control_chance += 15
        elif self.equip_dictionary[pair.soul_type][0] == 'control_resistance':
            self.control_resistance += 15

        self.equip_dictionary[self.soul_type][1].append(self)

    @classmethod
    def show_equip(cls, target):
        qualified_equip_dictionary = {}
        for soul_type in cls.equip_dictionary:
            qualified_equip_dictionary[soul_type] = []
            if cls.equip_dictionary[soul_type][1]:
                equip_number = 0
                for equip in cls.equip_dictionary[soul_type][1]:
                    meet_target = equip.critical_chance >= target['critical_chance'] and \
                                  equip.critical_damage >= target['critical_damage'] and \
                                  equip.damage_percentage >= target['damage_percentage'] and \
                                  equip.health_percentage >= target['health_percentage'] and \
                                  equip.control_chance >= target['control_chance'] and \
                                  equip.control_resistance >= target['control_resistance'] and \
                                  target['speed_min'] <= equip.speed <= target['speed_max']
                    if not meet_target:
                        continue
                    equip_number += 1
                    soul_info = '[%s<%s>] Id:%s 御魂：' % (soul_type, equip.side_soul_type, equip_number)
                    for soul in equip.member:
                        soul_info += "%s " % soul.code
                    damage_coefficient = (equip.critical_damage + 150) * (equip.damage_percentage + 100)
                    soul_info += "速度:%s 暴击:%s 暴击伤害:%s 攻击加成:%s 生命加成：%s 效果命中：%s 效果抵抗：%s 伤害系数：%s" % \
                                 (equip.speed, equip.critical_chance, equip.critical_damage, equip.damage_percentage,
                                  equip.health_percentage, equip.control_chance, equip.control_resistance, damage_coefficient)
                    print(soul_info)
                    qualified_equip_dictionary[soul_type].append((equip, soul_info))
        return qualified_equip_dictionary

    @classmethod
    def generate(cls, side_soul_type):
        cls.equip_dictionary = {
            "阴摩罗": ['damage', []], "心眼": ['damage', []], "鸣屋": ['damage', []], "狰": ['damage', []],
            "轮入道": ['damage', []], "蝠翼": ['damage', []], "狂骨": ['damage', []], "镇墓兽": ['critical', []],
            "破势": ['critical', []], "伤魂鸟": ['critical', []], "网切": ['critical', []], "三味": ['critical', []],
            "针女": ['critical', []], "树妖": ['health', []], "薙魂": ['health', []], "钟灵": ['health', []],
            "镜姬": ['health', []], "被服": ['health', []], "涅槃之火": ['health', []], "地藏像": ['health', []],
            "木魅": ['defence', []], "日女巳时": ['defence', []], "反枕": ['defence', []], "招财猫": ['defence', []],
            "雪幽魂": ['defence', []], "魅妖": ['defence', []], "珍珠": ['defence', []], "火灵": ['control', []],
            "蚌精": ['control', []], "魍魉之匣": ['control_resistance', []], "幽谷响": ['control_resistance', []],
            "返魂香": ['control_resistance', []], "骰子鬼": ['control_resistance', []], '荒骷髅': ['null', []]
        }
        for position in Suit.suit_dictionary:
            for suit in Suit.suit_dictionary[position][1]:
                for pair in Pair.pair_dictionary[Suit.suit_dictionary[position][0]]:
                    if side_soul_type != [''] and (pair.soul_type not in side_soul_type):
                        continue
                    if suit.soul_type != pair.soul_type:
                        Equip(suit, pair)
        for position in Suit.suit_dictionary:
            for suit in Suit.suit_dictionary[position][1]:
                for pair in Pair.pair_dictionary[Suit.suit_dictionary[position][0]]:
                    if side_soul_type != [''] and (pair.soul_type not in side_soul_type):
                        continue
                    if suit.soul_type == pair.soul_type:
                        Equip(suit, pair)
            break
