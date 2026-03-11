# The rules mapped from the original experta class
RULES = {
    "Myopia": {
        "symptoms": {'itching': '0', 'blurring': '1', 'redness': '0', 'night': '1', 'mucus': '0', 'tear': '0', 'yellowing': '0', 'headache': '1', 'cough': '0', 'pain': '0', 'overstrain': '1', 'sensitivity': '0', 'rainbow': '0', 'double': '0', 'sightedness': '1', 'sight': '0', 'nausea': '0', 'dilated': '0', 'eyelid': '1'},
        "description": "Nearsightedness (myopia) is a common vision condition in which you can see objects near to you clearly, but objects farther away are blurry.",
        "photo": r".\photo\Myopia.jpg"
    },
    "Conjunctivitis": {
        "symptoms": {'itching': '1', 'blurring': '1', 'redness': '1', 'night': '0', 'mucus': '1', 'tear': '1', 'yellowing': '0', 'headache': '0', 'cough': '0', 'pain': '1', 'overstrain': '1', 'sensitivity': '1', 'rainbow': '0', 'double': '0', 'sightedness': '0', 'sight': '0', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Pink eye (conjunctivitis) is the inflammation or infection of the transparent membrane that lines your eyelid and eyeball.",
        "photo": r".\photo\Conjunctivitis.jpg"
    },
    "Ocular Allergy": {
        "symptoms": {'itching': '1', 'blurring': '0', 'redness': '1', 'night': '1', 'mucus': '1', 'tear': '0', 'yellowing': '0', 'headache': '0', 'cough': '0', 'pain': '1', 'overstrain': '0', 'sensitivity': '1', 'rainbow': '0', 'double': '0', 'sightedness': '0', 'sight': '1', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Ocular allergy is an inflammatory reaction of the surface of the eye to particles (allergens) in the environment.",
        "photo": r".\photo\ocular-allergy.jpg"
    },
    "Glaucoma": {
        "symptoms": {'itching': '0', 'blurring': '1', 'redness': '1', 'night': '1', 'mucus': '0', 'tear': '0', 'yellowing': '1', 'headache': '0', 'cough': '0', 'pain': '1', 'overstrain': '0', 'sensitivity': '0', 'rainbow': '1', 'double': '0', 'sightedness': '0', 'sight': '1', 'nausea': '1', 'dilated': '1', 'eyelid': '0'},
        "description": "Glaucoma is a group of eye conditions that damage the optic nerve, the health of which is vital for good vision.",
        "photo": r".\photo\Glaucoma.jpg"
    },
    "Cataract": {
        "symptoms": {'itching': '0', 'blurring': '1', 'redness': '0', 'night': '1', 'mucus': '0', 'tear': '0', 'yellowing': '1', 'headache': '0', 'cough': '0', 'pain': '0', 'overstrain': '0', 'sensitivity': '1', 'rainbow': '1', 'double': '1', 'sightedness': '1', 'sight': '0', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Cataract is a clouding of the normally clear lens of the eye.",
        "photo": r".\photo\cataracts.png"
    },
    "Night Blindness": {
        "symptoms": {'itching': '0', 'blurring': '1', 'redness': '0', 'night': '1', 'mucus': '0', 'tear': '0', 'yellowing': '0', 'headache': '0', 'cough': '0', 'pain': '0', 'overstrain': '1', 'sensitivity': '1', 'rainbow': '1', 'double': '0', 'sightedness': '1', 'sight': '1', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Night blindness (nyctalopia) is your inability to see well at night or in poor light.",
        "photo": r".\photo\night-blindness.jpg"
    },
    "Diabetic retinopathy": {
        "symptoms": {'itching': '0', 'blurring': '1', 'redness': '1', 'night': '1', 'mucus': '0', 'tear': '0', 'yellowing': '0', 'headache': '0', 'cough': '0', 'pain': '0', 'overstrain': '1', 'sensitivity': '1', 'rainbow': '1', 'double': '0', 'sightedness': '1', 'sight': '1', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Diabetic retinopathy is a diabetes complication that affects eyes.",
        "photo": r".\photo\diabetic.jpg"
    },
    "Trachoma": {
        "symptoms": {'itching': '1', 'blurring': '0', 'redness': '1', 'night': '0', 'mucus': '0', 'tear': '1', 'yellowing': '1', 'headache': '0', 'cough': '0', 'pain': '0', 'overstrain': '1', 'sensitivity': '1', 'rainbow': '1', 'double': '0', 'sightedness': '0', 'sight': '0', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Trachoma is a microbial infection of the eye, caused due to the bacterium Chlamydia trachomatis.",
        "photo": r".\photo\Trachoma.jpg"
    },
    "Refractive errors": {
        "symptoms": {'itching': '0', 'blurring': '1', 'redness': '0', 'night': '0', 'mucus': '0', 'tear': '0', 'yellowing': '0', 'headache': '1', 'cough': '0', 'pain': '0', 'overstrain': '1', 'sensitivity': '1', 'rainbow': '1', 'double': '0', 'sightedness': '1', 'sight': '1', 'nausea': '0', 'dilated': '0', 'eyelid': '0'},
        "description": "Refractive error means that the eye cannot reflect the light properly, making vision blurry.",
        "photo": r".\photo\Refractive-errors.jpg"
    }
}

QUESTIONS = {
    "itching": "Do you experience itching and burning in your eyes?",
    "blurring": "Do you experience a blurring vision?",
    "redness": "Do you experience redness in your eye color?",
    "night": "Do you experience difficulty in seeing while driving at night?",
    "mucus": "Do you experience a discharge of sticky mucus in your eyes?",
    "tear": "Do you have a tear in both eyes?",
    "yellowing": "Do you experience yellowing of colors in your eyes?",
    "headache": "Do you experience severe headache?",
    "cough": "Do you experience cough, running nose and scratching throat?",
    "pain": "Do you experience eye pain and swollen eyelid?",
    "overstrain": "Does your eyes constantly overstrain you?",
    "sensitivity": "Do you experience an increased sensitivity to light?",
    "rainbow": "Do you see halos or rainbow-colored circle around light?",
    "double": "Do you experience double vision in a single eye?",
    "sightedness": "Do you experience nearsightedness?",
    "sight": "Do you experience sudden loss of sight?",
    "nausea": "Do you constant nausea and vomiting?",
    "dilated": "Do you have a dilated pupil?",
    "eyelid": "Do you need to partially close your eyelid to see clearly?"
}