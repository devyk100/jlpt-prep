import json

with open('jlpt-exam-prep/src/data/studyPoints.json', 'r', encoding='utf-8') as f:
    sp_list = json.load(f)

for card in sp_list:
    if card['id'] == 'skm2-c15-kuse-ni':
        print("=== POST-ASSEMBLY skm2-c15-kuse-ni ===")
        print("Nuance:", card.get('nuance'))
        print("KeyTakeaway:", card.get('keyTakeaway'))
        assert "must share the same subject" not in card.get('nuance')
        assert "SPEAKER'S BLAME & USAGE TENDENCY" in card.get('nuance')
        print("  ✓ kuse-ni check PASSED!")
    elif card['id'] == 'g2-l14-tara-dou-desu-ka':
        print("=== POST-ASSEMBLY g2-l14-tara-dou-desu-ka ===")
        print("Nuance:", card.get('nuance'))
        print("KeyTakeaway:", card.get('keyTakeaway'))
        assert "INVITATION BAN: NEVER use" not in card.get('nuance')
        assert "PRAGMATIC USE & INVITATION CONVENTION" in card.get('nuance')
        print("  ✓ tara-dou-desu-ka check PASSED!")

print("\nALL POST-ASSEMBLY CHECKS PASSED CLEANLY!")
