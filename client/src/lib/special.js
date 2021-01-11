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

    // Intense trainings
    bonus += player.perks.filter(
        perk => perk.id.substring(0, 16) == "intense_training" && perk.special == special.id
    ).length

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

    return player.special_points - specialsTotal
}

export default {
    special,
    remainingPoints
}

