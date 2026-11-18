import json
from pathlib import Path

ROOT = Path("c:/JLPT/jlpt-exam-prep")
EXERCISES_PATH = ROOT / "src/data/chapterExercises.json"

exercises = json.load(open(EXERCISES_PATH, encoding="utf-8"))

# Accurate English translations, contextual descriptions, and page citations for SKM N3 Part 1 Ch 6-12 & FRA-D
REPAIRS = {
    # === Chapter 6 (pp. 32–35) ===
    "skm3-c6-q1": {
        "translation": "If you force yourself to work despite feeling a cold coming on, you will end up completely sick in bed.",
        "context": "Warning a coworker who is pushing themselves while sick.",
        "hint": "Which pattern expresses that continuing a negative behavior will lead to a disastrous consequence (V-ては)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q2": {
        "translation": "As long as you have your passport, you can check in to hotels on overseas trips.",
        "context": "Confirming international travel check-in prerequisites.",
        "hint": "Which pattern means 'as long as / if only (sole required condition)' using 〜さえ〜ば?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q3": {
        "translation": "Even if we are far apart, our friendship will never change for eternity.",
        "context": "Reaffirming deep bonds before parting ways.",
        "hint": "Which adverb pairs with 〜ても to mean 'even if / no matter if'?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q4": {
        "translation": "If you haven't read the meeting materials yet, I will hand out a summary of the key points right now.",
        "context": "Offering an immediate solution based on the listener's current condition.",
        "hint": "Which conditional takes a listener's current situation as a premise for an immediate offer (〜のなら)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q5": {
        "translation": "If yesterday's weather had been good, we could have seen the spectacular view from the summit, but because of the fog we couldn't see a thing.",
        "context": "Expressing regret about a contrary-to-fact past condition on a hike.",
        "hint": "Which counterfactual conditional pairs with 〜のに to express what could have been?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q6": {
        "translation": "As long as our teamwork is good, we should be able to win our next match against that powerhouse school.",
        "context": "Encouraging sports team members before a tough match.",
        "hint": "Which pattern highlights teamwork as the essential condition (〜さえ〜ば)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q7": {
        "translation": "Just because you got paid, if you keep wasting money like that, you'll be in trouble by the end of the month.",
        "context": "Cautioning a friend against reckless spending right after payday.",
        "hint": "Which pattern warns against continuing an ongoing negative habit (〜ていては)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q8": {
        "translation": "If the train hadn't been delayed, I would have made it in time for the exam, but I arrived late and couldn't take it.",
        "context": "Lamenting an unfortunate missed exam due to public transit delay.",
        "hint": "Which past negative conditional pairs with 〜ものを to express regret over a prevented outcome?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q9": {
        "translation": "Even if they are your closest friend, you cannot disclose confidential information.",
        "context": "Emphasizing strict professional nondisclosure ethics.",
        "hint": "Which correlative adverb emphasizes 'even granting that' (たとえ〜であっても)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q10": {
        "translation": "If you're not feeling well, decline today's overtime and go home early.",
        "context": "Giving compassionate workplace advice to a sick colleague.",
        "hint": "Which conditional takes a known premise to give advice or an instruction (〜のなら)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q11": {
        "translation": "As long as you take your medicine properly, your fever will probably go down right away.",
        "context": "Reassuring a patient about the effectiveness of prescribed medication.",
        "hint": "Which structure inserts さえ between verb stem and auxiliary conditional (〜さえすれば)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },
    "skm3-c6-q12": {
        "translation": "If I had applied one year earlier, the grand opening discount would have applied, but I didn't make it in time.",
        "context": "Regretting missing a limited-time subscription or membership discount.",
        "hint": "Which past conditional expresses counterfactual regret about an earlier action (〜ていれば)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 6, Practice Drills, pp. 32–35"
    },

    # === Chapter 7 (pp. 36–37) ===
    "skm3-c7-q1": {
        "translation": "According to the city bulletin, garbage sorting methods will be updated starting next month.",
        "context": "Reporting formal municipal announcements about waste disposal.",
        "hint": "Which formal hearsay ending pairs with 〜によると to relay official news (〜とのことだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q2": {
        "translation": "Fermented foods like natto and miso are said to regulate gut health and be beneficial for well-being.",
        "context": "Stating widely acknowledged health facts and common consensus.",
        "hint": "Which passive reporting structure expresses general public knowledge (〜と言われている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q3": {
        "translation": "Tanaka: 'Hey, did you hear if that new cafe in front of the station has opened already?'",
        "context": "Inquiring about neighborhood hearsay in casual conversation.",
        "hint": "Which casual conversational question marker asks about rumors or heard information (〜んだって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q4": {
        "translation": "According to ancient records, this temple was said to have been constructed in the early Heian period.",
        "context": "Recounting historical tradition or written records.",
        "hint": "Which classic hearsay marker reports historical facts passed down in lore (〜という)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q5": {
        "translation": "Takahashi from the class next door is apparently moving to America with his family next month. I wonder if it's true.",
        "context": "Discussing unverified school gossip about a classmate.",
        "hint": "Which rumor particle indicates second-hand, unconfirmed hearsay (〜とか)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q6": {
        "translation": "Receptionist: 'I have a message from the general manager. Today's meeting will begin at 3:00 PM.'",
        "context": "Relaying an executive's message courteously in business.",
        "hint": "Which polite hearsay form reports messages on behalf of a superior (〜とのことです)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q7": {
        "translation": "In professional baseball this season, Team A, boasting a powerhouse pitching roster, is widely predicted to win the championship.",
        "context": "Quoting sports analyst consensus and public expectations.",
        "hint": "Which objective reporting structure conveys what the public expects (〜と言われている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q8": {
        "translation": "Yamada, just now in the staff room the teacher was saying 'come here right away!'",
        "context": "Relaying a teacher's spoken summons to a fellow classmate.",
        "hint": "Which conversational citation marker relays what someone just said (〜って言ってたよ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q9": {
        "translation": "According to this morning's science news, a new species of organism has reportedly been discovered in the deep sea.",
        "context": "Broadcasting newly announced scientific discoveries.",
        "hint": "Which formal report pattern concludes news items (〜ということだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q10": {
        "translation": "According to the village's ancient legend, a giant dragon is said to have lived in that mountain in olden times.",
        "context": "Narrating folklore passed down through local traditions.",
        "hint": "Which traditional narrative hearsay form links folklore records (〜という)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q11": {
        "translation": "According to colleagues, a new evaluation system is apparently being introduced next term, and everyone feels uneasy about it.",
        "context": "Sharing workplace grapevine rumors about policy changes.",
        "hint": "Which conversational hearsay noun phrase means 'I hear that / they say that' (〜とかで)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },
    "skm3-c7-q12": {
        "translation": "(Letter greeting) Having heard that your eldest son successfully passed his university entrance exams, I extend my heartfelt congratulations.",
        "context": "Formal written correspondence congratulating family achievements.",
        "hint": "Which elegant epistolary phrasing introduces heard good news (〜とのこと)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 7, Practice Drills, pp. 36–37"
    },

    # === Chapter 8 (pp. 38–41) ===
    "skm3-c8-q1": {
        "translation": "A person as earnest and honest as him would never embezzle company funds. It must be some kind of mistake.",
        "context": "Defending a trustworthy colleague's integrity against false accusations.",
        "hint": "Which strong logical denial expresses 'there is absolutely no possibility that' (〜わけがない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q2": {
        "translation": "Just because an item is expensive does not necessarily mean its quality is superior.",
        "context": "Consumer advice regarding price versus product craftsmanship.",
        "hint": "Which partial negation pattern pairs with 必ずしも to mean 'not necessarily' (〜とは限らない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q3": {
        "translation": "It is not that I dislike cooking, but on weekdays I simply don't have the time to cook for myself because of work.",
        "context": "Clarifying reasons for dining out frequently despite enjoying culinary arts.",
        "hint": "Which partial negation structure softens an absolute claim to mean 'it's not the case that' (〜わけではない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q4": {
        "translation": "If you repair the bicycle, it's not unusable, but buying a new one would be much faster.",
        "context": "Weighing repair viability against the convenience of a replacement.",
        "hint": "Which double negative pattern means 'it's not that one cannot...' (〜ないことはない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q5": {
        "translation": "This apartment is indeed close to the station, but the rent is so exorbitant that it's out of reach.",
        "context": "Acknowledging one positive factor while highlighting a fatal financial drawback.",
        "hint": "Which concessive repetition pattern concedes a fact before adding a reservation (〜ことは〜が)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q6": {
        "translation": "Since we have practiced relentlessly for months, there is no way we will fail in the actual performance.",
        "context": "Boosting self-confidence before taking the main stage.",
        "hint": "Which logical deduction expresses absolute conviction that an outcome is impossible (〜わけがない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q7": {
        "translation": "Just because someone studied abroad in an English-speaking country for three years does not mean anyone automatically becomes fluent.",
        "context": "Debunking common misconceptions about language acquisition.",
        "hint": "Which phrase pairs with 〜からといって to deny an automatic conclusion (〜とは限らない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q8": {
        "translation": "It's not that I don't want to attend the party, but I already have an unavoidable prior engagement.",
        "context": "Politely declining an invitation while reassuring the host of good intentions.",
        "hint": "Which explanatory negative phrasing means 'it isn't that I don't want to' (〜わけではない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q9": {
        "translation": "If we take a taxi, it's not impossible to make the last Shinkansen bullet train, but I am worried about traffic jams.",
        "context": "Evaluating tight transit options during rush hour.",
        "hint": "Which double negative means 'it is not that we cannot make it' (〜間に合わないこともない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q10": {
        "translation": "As for skiing, I can ski after a fashion, but advanced slopes are completely beyond me.",
        "context": "Clarifying modest winter sports capability.",
        "hint": "Which repetition concedes basic competence before asserting limits (〜ことは〜が)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q11": {
        "translation": "There is no possible way that dishes prepared by an executive chef of a three-star restaurant could taste bad.",
        "context": "Expressing unshakeable trust in culinary masteries.",
        "hint": "Which adjective form attaches directly to わけがない to negate poor taste?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },
    "skm3-c8-q12": {
        "translation": "When treated with kindness, there is no way anyone would not feel happy.",
        "context": "Reflecting on universal human emotional responses to warmth.",
        "hint": "Which negative adjective form attaches to わけがない to mean 'impossible not to feel glad'?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 8, Practice Drills, pp. 38–41"
    },

    # === Chapter 9 (pp. 44–45) ===
    "skm3-c9-q1": {
        "translation": "Excuse me, but I would like to have a native speaker check the Japanese phrasing of this business proposal.",
        "context": "Asking a colleague to arrange language proofreading.",
        "hint": "Which benefactive desiderative expresses wanting another person to perform an action (〜てもらいたい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q2": {
        "translation": "Because I am not feeling well, I would like to leave early today, if that is alright with you.",
        "context": "Requesting permission from a supervisor to depart work early due to illness.",
        "hint": "Which humble causative desiderative politely asks permission for oneself (〜させていただきたい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q3": {
        "translation": "It would be wonderful if it doesn't rain for tomorrow's outdoor concert.",
        "context": "Hoping for pleasant weather ahead of an open-air event.",
        "hint": "Which conditional particle pairs with いい to express a simple wish for favorable conditions (〜といい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q4": {
        "translation": "My son has been constantly begging for a new video game and is saving up his allowance.",
        "context": "Describing a third person's overt desire and visible enthusiasm.",
        "hint": "Which auxiliary expresses a third person's visible wanting for an object (〜を欲しがっている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q5": {
        "translation": "Inside the art museum, we ask visitors not to take photographs using flash.",
        "context": "Announcing museum etiquette guidelines politely.",
        "hint": "Which negative request pattern expresses a speaker's wish for others to refrain (〜ないでほしい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q6": {
        "translation": "Please definitely let me serve as the leader for this new business development project.",
        "context": "Volunteering passionately for a key career opportunity.",
        "hint": "Which imperative causative form asks a superior for permission to do the role (〜させてください)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q7": {
        "translation": "If you look that pale, don't force yourself and take work off today.",
        "context": "Giving warm, caring advice to an overextended coworker.",
        "hint": "Which conditional form is commonly used for gentle recommendations (〜たらいい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q8": {
        "translation": "The moment the needle pierced her arm, the little girl showed intense signs of pain and burst into tears.",
        "context": "Observing a young child's visible reaction to a medical vaccination.",
        "hint": "Which third-person sensory verb describes outwardly manifesting physical pain (〜を痛がって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q9": {
        "translation": "As parents, we naturally want our children to live resiliently without yielding to hardships.",
        "context": "Expressing enduring parental aspirations for their children's future.",
        "hint": "Which pattern expresses general parental wishes for others (〜ていってほしいものだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q10": {
        "translation": "I apologize for the imposition, but could you please allow me to review the financial data for the past five years?",
        "context": "Formally requesting audit access from department directors.",
        "hint": "Which respectful potential causative request asks permission for oneself (〜させていただけますでしょうか)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q11": {
        "translation": "I did my absolute best writing my exam answers. Now I just hope I will be able to pass safely.",
        "context": "Hoping for a positive result after turning in an examination.",
        "hint": "Which conditional pattern expresses personal hope for a successful outcome (〜といいのだが)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },
    "skm3-c9-q12": {
        "translation": "He always shows reluctance when asked to give public speeches, and this time too he turned down the MC role.",
        "context": "Characterizing a colleague's habitual aversion to public speaking.",
        "hint": "Which form describes a third person's outward dislike or reluctance (〜を嫌がっている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 9, Practice Drills, pp. 44–45"
    },

    # === Chapter 10 (pp. 46–49) ===
    "skm3-c10-q1": {
        "translation": "Borrowed books ought to be treated with care, without staining or tearing them.",
        "context": "Stating moral duties regarding shared library property.",
        "hint": "Which moral obligation pattern expresses what one ought to do (〜べきだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q2": {
        "translation": "(Proctor written instructions) 'Fill in your name and examinee registration number using an HB pencil.'",
        "context": "Written administrative rules on examination protocols.",
        "hint": "Which written directive pattern ends written regulations and rules (〜こと)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q3": {
        "translation": "(During soccer match) The coach shouted loudly from the bench: 'Drive the ball forward!'",
        "context": "Urgent coaching commands yelled in athletic competition.",
        "hint": "Which imperative verb form commands urgent physical action (出せ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q4": {
        "translation": "Isn't it painful to remain on bad terms with him? Why don't you try honestly apologizing to him first?",
        "context": "Gently advising a friend on reconciling after an argument.",
        "hint": "Which casual suggestion phrase invites someone to try taking an action (〜てみたらどう)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q5": {
        "translation": "According to the Meteorological Agency's announcement, a massive typhoon is expected to make landfall in the Kyushu region before dawn tomorrow.",
        "context": "Citing government weather bureau advisories.",
        "hint": "Which information source marker introduces official data (〜によると)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q6": {
        "translation": "(Sign on construction fence) 'Danger! Unauthorized personnel must absolutely not enter.'",
        "context": "Prominent hazard warning signage forbidding entry.",
        "hint": "Which strong prohibition form commands someone not to do an action (〜な)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q7": {
        "translation": "Toward a friend who helped you with all their heart, you should never have taken such a disrespectful attitude.",
        "context": "Chiding someone for past ungrateful behavior.",
        "hint": "Which past obligation pattern expresses 'should not have done' (〜べきではなかった)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q8": {
        "translation": "Instead of just complaining about how others do things, if you have that much to say, why don't you try doing it yourself?",
        "context": "Challenging a critical observer to take responsibility.",
        "hint": "Which colloquial suggestion challenges someone to give it a try (〜てみたらどうか)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q9": {
        "translation": "Corporations ought to actively invest in environmental conservation, not just in short-term profits.",
        "context": "Advocating corporate social responsibility in sustainable business.",
        "hint": "Which auxiliary attaches to する to express social duty (すべきだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q10": {
        "translation": "When I was a child, my mother used to scold me sternly: 'Don't play video games late into the night!'",
        "context": "Reminiscing about childhood parental admonitions.",
        "hint": "Which direct prohibition particle forbids an action (〜するな)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q11": {
        "translation": "(Dormitory rule) 'After 10:00 PM, do not make loud noises that would disturb other residents.'",
        "context": "Reading written behavioral guidelines in student accommodations.",
        "hint": "Which negative written instruction states rule prohibitions (〜出さないこと)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },
    "skm3-c10-q12": {
        "translation": "According to the latest industry research report, purchase rates of printed books among young people are reportedly surging.",
        "context": "Presenting market analysis data on publishing trends.",
        "hint": "Which formal source particle introduces findings (〜によれば)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 10, Practice Drills, pp. 46–49"
    },

    # === Chapter 11 (pp. 50–51) ===
    "skm3-c11-q1": {
        "translation": "The exact moment I was about to step into the bath, the telephone suddenly rang loudly.",
        "context": "Describing an interrupted action right on the verge of occurring.",
        "hint": "Which volitional construction expresses 'just on the point of doing' (〜ようとした瞬間)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q2": {
        "translation": "Even though his fault is obvious, he will not make the slightest effort to apologize to the other party.",
        "context": "Criticizing an unrepentant individual who refuses to show remorse.",
        "hint": "Which construction indicates obstinate refusal or lack of willingness (〜ようとしない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q3": {
        "translation": "To prevent lifestyle-related diseases, I make a continuous effort to use the stairs every morning without taking the elevator.",
        "context": "Explaining daily conscious health habits.",
        "hint": "Which pattern indicates making an active ongoing effort toward a habit (〜ようにしている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q4": {
        "translation": "No matter how busy work gets, I make it my personal rule to spend weekends with my family.",
        "context": "Sharing established lifestyle balance routines.",
        "hint": "Which pattern denotes an established personal rule or conscious decision (〜ことにしている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q5": {
        "translation": "I myself believed I had sung quite well, but when I listened back to the recording, my pitch was completely off.",
        "context": "Discovering a gap between subjective impression and objective performance.",
        "hint": "Which noun expresses subjective belief or intention that proved mistaken (〜たつもり)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q6": {
        "translation": "Just as I was about to power down the computer, the screen suddenly went pitch black and froze.",
        "context": "Recounting sudden electronic malfunction during shutdown.",
        "hint": "Which volitional phrase means 'was just attempting to turn off' (〜切ろうとしたら)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q7": {
        "translation": "No matter how cluttered the room gets, my younger brother refuses to clean up on his own.",
        "context": "Complaining about a sibling's persistent refusal to tidy up.",
        "hint": "Which negative volitional phrase indicates zero willingness to clean (〜掃除をしようとしない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q8": {
        "translation": "This is an important contract document, so please ensure that there are no typographical errors or omissions.",
        "context": "Instructing an assistant to check legal paperwork carefully.",
        "hint": "Which phrase asks someone to take care that a negative condition does not occur (〜ないようにしてください)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q9": {
        "translation": "For the sake of health management, since becoming a freelancer I have made it a rule never to accept all-night assignments.",
        "context": "Stating professional boundaries to preserve personal health.",
        "hint": "Which pattern denotes a conscious personal policy of non-action (〜引き受けないことにしている)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q10": {
        "translation": "Words that I had intended merely as light advice ended up deeply wounding her feelings.",
        "context": "Regretting an unintended emotional hurt caused by careless phrasing.",
        "hint": "Which phrase describes an intended meaning that misfired (〜のつもりで言った)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q11": {
        "translation": "When I attempted to lift the heavy parcel all by myself, I suddenly threw out my lower back.",
        "context": "Explaining an acute physical injury while handling freight.",
        "hint": "Which volitional auxiliary expresses the moment of initiating physical strain (〜持ち上げようとしたら)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },
    "skm3-c11-q12": {
        "translation": "You may think you can resolve everything single-handedly, but you also need help from those around you.",
        "context": "Reminding an independent person not to isolate themselves from team support.",
        "hint": "Which noun conveys subjective self-conception or presumption (〜つもりかもしれない)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 11, Practice Drills, pp. 50–51"
    },

    # === Chapter 12 (pp. 52–55) ===
    "skm3-c12-q1": {
        "translation": "President, President Tanaka of Company A arrived in the lobby a moment ago. Shall I escort him to the reception room?",
        "context": "Notifying the company president of an executive guest's arrival.",
        "hint": "Which respectful honorific verb expresses the arrival of an esteemed visitor (お見えになりました)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q2": {
        "translation": "Professor, shall I carry that heavy-looking baggage for you?",
        "context": "Offering humble assistance to an academic advisor.",
        "hint": "Which humble auxiliary pattern offers one's service to a superior (お〜しましょうか)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q3": {
        "translation": "Nice to meet you. I am called Taro Yamada. I look forward to working with you today.",
        "context": "Self-introduction at an initial formal business meeting.",
        "hint": "Which humble kenjougo verb is used to state one's own name (申します)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q4": {
        "translation": "Professor, have you already had lunch? If you like, would you care to join me?",
        "context": "Politely inquiring about a teacher's dining status.",
        "hint": "Which respectful sonkeigo verb means to eat or drink (召し上がりました)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q5": {
        "translation": "I would like to visit your company's head office at 3:00 PM tomorrow.",
        "context": "Scheduling a formal business call with a client.",
        "hint": "Which humble kenjougo verb denotes visiting a client's location (伺いたい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q6": {
        "translation": "(Telephone reception to outside caller) 'Unfortunately, our president is away from his desk at the moment.'",
        "context": "Answering an outside customer inquiry regarding executive availability.",
        "hint": "Which humble phrasing reports an insider's temporary absence to outsiders (席を外しております)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q7": {
        "translation": "Please take a look at our latest product catalog.",
        "context": "Offering sales literature politely to a prospective customer.",
        "hint": "Which respectful honorific expression asks someone to look (ご覧ください)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q8": {
        "translation": "I had the privilege of reviewing the proposal you sent yesterday right away; it is of excellent quality.",
        "context": "Praising a client's submitted project documentation.",
        "hint": "Which humble kenjougo verb expresses reading or viewing a superior's document (拝見しました)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q9": {
        "translation": "We currently have ample stock in our warehouse. Shipment is possible tomorrow.",
        "context": "Providing order fulfillment confirmation to a purchasing client.",
        "hint": "Which polite teineigo verb substitutes for あります in formal service (ございます)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q10": {
        "translation": "Professor, will you be in your research office tomorrow afternoon?",
        "context": "Checking faculty availability before scheduling an academic consultation.",
        "hint": "Which respectful sonkeigo verb expresses being present or staying (いらっしゃる)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q11": {
        "translation": "Because it is an essential package, I will personally deliver it first thing tomorrow morning.",
        "context": "Promising personal delivery of critical corporate shipments.",
        "hint": "Which humble verb structure expresses personal delivery service (お届けします)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },
    "skm3-c12-q12": {
        "translation": "The restrooms are located at the end of the hallway after turning right.",
        "context": "Providing facility directions gracefully to office visitors.",
        "hint": "Which polite copular form gives courteous location directions (ございます)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Chapter 12, Practice Drills, pp. 52–55"
    },

    # === Form Review A (pp. 58–61) ===
    "skm3-fa-q1": {
        "translation": "There are still 30 minutes until the next train arrives, so shall we drink some coffee or something at the cafe in front of the station while we wait?",
        "context": "Suggesting a light beverage option to pass time comfortably.",
        "hint": "Which particle offers a representative, casual suggestion (コーヒーでも)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q2": {
        "translation": "I swore firmly in my heart that this year without fail I would pass the JLPT N3.",
        "context": "Strengthening personal resolve for an annual milestone goal.",
        "hint": "Which emphatic particle underscores a specific point in time with determination (今年こそ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q3": {
        "translation": "This math problem is so overly simple that even an elementary school student can solve it immediately.",
        "context": "Highlighting an extreme minimum baseline to show extreme ease.",
        "hint": "Which compound particle emphasizes an extreme baseline example (〜でさえ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q4": {
        "translation": "In the violent storm, even sturdy giant trees were toppled from their roots.",
        "context": "Describing extensive typhoon damage uprooting massive trees.",
        "hint": "Which particle denotes an extreme extent reaching unexpectedly far (大木まで)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q5": {
        "translation": "At least take the dishes you ate from to the sink yourself and wash them.",
        "context": "Admonishing a family member to fulfill minimal household courtesy.",
        "hint": "Which particle denotes a minimal baseline expectation of effort (食器くらい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q6": {
        "translation": "I feel truly humbled that an inexperienced person like myself should receive such a prestigious award.",
        "context": "Expressing deep modesty in an awards acceptance speech.",
        "hint": "Which humble particle downplays oneself respectfully (私なんか)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q7": {
        "translation": "There is absolutely no need to pay any mind to baseless rumors like that.",
        "context": "Reassuring a colleague not to be troubled by unfounded office talk.",
        "hint": "Which dismissive particle downplays trivial or gossip topics (噂話なんて)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q8": {
        "translation": "I am always grateful for your assistance. It is I who must express my gratitude to you.",
        "context": "Reciprocating appreciation graciously in mutual cooperation.",
        "hint": "Which emphatic focus particle redirects gratitude back to oneself (こちらこそ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q9": {
        "translation": "Even though we work in the same office every day, I don't even know the name of the person sitting next to me.",
        "context": "Remarking on modern workplace social distance.",
        "hint": "Which particle expresses an extreme baseline negative ('not even...') (名前さえ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q10": {
        "translation": "One ought to exchange basic greetings properly, no matter how bad a mood one is in.",
        "context": "Emphasizing elementary interpersonal courtesy in social settings.",
        "hint": "Which particle specifies minimum baseline standards (挨拶ぐらい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q11": {
        "translation": "After the meal, if you would care for it, wouldn't you like to enjoy some seasonal fruit or something?",
        "context": "Hospitably offering a dessert option to dining guests.",
        "hint": "Which particle presents a polite culinary suggestion (フルーツでも)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },
    "skm3-fa-q12": {
        "translation": "That smash-hit song is hummed not only by young people, but even by 80-year-old grandfathers.",
        "context": "Illustrating cross-generational cultural penetration of music.",
        "hint": "Which particle highlights an extreme demographic reached (おじいちゃんまで)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review A, Practice Drills, pp. 58–61"
    },

    # === Form Review B (pp. 62–65) ===
    "skm3-fb-q1": {
        "translation": "For learners of Japanese, mastering kanji is one of the greatest hurdles that cannot be avoided.",
        "context": "Analyzing foreign language acquisition challenges from the learner's standpoint.",
        "hint": "Which compound particle expresses 'from the perspective/standpoint of' (〜にとって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q2": {
        "translation": "He was invited to the United Nations international symposium in his capacity as a specialist in environmental issues.",
        "context": "Introducing a keynote speaker's professional qualification and role.",
        "hint": "Which compound particle denotes capacity, status, or title (〜として)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q3": {
        "translation": "The novel 'Botchan' was penned by the Meiji-era literary giant Natsume Soseki.",
        "context": "Stating the authorial agent in a passive literary attribution.",
        "hint": "Which passive agent marker indicates the creator of artistic works (〜によって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q4": {
        "translation": "The store clerk responded calmly, no matter how unreasonable the customer making the complaint was.",
        "context": "Describing professional retail customer service under stress.",
        "hint": "Which compound particle indicates the target or recipient of an attitude (〜に対して)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q5": {
        "translation": "In today's seminar, I will deliver a presentation regarding the history of kabuki, Japan's traditional performing art.",
        "context": "Announcing the academic topic of an oral presentation.",
        "hint": "Which compound particle introduces a theme or subject matter (〜について)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q6": {
        "translation": "The flavoring of New Year's zoni soup varies according to the region, featuring miso broth in some places and soy sauce broth in others.",
        "context": "Explaining regional cultural variations in traditional holiday dishes.",
        "hint": "Which compound particle means 'depending on / according to' (〜によって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q7": {
        "translation": "It might look like mere junk to others, but to me it is an irreplaceable personal treasure.",
        "context": "Expressing sentimental valuation from one's personal perspective.",
        "hint": "Which compound particle establishes personal subjective evaluation (私にとって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q8": {
        "translation": "In contrast to the older brother being outgoing and having many friends, the younger brother is introverted and prefers reading alone.",
        "context": "Contrasting two siblings' differing temperaments directly.",
        "hint": "Which contrastive marker highlights opposing traits (〜のに対して)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q9": {
        "translation": "Nowadays people don't carry paper dictionaries around, utilizing their smartphones in lieu of electronic dictionaries.",
        "context": "Describing technology adoption replacing traditional study tools.",
        "hint": "Which particle denotes the role or function served (代わりとして)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q10": {
        "translation": "When the tax hike policy was announced, criticism directed at the government's economic measures surged sharply in opinion polls.",
        "context": "Reporting public sentiment and political critiques.",
        "hint": "Which prenominal form modifies a noun to indicate target of criticism (〜に対する)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q11": {
        "translation": "Due to last night's severe heavy snowfall, the railway network across the capital area was completely paralyzed this morning.",
        "context": "Explaining meteorological cause and resulting transportation chaos.",
        "hint": "Which formal causal compound particle indicates an external cause (〜によって)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },
    "skm3-fb-q12": {
        "translation": "The marketing department conducted a detailed questionnaire survey regarding consumer trends among youth.",
        "context": "Outlining corporate research initiatives on generational buying patterns.",
        "hint": "Which prenominal form modifies a noun to specify the research topic (〜についての)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review B, Practice Drills, pp. 62–65"
    },

    # === Form Review C (pp. 66–69) ===
    "skm3-fc-q1": {
        "translation": "When I looked up at the night sky, I saw a beautiful shooting star smoothly streaking across.",
        "context": "Describing a direct sensory visual observation of rapid motion.",
        "hint": "Which nominalizer is required for direct visual perception verbs like 見る (流れていくのを見た)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q2": {
        "translation": "My long-cherished dream is to travel across the globe and interact with people of diverse cultures.",
        "context": "Stating an abstract personal aspiration or life goal.",
        "hint": "Which nominalizer is required for predicate definitions of dreams and goals (〜ことです)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q3": {
        "translation": "Thanks to sprinting with all my might to the ticket gates I made it, but I was on the very brink of missing the last train.",
        "context": "Recounting a close shave with missing late-night transit.",
        "hint": "Which temporal noun phrase denotes almost reaching an undesirable event (〜ところだった)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q4": {
        "translation": "Being able to transfer money 24 hours a day on a smartphone without lining up at a bank teller counter is truly convenient.",
        "context": "Evaluating digital banking advantages.",
        "hint": "Which nominalizer is standard when evaluating practical convenience of actions (〜のは便利だ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q5": {
        "translation": "When I first began studying Japanese was during summer vacation in my first year of high school.",
        "context": "Reflecting on the historical starting point of one's language journey.",
        "hint": "Which nominalizer pairs with focus structures emphasizing time (〜始めたのは)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q6": {
        "translation": "Because I was walking while looking down at my smartphone, I came within inches of colliding into a telephone pole.",
        "context": "Warning about the physical hazards of distracted smartphone walking.",
        "hint": "Which non-past verb collocation expresses narrowly averting an accident (ぶつかるところだった)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q7": {
        "translation": "Since it's a scorching midsummer afternoon, let's buy something cold from the vending machine and drink it.",
        "context": "Seeking cold refreshments on a hot day.",
        "hint": "Which tangible noun refers to a physical beverage item (冷たいもの)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q8": {
        "translation": "In the quiet night, I could hear a man and woman quarreling loudly and fiercely in the next room.",
        "context": "Noticing auditory disturbances through apartment walls.",
        "hint": "Which nominalizer is required for auditory perception verbs like 聞こえる (〜のを/が聞こえた)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q9": {
        "translation": "The foremost distinctive feature of this restaurant is that it exclusively uses organic produce.",
        "context": "Describing restaurant culinary commitments.",
        "hint": "Which nominalizer defines characteristics or structural features in predicates (〜ことだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q10": {
        "translation": "I typed one digit of the recipient account number wrong and almost transferred money to a complete stranger.",
        "context": "Confessing a near-disaster during mobile wire transfers.",
        "hint": "Which phrase marks almost making a critical financial error (〜ところだった)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q11": {
        "translation": "When learning a foreign language, acquiring native-level natural pronunciation is exceptionally challenging.",
        "context": "Discussing phonetic difficulties in second language acquisition.",
        "hint": "Which nominalizer is commonly used with difficulty adjectives like 難しい (〜のは難しい)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },
    "skm3-fc-q12": {
        "translation": "As I was dozing off after getting into bed, I felt the entire house shaking slightly.",
        "context": "Sensing early minor tremors of an earthquake while half-asleep.",
        "hint": "Which nominalizer is required for physical sensory perceptions like 感じる (〜のを感じた)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review C, Practice Drills, pp. 66–69"
    },

    # === Form Review D (pp. 70–73) ===
    "skm3-fd-q1": {
        "translation": "We prepared multilingual audio guides so that foreign tourists could also understand the exhibition content thoroughly.",
        "context": "Improving museum accessibility for international visitors.",
        "hint": "Which non-volitional potential verb pairs with ように to state a purpose (分かるように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q2": {
        "translation": "Even though it is midwinter, the sunlight is pleasantly warm as if spring had already arrived.",
        "context": "Marveling at unusually balmy winter weather.",
        "hint": "Which simile pattern pairs with まるで to express 'as though' (まるで〜たようだ)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q3": {
        "translation": "After my health checkup, the physician strictly instructed me to 'make sure to walk for 30 minutes every day.'",
        "context": "Relaying medical advice and health regimens.",
        "hint": "Which verb form pairs with 〜ようにと指導された to report medical instructions (散歩をするように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q4": {
        "translation": "At the shrine for the New Year visit, all family members clapped their hands and prayed that we could spend this whole year in good health and safety.",
        "context": "Offering traditional New Year prayers for family wellbeing.",
        "hint": "Which polite potential form pairs with 〜ようにと祈る to express religious prayers (過ごせますように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q5": {
        "translation": "I took careful notes in my planner so that I would not forget important announcements later.",
        "context": "Taking precautions against memory lapses with scheduling notes.",
        "hint": "Which negative verb form expresses purposeful prevention (忘れないように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q6": {
        "translation": "As you are all already aware, renovation work on our offices will commence starting next month.",
        "context": "Giving polite corporate announcements referencing shared background knowledge.",
        "hint": "Which polite honorific phrase means 'as you all know' (ご存知のように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q7": {
        "translation": "The natural mountain spring water was as ice-cold and crystal clear as if it were actual ice.",
        "context": "Describing refreshing, frigid mountain streams.",
        "hint": "Which noun attaches directly with のように to form a simile comparison (氷のように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q8": {
        "translation": "I adjusted the focus of the telescope meticulously so that the distant landscape could be seen clearly.",
        "context": "Calibrating optical equipment for astronomy or nature observation.",
        "hint": "Which spontaneous visual potential verb pairs with ように (見えるように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q9": {
        "translation": "The teacher instructed the students to submit their homework first thing tomorrow morning.",
        "context": "Quoting classroom assignment deadlines set by instructors.",
        "hint": "Which dictionary verb form pairs with 〜ように指示した for relayed directives (提出するように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q10": {
        "translation": "Thanks to persisting with shadowing exercises every day, I became able to comprehend Japanese spoken at natural speed.",
        "context": "Reflecting on progressive listening skill improvements.",
        "hint": "Which potential verb form pairs with 〜ようになった to mark newly achieved capability (聞き取れるようになった)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q11": {
        "translation": "To avoid catching a cold, I thoroughly wash my hands and gargle immediately upon returning home.",
        "context": "Describing seasonal preventative hygiene habits.",
        "hint": "Which negative verb collocation expresses preventative intent (風邪をひかないように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    },
    "skm3-fd-q12": {
        "translation": "In both how he walks and how he speaks, he is the spitting image of his father.",
        "context": "Noting uncanny physical and mannerism resemblances between father and son.",
        "hint": "Which noun-modifying simile particle means 'just like father' (お父さんのように)?",
        "evidence": "Shin Kanzen Master N3 Bunpou, Part 1 Form Review D, Practice Drills, pp. 70–73"
    }
}

updated = 0
for e in exercises:
    eid = e.get("id")
    if eid in REPAIRS:
        r = REPAIRS[eid]
        e["translation"] = r["translation"]
        e["context"] = r["context"]
        e["hint"] = r["hint"]
        e["provenance"] = "source-derived"
        e["sourceEvidence"] = r["evidence"]
        updated += 1

print(f"Repaired {updated} SKM N3 Part 1 exercises.")

with open(EXERCISES_PATH, "w", encoding="utf-8") as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print("Updated chapterExercises.json successfully.")
