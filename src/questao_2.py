from gekko import GEKKO


def calculate_maximum_flow(valor_arcos: dict) -> None:
    model = GEKKO()
    x14, x24, x25, x26, x35, x45, x46, x47, x56, x58, x67, x68 = model.Array(
        model.Var, 12, integer=True, lb=0
    )
    model.Maximize(x47 + x67 + x58 + x68)
    model.Equations(
        [
            x14 + x24 == x45 + x46 + x47,
            x25 + x35 + x45 == x56 + x58,
            x26 + x46 + x56 == x67 + x68,
            x14 <= valor_arcos["A"],
            x24 <= valor_arcos["B"],
            x26 <= valor_arcos["C"],
            x25 <= valor_arcos["D"],
            x35 <= valor_arcos["E"],
            x47 <= valor_arcos["F"],
            x46 <= valor_arcos["G"],
            x45 <= valor_arcos["H"],
            x56 <= valor_arcos["I"],
            x58 <= valor_arcos["J"],
            x67 <= valor_arcos["K"],
            x68 <= valor_arcos["L"]
        ]
    )
    model.options.SOLVER = 1
    model.solve()
    print('Objective: ', -model.options.OBJFCNVAL)
    print('x14: ', x14.value[0])
    print('x24: ', x24.value[0])
    print('x26: ', x26.value[0])
    print('x25: ', x25.value[0])
    print('x35: ', x35.value[0])
    print('x47: ', x47.value[0])
    print('x46: ', x46.value[0])
    print('x45: ', x45.value[0])
    print('x56: ', x56.value[0])
    print('x58: ', x58.value[0])
    print('x67: ', x67.value[0])
    print('x68: ', x68.value[0])
