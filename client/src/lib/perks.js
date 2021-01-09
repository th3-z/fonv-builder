function isVisible(perk, player) {
    if (player.perks.find(pl_perk => pl_perk.id == perk.id)) return false
    if (!perk.required_perk) return true
    if (player.perks.find(pl_perk => pl_perk.id == perk.required_perk)) return true
    return false
}

function reqString(perk) {
    let reqStr = "Level " + perk.level_requirement
    for (let skill in perk.required_skills) {
        reqStr += ", " + skill + " " + perk.required_skills[skill]
    }
    for (let special in perk.required_specials) {
        reqStr += ", " + special + " " + perk.required_specials[special]
    }

    reqStr = reqStr
        .split(' ')
        .map(word => word[0].toUpperCase() + word.substr(1))
        .join(' ')
    return reqStr
}

export default {
    isVisible,
    reqString
}

