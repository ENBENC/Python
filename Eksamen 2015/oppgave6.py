def kampResultat(scoringerLagA,scoringerLagB):
    if scoringerLagA > scoringerLagB:
        return "hjemme"
    elif scoringerLagA < scoringerLagB:
        return "borte"
    elif scoringerLagA == scoringerLagB:
        return "uabgjort"
