import computedSkill from './skills.js'
import computedSpecial from './special.js'

import store from '../store'

function isVisible(perk, player) {
    if (player.perks.find(pl_perk => pl_perk.id == perk.id)) return false
    if (!perk.required_perk) return true
    if (player.perks.find(pl_perk => pl_perk.id == perk.required_perk)) return true
    return false
}

function reqList(perk, player) {
    let idx = 0
    let reqList = []
    
    reqList.push({
        requirement: "Level " + perk.level_requirement,
        ok: perk.level_requirement <= player.level,
        idx: idx
    })

    idx++

    for (let skill in perk.required_skills) {
        reqList.push({
            requirement: skill + " " + perk.required_skills[skill],
            ok: perk.required_skills[skill] <= computedSkill.skill(player, store.getters.getSkill(skill)),
            idx: idx
        })
        idx++
    }

    for (let special in perk.required_specials) {
        reqList.push({
            requirement: special + " " + perk.required_specials[special],
            ok: perk.required_specials[special] <= computedSpecial.special(player, store.getters.getSpecial(special)),
            idx: idx
        })
        idx++
    }

    return reqList
}

export default {
    isVisible,
    reqList
}

