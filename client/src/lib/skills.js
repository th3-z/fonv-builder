const good_natured_bonus = [
    "speech", "medicine", "repair", "science", "barter"
]
const good_natured_penalty = [
    "energy_weapons", "explosives", "guns", "melee_weapons", "unarmed"
]

function skill(player, skill) {
    var bonus = 0
    var penalty = 0
    
    // Special
    bonus = player.base_specials[skill.special_id]*2
    // Luck
    bonus += Math.ceil(player.base_specials.luck/2)

    // Books
    const has_comprehension = player.perks.find(perk => perk.id == "comprehension")
    for (let book in player.books) {
        if (book.id == skill.book_id) {
            if (has_comprehension) {
                bonus += 3
            } else {
                bonus += 4
            }
        }
    }

    // Skilled
    if (player.traits.includes("skilled")) {
        bonus += 5
    }

    // Good natured
    if (player.traits.includes("good_natured")) {
        if (good_natured_bonus.includes(skill.id)) {
            bonus += 5
        } else if (good_natured_penalty.includes(skill.id)) {
            penalty += 5
        }
    }
    
    return Math.min(
        100,
        player.base_skills[skill.id].value + bonus - penalty
    )
}

export default {
    skill
}

