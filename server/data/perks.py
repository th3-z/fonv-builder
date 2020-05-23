PERKS = [
    {
        "id": "lady_killer",
        "name": "Lady Killer",
        "name_female": "Black Widow",
        "benefit": "+10% damage to the opposite sex and unique dialogue options with certain characters",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "confirmed_bachelor",
        "name": "Confirmed Bachelor",
        "name_female": "Cherchez La Femme",
        "benefit": "+10% damage to the same sex and unique dialogue options with certain characters",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "friend_of_the_night",
        "name": "Friend of the Night",
        "name_female": None,
        "benefit": "Your eyes adapt quickly to low-light conditions",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "perception": 6
        },
        "required_skills": {
            "sneak": 30
        }
    },
    {
        "id": "heave_ho",
        "name": "Heave, Ho!",
        "name_female": None,
        "benefit": "+50% thrown weapon velocity and range",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "strength": 5
        },
        "required_skills": {
            "explosives": 30
        }
    },
    {
        "id": "hunter",
        "name": "Hunter",
        "name_female": None,
        "benefit": "In combat, you do 75% more critical damage against animals and mutated animals",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 30
        }
    },
    {
        "id": "intense_training",
        "name": "Intense Training",
        "name_female": None,
        "benefit": "You can put a single point into any of your SPECIAL attributes",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 10,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "rapid_reload",
        "name": "Rapid Reload",
        "name_female": None,
        "benefit": "All of your weapon reloads are 25% faster than normal",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "agility": 5
        },
        "required_skills": {
            "guns": 30
        }
    },
    {
        "id": "retention",
        "name": "Retention",
        "name_female": None,
        "benefit": "Skill magazines last for 3 real-time minutes",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "intelligence": 5
        },
        "required_skills": {}
    },
    {
        "id": "swift_learner",
        "name": "Swift Learner",
        "name_female": None,
        "benefit": "You gain an additional 10% whenever experience points are earned",
        "expansion": "base",
        "level_requirement": 2,
        "ranks": 3,
        "required_specials": {
            "intelligence": 4
        },
        "required_skills": {}
    },
    {
        "id": "cannibal",
        "name": "Cannibal",
        "name_female": None,
        "benefit": "When you're in Sneak mode, you gain the option to eat a human corpse to regain hit points, but lose Karma",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "comprehension",
        "name": "Comprehension",
        "name_female": None,
        "benefit": "You gain one additional skill point for reading books and double the skill points for reading magazines",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {
            "intelligence": 4
        },
        "required_skills": {}
    },
    {
        "id": "educated",
        "name": "Educated",
        "name_female": None,
        "benefit": "You gain two more skill points every time you advance in level",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {
            "intelligence": 4
        },
        "required_skills": {}
    },
    {
        "id": "entomologist",
        "name": "Entomologist",
        "name_female": None,
        "benefit": "You do an additional 50% damage every time you attack a mutated insect",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {
            "intelligence": 4
        },
        "required_skills": {
            "survival": 45
        }
    },
    {
        "id": "rad_child",
        "name": "Rad Child",
        "name_female": None,
        "benefit": "Regenerate 2 HP per second per 200 rads accumulated",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 70
        }
    },
    {
        "id": "run_n_gun",
        "name": "Run 'n Gun",
        "name_female": None,
        "benefit": "Halved spread with one-handed ranged weapons while walking or running",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            # Guns 45 or energy_weapons 45
        }
    },
    {
        "id": "travel_light",
        "name": "Travel Light",
        "name_female": None,
        "benefit": "While wearing light armor or no armor, you run 10% faster",
        "expansion": "base",
        "level_requirement": 4,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 45
        }
    },
    {
        "id": "bloody_mess",
        "name": "Bloody Mess",
        "name_female": None,
        "benefit": "+5% overall damage; more violent death animations",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "demolition_expert",
        "name": "Demolition Expert",
        "name_female": None,
        "benefit": "+20% damage with explosives",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 3,
        "required_specials": {},
        "required_skills": {
            "explosives": 50
        }
    },
    {
        "id": "ferocious_loyalty",
        "name": "Ferocious Loyalty",
        "name_female": None,
        "benefit": "When you drop below 50% HP, companions gain +50 DR",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {
            "charisma": 6
        },
        "required_skills": {}
    },
    {
        "id": "fortune_finder",
        "name": "Fortune Finder",
        "name_female": None,
        "benefit": "Considerably more bottle caps will be found in stockpiles",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "gunslinger",
        "name": "Gunslinger",
        "name_female": None,
        "benefit": "+25% accuracy in V.A.T.S. with one-handed weapons",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "hand_loader",
        "name": "Hand Loader",
        "name_female": None,
        "benefit": "When using Guns, you are twice as likely to recover cases and hulls. You also have all hand load recipes unlocked at any reloading benches",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "repair": 70
        }
    },
    {
        "id": "lead_belly",
        "name": "Lead Belly",
        "name_female": None,
        "benefit": "-50% radiation taken from food and water sources",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {
            "endurance": 5
        },
        "required_skills": {}
    },
    {
        "id": "shotgun_surgeon",
        "name": "Shotgun Surgeon",
        "name_female": None,
        "benefit": "When using shotguns, regardless of ammunition used, you ignore an additional 10 points of a target's Damage Threshold",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "the_professional",
        "name": "The Professional",
        "name_female": None,
        "benefit": "Your sneak attack criticals with revolvers, pistols, and submachine guns (guns and energy weapons) all inflict an additional 20% damage",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "sneak": 70
        }
    },
    {
        "id": "toughness",
        "name": "Toughness",
        "name_female": None,
        "benefit": "+3 DT permanently",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 2,
        "required_specials": {
            "endurance": 5
        },
        "required_skills": {}
    },
    {
        "id": "vigilant_recycler",
        "name": "Vigilant Recycler",
        "name_female": None,
        "benefit": "When using Energy Weapons, you are twice as likely to recover drained ammunition. You also have more efficient recycling recipes available at workbenches",
        "expansion": "base",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "science": 70
        }
    },
    {
        "id": "commando",
        "name": "Commando",
        "name_female": None,
        "benefit": "+25% accuracy in V.A.T.S. with two-handed weapons",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "cowboy",
        "name": "Cowboy",
        "name_female": None,
        "benefit": "+25% damage done by dynamite, hatchets, knives, revolvers, and lever-action guns",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "guns": 45,
            "melee": 45
        }
    },
    {
        "id": "living_anatomy",
        "name": "Living Anatomy",
        "name_female": None,
        "benefit": "Shows health and Damage Threshold of any target. +5% bonus to damage against humans and non-feral ghouls",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "medicine": 70
        }
    },
    {
        "id": "pack_rat",
        "name": "Pack Rat",
        "name_female": None,
        "benefit": "Items with a weight of two pounds or less now weigh half as much",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "intelligence": 5
        },
        "required_skills": {
            "barter": 70
        }
    },
    {
        "id": "quick_draw",
        "name": "Quick Draw",
        "name_female": None,
        "benefit": "Makes weapon equipping and holstering 50% faster",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "agility": 5
        },
        "required_skills": {}
    },
    {
        "id": "rad_resistance",
        "name": "Rad Resistance",
        "name_female": None,
        "benefit": "+25% radiation resistance permanently",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "endurance": 5
        },
        "required_skills": {
            "survival": 40
        }
    },
    {
        "id": "scrounger",
        "name": "Scrounger",
        "name_female": None,
        "benefit": "Considerably more ammunition in stockpiles",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "luck": 5
        },
        "required_skills": {}
    },
    {
        "id": "stonewall",
        "name": "Stonewall",
        "name_female": None,
        "benefit": "+5 DT against melee and unarmed attacks and cannot be knocked down during combat",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "strength": 6,
            "endurance": 6
        },
        "required_skills": {}
    },
    {
        "id": "strong_back",
        "name": "Strong Back",
        "name_female": None,
        "benefit": "+50 Carry Weight",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "strength": 5,
            "edurance": 5
        },
        "required_skills": {}
    },
    {
        "id": "super_slam",
        "name": "Super Slam!",
        "name_female": None,
        "benefit": "All melee (except thrown) and unarmed attacks have a chance of knocking your target down. 15% for Unarmed or one-handed melee, 30% for two-handed melee",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {
            "strength": 6
        },
        "required_skills": {
            "melee_weapons": 45
        }
    },
    {
        "id": "terrifying_presence",
        "name": "Terrifying Presence",
        "name_female": None,
        "benefit": "Can intimidate foes through dialogue; closing dialogue results in the foe fleeing for 5 seconds",
        "expansion": "base",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "speech": 70
        }
    },
    {
        "id": "here_and_now",
        "name": "Here and Now",
        "name_female": None,
        "benefit": "You instantly level up again",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "animal_friend",
        "name": "Animal Friend",
        "name_female": None,
        "benefit": "On 1st rank, hostile animals become friendly. On 2nd rank they come to your aid against enemies except against other animals",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 2,
        "required_specials": {
            "charisma": 6
        },
        "required_skills": {
            "survival": 45
        }
    },
    {
        "id": "finesse",
        "name": "Finesse",
        "name_female": None,
        "benefit": "+5% Critical Chance",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "math_wrath",
        "name": "Math Wrath",
        "name_female": None,
        "benefit": "Reduces all AP costs by 10%",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "miss_fortune",
        "name": "Miss Fortune",
        "name_female": None,
        "benefit": "10% chance that Miss Fortune will incapacitate a target in V.A.T.S",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {
            "luck": 5
        },
        "required_skills": {}
    },
    {
        "id": "mister_sandman",
        "name": "Mister Sandman",
        "name_female": None,
        "benefit": "Can instantly kill a sleeping non-player character, and earn bonus XP when doing so",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "sneak": 60
        }
    },
    {
        "id": "mysterious_stranger",
        "name": "Mysterious Stranger",
        "name_female": None,
        "benefit": "10% chance that the Stranger will finish off a target in V.A.T.S",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {
            "luck": 5
        },
        "required_skills": {}
    },
    {
        "id": "nerd_rage",
        "name": "Nerd Rage!",
        "name_female": None,
        "benefit": "+15 DT and Strength increased to 10 whenever health is 20% or lower",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {
            "intelligence": 5
        },
        "required_skills": {
            "science": 70
        }
    },
    {
        "id": "night_person",
        "name": "Night Person",
        "name_female": None,
        "benefit": "+2 Intelligence and +2 Perception between 6:00 P.M. and 6:00 A.M",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "plasma_spaz",
        "name": "Plasma Spaz",
        "name_female": None,
        "benefit": "AP costs for all plasma weapons are reduced by 20%",
        "expansion": "base",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "energy_weapons": 70
        }
    },
    {
        "id": "fast_metabolism",
        "name": "Fast Metabolism",
        "name_female": None,
        "benefit": "+20% Hit Points restored with stimpaks",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "ghastly_scavenger",  # Requires cannibal perk
        "name": "Ghastly Scavenger",
        "name_female": None,
        "benefit": "When you're in Sneak mode, you gain the option to eat a super mutant or feral ghoul corpse to regain hit points, but lose Karma",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "hit_the_deck",
        "name": "Hit the Deck",
        "name_female": None,
        "benefit": "+25 DT against explosives",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "explosives": 70
        }
    },
    {
        "id": "life_giver",
        "name": "Life Giver",
        "name_female": None,
        "benefit": "+30 hit points",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "endurance": 6
        },
        "required_skills": {}
    },
    {
        "id": "long_haul",
        "name": "Long Haul",
        "name_female": None,
        "benefit": "Being over-encumbered no longer prevents you from using fast travel",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "endurance": 6
        },
        "required_skills": {
            "barter": 70
        }
    },
    {
        "id": "piercing_strike",
        "name": "Piercing Strike",
        "name_female": None,
        "benefit": "All your unarmed and melee attacks negate 15 points of DT",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "unarmed": 70
        }
    },
    {
        "id": "pyromaniac",
        "name": "Pyromaniac",
        "name_female": None,
        "benefit": "+50% damage with fire-based weapons",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "explosives": 60
        }
    },
    {
        "id": "robotics_expert",
        "name": "Robotics Expert",
        "name_female": None,
        "benefit": "+25% damage to robots; can shut down robots by sneaking up on them and deactivating",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "science": 70
        }
    },
    {
        "id": "silent_running",
        "name": "Silent Running",
        "name_female": None,
        "benefit": "Running no longer factors into a successful sneak attempt",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "agility": 6
        },
        "required_skills": {
            "sneak": 50
        }
    },
    {
        "id": "sniper",
        "name": "Sniper",
        "name_female": None,
        "benefit": "25% more likely to hit the target's head in V.A.T.S",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "perception": 6,
            "agility": 6
        },
        "required_skills": {}
    },
    {
        "id": "splash_damage",
        "name": "Splash Damage",
        "name_female": None,
        "benefit": "Explosives have a 25% larger area of effect",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "explosives": 70
        }
    },
    {
        "id": "unstoppable_force",
        "name": "Unstoppable Force",
        "name_female": None,
        "benefit": "x4 normal damage through enemy blocks with melee and unarmed attacks",
        "expansion": "base",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "strength": 7
        },
        "required_skills": {
            "melee_weapons": 90
        }
    },
    {
        "id": "adamantium_skeleton",
        "name": "Adamantium Skeleton",
        "name_female": None,
        "benefit": "Damage taken by limbs reduced by 50%",
        "expansion": "base",
        "level_requirement": 14,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "center_of_mass",
        "name": "Center of Mass",
        "name_female": None,
        "benefit": "In V.A.T.S., you do an additional 15% damage when targeting the torso",
        "expansion": "base",
        "level_requirement": 14,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "guns": 70
        }
    },
    {
        "id": "chemist",
        "name": "Chemist",
        "name_female": None,
        "benefit": "Chems and (in Hardcore) stimpaks last twice as long",
        "expansion": "base",
        "level_requirement": 14,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "medicine": 60
        }
    },
    {
        "id": "jury_rigging",
        "name": "Jury Rigging",
        "name_female": None,
        "benefit": "Repair any item using a roughly similar item",
        "expansion": "base",
        "level_requirement": 14,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "repair": 90
        }
    },
    {
        "id": "light_step",
        "name": "Light Step",
        "name_female": None,
        "benefit": "Floor traps or mines will not be set off",
        "expansion": "base",
        "level_requirement": 14,
        "ranks": 1,
        "required_specials": {
            "perception": 6,
            "agility": 6
        },
        "required_skills": {}
    },
    {
        "id": "purifier",
        "name": "Purifier",
        "name_female": None,
        "benefit": "You do 50% extra damage with melee and unarmed weapons against centaurs, night stalkers, spore plants, spore carriers, deathclaws and super mutants",
        "expansion": "base",
        "level_requirement": 14,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "action_boy",
        "name": "Action Boy",
        "name_female": "Action Girl",
        "benefit": "+15 Action Points",
        "expansion": "base",
        "level_requirement": 16,
        "ranks": 2,
        "required_specials": {
            "agility": 6
        },
        "required_skills": {}
    },
    {
        "id": "better_criticals",
        "name": "Better Criticals",
        "name_female": None,
        "benefit": "+50% damage with critical hits",
        "expansion": "base",
        "level_requirement": 16,
        "ranks": 1,
        "required_specials": {
            "perception": 6,
            "luck": 6
        },
        "required_skills": {}
    },
    {
        "id": "chem_resistant",
        "name": "Chem Resistant",
        "name_female": None,
        "benefit": "Half as likely to get addicted",
        "expansion": "base",
        "level_requirement": 16,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "medicine": 60
        }
    },
    {
        "id": "meltdown",
        "name": "Meltdown",
        "name_female": None,
        "benefit": "Foes killed by your Energy Weapons emit a corona of harmful energy",
        "expansion": "base",
        "level_requirement": 16,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "energy_weapons": 90
        }
    },
    {
        "id": "tag",
        "name": "Tag!",
        "name_female": None,
        "benefit": "Fourth \"tag\" skill: +15 points to that skill",
        "expansion": "base",
        "level_requirement": 16,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "weapon_handling",
        "name": "Weapon Handling",
        "name_female": None,
        "benefit": "Weapon Strength requirements are now 2 points lower than normal for you",
        "expansion": "base",
        "level_requirement": 16,
        "ranks": 1,
        "required_specials": {
            # Stength less than 10
        },
        "required_skills": {}
    },
    {
        "id": "computer_whiz",
        "name": "Computer Whiz",
        "name_female": None,
        "benefit": "Can make one extra attempt to hack a locked-down terminal",
        "expansion": "base",
        "level_requirement": 18,
        "ranks": 1,
        "required_specials": {
            "intelligence": 7
        },
        "required_skills": {
            "science": 70
        }
    },
    {
        "id": "concentrated_fire",
        "name": "Concentrated Fire",
        "name_female": None,
        "benefit": "+5% accuracy in V.A.T.S. with every subsequent attack on a given body part queued",
        "expansion": "base",
        "level_requirement": 18,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "energy_weapons": 60,
            "guns": 60
        }
    },
    {
        "id": "infiltrator",
        "name": "Infiltrator",
        "name_female": None,
        "benefit": "Can make one more attempt to pick a broken lock",
        "expansion": "base",
        "level_requirement": 18,
        "ranks": 1,
        "required_specials": {
            "perception": 6
        },
        "required_skills": {
            "lockpick": 70
        }
    },
    {
        "id": "paralyzing_palm",
        "name": "Paralyzing Palm",
        "name_female": None,
        "benefit": "Can paralyze an enemy for 30 seconds with a V.A.T.S. unarmed attack",
        "expansion": "base",
        "level_requirement": 18,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "unarmed": 70
        }
    },
    {
        "id": "explorer",
        "name": "Explorer",
        "name_female": None,
        "benefit": "All locations are marked on your map",
        "expansion": "base",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "grim_reapers_sprint",
        "name": "Grim Reaper's Sprint",
        "name_female": None,
        "benefit": "A kill in V.A.T.S. restores 20 AP immediately",
        "expansion": "base",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "ninja",
        "name": "Ninja",
        "name_female": None,
        "benefit": "x1.15 (instead of +15 luck due to a bug) critical chance with melee and unarmed weapons, +25% damage with melee/unarmed sneak attack criticals",
        "expansion": "base",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "melee_weapons": 80,
            "sneak": 80
        }
    },
    {
        "id": "solar_powered",
        "name": "Solar Powered",
        "name_female": None,
        "benefit": "+2 Strength and +1 HP per second while outside, from 6:00 A.M. to 6:00 P.M",
        "expansion": "base",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {
            "endurance": 7
        },
        "required_skills": {}
    },
    {
        "id": "laser_commander",
        "name": "Laser Commander",
        "name_female": None,
        "benefit": "You do an extra 15% damage and have a 10% extra chance to critically hit with any laser weapon",
        "expansion": "base",
        "level_requirement": 22,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "energy_weapons": 90
        }
    },
    {
        "id": "nuka_chemist",
        "name": "Nuka Chemist",
        "name_female": None,
        "benefit": "Unlocks special Nuka-Cola recipes at the workbench",
        "expansion": "base",
        "level_requirement": 22,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "science": 90
        }
    },
    {
        "id": "spray_and_pay",
        "name": "Spray and Pray",
        "name_female": None,
        "benefit": "Your attacks do 75% less damage to companions",
        "expansion": "base",
        "level_requirement": 22,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "slayer",
        "name": "Slayer",
        "name_female": None,
        "benefit": "The speed of all your melee and unarmed attacks is increased by 30%",
        "expansion": "base",
        "level_requirement": 24,
        "ranks": 1,
        "required_specials": {
            "strength": 7,
            "agility": 7
        },
        "required_skills": {
            "unarmed": 90
        }
    },
    {
        "id": "nerves_of_steel",
        "name": "Nerves of Steel",
        "name_female": None,
        "benefit": "20% faster AP regeneration",
        "expansion": "base",
        "level_requirement": 26,
        "ranks": 1,
        "required_specials": {
            "agility": 7
        },
        "required_skills": {}
    },
    {
        "id": "rad_absorption",
        "name": "Rad Absorption",
        "name_female": None,
        "benefit": "-1 Rad every 20 seconds",
        "expansion": "base",
        "level_requirement": 28,
        "ranks": 1,
        "required_specials": {
            "endurance": 7
        },
        "required_skills": {}
    },
    {
        "id": "in_shining_armor",
        "name": "In Shining Armor",  # Bugged perk, does nothing
        "name_female": None,
        "benefit": "+5 DT against energy weapons while wearing metal armor, with a further +2 DT while wearing reflective eyewear or helmets",
        "expansion": "dead_money",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "repair": 20,
            "science": 70
        }
    },
    {
        "id": "junk_rounds",
        "name": "Junk Rounds",
        "name_female": None,
        "benefit": "You can craft ammunition using scrap metal and tin cans",
        "expansion": "dead_money",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "luck": 6
        },
        "required_skills": {
            "repair": 45
        }
    },
    {
        "id": "light_touch",
        "name": "Light Touch",
        "name_female": None,
        "benefit": "While wearing light armor you gain +5% critical hit chance and your enemies suffer a -25% critical hit chance",
        "expansion": "dead_money",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "agility": 6
        },
        "required_skills": {
            "repair": 45
        }
    },
    {
        "id": "old_world_gourmet",
        "name": "Old World Gourmet",
        "name_female": None,
        "benefit": "+25% addiction resistance. +50% health bonus from snack foods. Scotch, vodka and wine now give you health in addition to their normal effects",
        "expansion": "dead_money",
        "level_requirement": 2,
        "ranks": 1,
        "required_specials": {
            "endurance": 6
        },
        "required_skills": {
            "survival": 45
        }
    },
    {
        "id": "and_stay_back",
        "name": "And Stay Back",
        "name_female": None,
        "benefit": "Shotguns have a 10% chance, per pellet, of knocking an enemy back",
        "expansion": "dead_money",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "guns": 70
        }
    },
    {
        "id": "heavyweight",
        "name": "Heavyweight",
        "name_female": None,
        "benefit": "Weapons with a weight of more than 10 are cut in half. This does not affect weapons modded to under 10 wg",
        "expansion": "dead_money",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "strength": 7
        },
        "required_skills": {}
    },
    {
        "id": "hobbler",
        "name": "Hobbler",
        "name_female": None,
        "benefit": "Your chance to hit an opponent's legs in V.A.T.S. is increased by 25%",
        "expansion": "dead_money",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            "perception": 7
        },
        "required_skills": {}
    },
    {
        "id": "grunt",
        "name": "Grunt",
        "name_female": None,
        "benefit": "25% more damage with 9mm pistols and SMGs, .45 pistols and SMGs, service rifles, assault and Marksman carbines, light machine guns, frag grenades, grenade rifles and launchers and combat knives",
        "expansion": "honest_hearts",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "guns": 45,
            "explosives": 20
        }
    },
    {
        "id": "home_on_the_range",
        "name": "Home on the Range",
        "name_female": None,
        "benefit": "Whenever you interact with a campfire, you have the option of sleeping, with all the benefits that sleep brings",
        "expansion": "honest_hearts",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 70
        }
    },
    {
        "id": "sneering_imperialist",
        "name": "Sneering Imperialist",
        "name_female": None,
        "benefit": "+15% Damage and +25% accuracy in V.A.T.S. to various tribal and raider characters",
        "expansion": "honest_hearts",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "tribal_wisdom",
        "name": "Tribal Wisdom",
        "name_female": None,
        "benefit": "-50% limb damage from animals, mutated animals, and mutated insects, +25% to Poison resistance, ability to eat mutated insects in sneak mode",
        "expansion": "honest_hearts",
        "level_requirement": 8,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 70
        }
    },
    {
        "id": "fight_the_power",
        "name": "Fight the Power!",
        "name_female": None,
        "benefit": "+2 Damage Threshold and +5% Critical chance against anyone wearing NCR, Legion or Brotherhood of Steel armor",
        "expansion": "honest_hearts",
        "level_requirement": 10,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "eye_for_eye",
        "name": "Eye for Eye",
        "name_female": None,
        "benefit": "For each crippled limb you have, you do an additional 10% damage",
        "expansion": "honest_hearts",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "atomic",
        "name": "Atomic!",
        "name_female": None,
        "benefit": "In irradiated areas, +25% move and attack speed, +2 DT, +2 ST. With excess rad level, AP regen scales from 1.1 times to 1.5 times normal",
        "expansion": "old_world_blues",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {
            "endurance": 6
        },
        "required_skills": {}
    },
    {
        "id": "mile_in_their_shoes",
        "name": "Mile in Their Shoes",
        "name_female": None,
        "benefit": "You have come to understand night stalkers. Consuming night stalker squeezin's now grants bonuses to Perception (+1 PER), Poison Resistance (+5), and Stealth (+5 Sneak) in addition to the normal benefits",
        "expansion": "old_world_blues",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 25
        }
    },
    {
        "id": "thems_good_eatin",
        "name": "Them's Good Eatin'",
        "name_female": None,
        "benefit": "Any living creature you kill has a 50% chance to have the potent healing items thin red paste or blood sausage when looted",
        "expansion": "old_world_blues",
        "level_requirement": 20,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 55
        }
    },
    {
        "id": "implant_grx",
        "name": "Implant GRX",
        "name_female": None,
        "benefit": "You gain a non-addictive subdermal turbo (chem) injector. This perk may be taken twice, with the second rank increasing the effect from 2 to 3 seconds and the uses per day from 5 to 10 (activated in the Pip-Boy inventory)",
        "expansion": "old_world_blues",
        "level_requirement": 30,
        "ranks": 2,
        "required_specials": {
            "endurance": 8
        },
        "required_skills": {}
    },
    {
        "id": "alertness",
        "name": "Alertness",
        "name_female": None,
        "benefit": "+2 Perception when crouched and still",
        "expansion": "lonesome_road",
        "level_requirement": 12,
        "ranks": 1,
        "required_specials": {
            # Perception between 6 and 9
        },
        "required_skills": {}
    },
    {
        "id": "walker_instinct",
        "name": "Walker Instinct",
        "name_female": None,
        "benefit": "+1 Perception and Agility when outside",
        "expansion": "lonesome_road",
        "level_requirement": 18,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 50
        }
    },
    {
        "id": "irradiated_beauty",
        "name": "Irradiated Beauty",
        "name_female": None,
        "benefit": "Sleep removes all Rads (Hardcore: only -100 Rads)",
        "expansion": "lonesome_road",
        "level_requirement": 22,
        "ranks": 1,
        "required_specials": {
            "endurance": 8
        },
        "required_skills": {}
    },
    {
        "id": "voracious_reader",
        "name": "Voracious Reader",
        "name_female": None,
        "benefit": "Damaged books become blank magazines; can copy existing magazines into blank magazines",
        "expansion": "lonesome_road",
        "level_requirement": 22,
        "ranks": 1,
        "required_specials": {
            "intelligence": 7
        },
        "required_skills": {}
    },
    {
        "id": "lessons_learned",
        "name": "Lessons Learned",
        "name_female": None,
        "benefit": "+1% XP gain per player level",
        "expansion": "lonesome_road",
        "level_requirement": 26,
        "ranks": 1,
        "required_specials": {
            "intelligence": 6
        },
        "required_skills": {}
    },
    {
        "id": "tunnel_runner",
        "name": "Tunnel Runner",
        "name_female": None,
        "benefit": "+25% sneaking speed when wearing light or no armor",
        "expansion": "lonesome_road",
        "level_requirement": 26,
        "ranks": 1,
        "required_specials": {
            "agility": 8
        },
        "required_skills": {}
    },
    {
        "id": "roughin_it",
        "name": "Roughin' It",
        "name_female": None,
        "benefit": "Sleeping outside gives Well Rested benefit",
        "expansion": "lonesome_road",
        "level_requirement": 28,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {
            "survival": 100
        }
    },
    {
        "id": "burden_to_bear",
        "name": "Burden to Bear",
        "name_female": None,
        "benefit": "+50 carry weight",
        "expansion": "lonesome_road",
        "level_requirement": 30,
        "ranks": 1,
        "required_specials": {
            "strength": 6,
            "endurance": 6
        },
        "required_skills": {}
    },
    {
        "id": "broad_daylight",
        "name": "Broad Daylight",
        "name_female": None,
        "benefit": "No Sneak penalty for using Pip-Boy light",
        "expansion": "lonesome_road",
        "level_requirement": 36,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "certified_tech",
        "name": "Certified Tech",
        "name_female": None,
        "benefit": "+25% critical hit chance against robots, 85% chance of finding an extra crafting component on destroyed robots",
        "expansion": "lonesome_road",
        "level_requirement": 40,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "aint_like_that_now",  # The following three require karma to be within certain bounds
        "name": "Ain't Like That Now",
        "name_female": None,
        "benefit": "Karma reset to 0, +25% AP regeneration rate, +20% attack speed, immunity to critical hits",
        "expansion": "lonesome_road",
        "level_requirement": 50,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "just_lucky_im_alive",
        "name": "Just Lucky I'm Alive",
        "name_female": None,
        "benefit": "+4 Luck for 3 minutes upon finishing a battle with less than 25% health; immunity to critical hits, +50% critical damage",
        "expansion": "lonesome_road",
        "level_requirement": 50,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "thought_you_died",
        "name": "Thought You Died",
        "name_female": None,
        "benefit": "+10 Health per 100 Karma; Karma reset to 0, +10% damage, immunity to critical hits",
        "expansion": "lonesome_road",
        "level_requirement": 50,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    },
    {
        "id": "mad_bomber",
        "name": "Mad Bomber",
        "name_female": None,
        "benefit": "Enables you to create special explosive recipes at any workbench",
        "expansion": "gun_runners_arsenal",
        "level_requirement": 6,
        "ranks": 1,
        "required_specials": {},
        "required_skills": {}
    }
]