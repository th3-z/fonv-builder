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

    return Math.min(
        10,
        player.base_specials[special.id] + bonus - penalty
    )
}

export default {
    special
}

