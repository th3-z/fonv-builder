
function actionPoints(player) {
    let base = 65 + (3 * player.base_specials.agility);
    let bonus = 0

    if (player.traits.includes("kamikaze")) bonus += 10

    




    return base + bonus;
}

export default {
    actionPoints
}

