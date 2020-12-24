function skill(player, skill) {
    
    return Math.min(player.base_skills[skill.id].value + player.base_specials[skill.special_id]*2 + Math.ceil(player.base_specials.luck/2), 100)
}

export default {
    skill
}

