function special(player, special) {
    var bonus = 0
    var penalty = 0
    
    // Four eyes
    if (special.id == "perception" && player.traits.includes("four_eyes")) {
        penalty += 1
    }

    // Small Frame
    if (special.id == "agility" && player.traits.includes("small_frame")) {
        bonus += 1
    }

    // Implant
    if (player.implants.find(implant => implant.id == special.implant_id)) {
        bonus += 1
    }

    return Math.min(
        10,
        player.base_specials[special.id] + bonus - penalty
    )
}

function remainingPoints(player) {
    let specialsTotal = 0
    for(let special in player.base_specials) {
        specialsTotal += player.base_specials[special]
    }

    const intenseTraining = player.perks.find(perk => perk.id == "intense_training")
    let intenseTrainingRanks = 0
    if (intenseTraining) {
        intenseTrainingRanks = intenseTraining.rank
    }

    return player.special_points - specialsTotal + intenseTrainingRanks
}

export default {
    special,
    remainingPoints
}

