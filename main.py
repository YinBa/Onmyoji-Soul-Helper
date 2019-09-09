# coding=utf-8
from AddSouls import add_all_souls
from SoulLib import Soul, Pair, Suit, Equip


def soul_filter(target_list, logic):
    for soul_position in Soul.soul_list:
        for soul in soul_position:
            if soul.ignored:
                continue
            property_dictionary = {
                'critical': (soul.critical_chance or soul.critical_damage or
                             soul.main_property == 'critical_chance' or soul.main_property == 'critical_damage'),
                'damage': (soul.damage_percentage or soul.main_property == 'damage'),
                'speed': (soul.speed or soul.main_property == 'speed'),
                'control': (soul.control_chance or soul.main_property == 'control_chance'),
                'resistance': (soul.control_resistance or soul.main_property == 'control_resistance')
            }
            if logic == 'and':
                for target in target_list:
                    if not property_dictionary[target]:
                        soul.ignored = True
            elif logic == 'or':
                soul.ignored = True
                for target in target_list:
                    if property_dictionary[target]:
                        soul.ignored = False
            else:
                for target in target_list:
                    if target == 'main' and soul.main_property == 'defence':
                        soul.ignored = True
                    elif target == 'side' and (soul.defence_absolute + soul.defence_percentage) > 0:
                        soul.ignored = True


def config_filter():
    filter_and = []
    filter_or = []
    filter_no = []
    print('每个御魂必须有以下属性：')
    if input('暴击/暴伤[Y/N]') == 'Y':
        filter_and.append('critical')
    if input('攻击加成[Y/N]') == 'Y':
        filter_and.append('damage')
    if input('速度[Y/N]') == 'Y':
        filter_and.append('speed')
    if input('命中[Y/N]') == 'Y':
        filter_and.append('control')
    if input('抵抗[Y/N]') == 'Y':
        filter_and.append('resistance')
    print('每个御魂至少有下列其一的属性：')
    if input('暴击/暴伤[Y/N]') == 'Y':
        filter_or.append('critical')
    if input('攻击加成[Y/N]') == 'Y':
        filter_or.append('damage')
    if input('速度[Y/N]') == 'Y':
        filter_or.append('speed')
    if input('命中[Y/N]') == 'Y':
        filter_or.append('control')
    if input('抵抗[Y/N]') == 'Y':
        filter_or.append('resistance')
    print('御魂不可以有以下属性：')
    if input('主属性为防御加成[Y/N]') == 'Y':
        filter_no.append('main')
    if input('副属性有防御相关[Y/N]') == 'Y':
        filter_no.append('side')
    print('属性范围：')
    critical_chance = input('暴击率(%):')
    critical_damage = input('暴击伤害(%):')
    damage_percentage = input('攻击加成(%):')
    health_percentage = input('生命加成(%):')
    control_chance = input('效果命中(%):')
    control_resistance = input('效果抵抗(%):')
    speed_min = input('最小速度:')
    speed_max = input('最大速度:')
    type_filter = input('御魂范围（以&隔开）:').split('&')
    side_type = input('副御魂类型：').split('&')
    pre_filter = [filter_and, filter_or, filter_no, type_filter, side_type]
    final_filter_str = [critical_chance, critical_damage, damage_percentage, health_percentage, control_chance,
                        control_resistance, speed_min, speed_max]
    final_filter = []
    for final_filter_individual in final_filter_str:
        if final_filter_individual:
            final_filter.append(int(final_filter_individual))
        else:
            final_filter.append(0)
    return pre_filter, final_filter


def main():
    add_all_souls()
    equip_info_list = []
    pre_filter = [[], ['critical', 'damage', 'speed', 'control', 'resistance'], [],
                  ['三味'],
                  ['']]
    final_filter = [95, 90, 0, 55, 0, 25, 80, 83]
    print("当前过滤条件为：\n  暴击≥%s%% 暴伤≥%s%% 攻击加成≥%s%% 生命加成≥%s%%\n"
          "  效果命中≥%s%% 效果抵抗≥%s%% %s≤速度≤%s" %
          (final_filter[0], final_filter[1], final_filter[2], final_filter[3], final_filter[4], final_filter[5],
           final_filter[6], final_filter[7]))
    while True:
        try:
            if input('是否更新过滤条件[Y/N]?') == 'Y':
                pre_filter, final_filter = config_filter()
            soul_filter(pre_filter[0], 'and')
            soul_filter(pre_filter[1], 'or')
            soul_filter(pre_filter[2], 'no')
            Pair.generate()
            Suit.generate(pre_filter[3])
            Equip.generate(pre_filter[4])
            qualified_equip_dictionary = Equip.show_equip(target={'critical_chance': final_filter[0],
                                                                  'critical_damage': final_filter[1],
                                                                  'damage_percentage': final_filter[2],
                                                                  'health_percentage': final_filter[3],
                                                                  'control_chance': final_filter[4],
                                                                  'control_resistance': final_filter[5],
                                                                  'speed_min': final_filter[6],
                                                                  'speed_max': final_filter[7]})
            use_equip_type = input('选定御魂类型：')
            if not use_equip_type:
                continue
            use_equip_index = int(input('选定御魂Id：')) - 1
            use_equip_info = qualified_equip_dictionary[use_equip_type][use_equip_index][1]
            use_equip_obj = qualified_equip_dictionary[use_equip_type][use_equip_index][0]
            for soul_obj in use_equip_obj.member:
                soul_obj.equipped = True
            equip_info_list.append(use_equip_info)
            end_and_print = input('End?')
            if end_and_print:
                for equip_info in equip_info_list:
                    print(equip_info)
                break
        except Exception as e:
            print(e)
            for equip_info in equip_info_list:
                print(equip_info)
            break


if __name__ == '__main__':
    main()
