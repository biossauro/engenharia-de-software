from gekko import GEKKO


def calculate_shortest_path(valor_arcos: dict) -> None:
    model = GEKKO()
    x12, x13, x14, x25, x26, x35, x36, x37, x46, x47, x58, x68, x78 = model.Array(
        model.Var, 13, integer=True, lb=0
    )
    model.Minimize(
        valor_arcos["U"] * x12 +
        valor_arcos["T"] * x13 +
        valor_arcos["S"] * x14 +
        valor_arcos["P"] * x25 +
        valor_arcos["Q"] * x26 +
        valor_arcos["R"] * x35 +
        valor_arcos["K"] * x36 +
        valor_arcos["L"] * x37 +
        valor_arcos["M"] * x46 +
        valor_arcos["N"] * x47 +
        valor_arcos["B"] * x58 +
        valor_arcos["C"] * x68 +
        valor_arcos["D"] * x78
    )
    model.Equations(
        [
            1 == x12 + x13 + x14,
            x12 == x25 + x26,
            x13 == x35 + x36 + x37,
            x14 == x46 + x47,
            x25 + x35 == x58,
            x26 + x36 + x46 == x68,
            x37 + x47 == x78,
            x58 + x68 + x78 == 1
        ]
    )
    model.options.SOLVER = 1
    model.solve()
    print('Objective: ', model.options.OBJFCNVAL)
    print('x12: ', x12.value[0])
    print('x13: ', x13.value[0])
    print('x14: ', x14.value[0])
    print('x25: ', x25.value[0])
    print('x26: ', x26.value[0])
    print('x35: ', x35.value[0])
    print('x36: ', x36.value[0])
    print('x37: ', x37.value[0])
    print('x46: ', x46.value[0])
    print('x47: ', x47.value[0])
    print('x58: ', x58.value[0])
    print('x68: ', x68.value[0])
    print('x78: ', x78.value[0])
