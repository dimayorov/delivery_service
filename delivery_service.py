# ID 139134802 успешной посылки
def get_transports_amount(mass: list[int], carrying: int):
    """Расчет минимального количества транспортных платформ.

    Функция выполняет расчет минимального количества транспортных платформ
    требуемых для первозки роботов. Платформа не может быть загружена более
    чем двумя роботами с общим весом превышающим её грузоподъемность.

    Args:
        mass (list[int]): список весов отдельных роботов.
        carrying (int): максимальная грузоподъемность платформы.
    """
    weight = sorted(mass)
    light_index = 0
    heavy_index = len(weight) - 1
    transports_amount = 0
    while light_index < heavy_index:
        if weight[light_index] + weight[heavy_index] <= carrying:
            light_index += 1
        heavy_index -= 1
        transports_amount += 1
    if light_index == heavy_index:
        transports_amount += 1
    return transports_amount


if __name__ == '__main__':
    print(get_transports_amount(
        mass=[int(weight) for weight in input().split()],
        carrying=int(input()))
    )
