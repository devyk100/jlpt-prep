"""
verify_star_marks.py
Comprehensive verification script for JLPT Question 2 Star-Mark (文の組み立て) exercises.

Validates:
1. Slot structure: prompt question contains exactly 4 slots with ★ in slot 3 (＿＿ ＿＿ ★ ＿＿).
2. Permutation: scrambleOrder is a strictly valid permutation of [1, 2, 3, 4].
3. Keyed Option: correctIndex corresponds exactly to the 3rd slot (scrambleOrder[2] - 1).
4. Exact String Reconstruction: prefix + ordered fragments + suffix matches reconstructedSentence.
5. Explanation Alignment:
   - explanation.options text matches options text exactly.
   - correct option has isCorrect == True, all other 3 have isCorrect == False.
   - reasons contain specific linguistic rationale without generic templates.

Includes 10 deliberately broken test fixtures proving that each check rejects invalid data.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXERCISES_FILE = ROOT / "src/data/chapterExercises.json"

GENERIC_TEMPLATES = [
    "語用論的制約に反します", "文脈上の時間関係", "文体・語用論", "文脈上の意味論",
    "モダリティ・感情表現の制約に反します", "文の組み立て・構造的呼応に反します",
    "文脈上の文型体系・機能制約に反します", "文体・語用論・結束性において不適切です"
]

class StarMarkValidationError(Exception):
    """Custom exception raised when star-mark validation fails."""
    pass

def validate_star_mark_exercise(exercise: dict) -> None:
    """
    Validates a single star-mark exercise against strict structural,
    permutation, reconstruction, keying, and explanation criteria.
    Raises StarMarkValidationError on any defect.
    """
    eid = exercise.get("id", "UNKNOWN")

    # 1. Type check
    if exercise.get("type") != "star-mark":
        raise StarMarkValidationError(f"[{eid}] Exercise type must be 'star-mark', got '{exercise.get('type')}'")

    # 2. Options list
    options = exercise.get("options", [])
    if not isinstance(options, list) or len(options) != 4:
        raise StarMarkValidationError(f"[{eid}] 'options' must be a list of exactly 4 items, got: {options}")

    for idx, opt in enumerate(options):
        if not isinstance(opt, str) or not opt.strip():
            raise StarMarkValidationError(f"[{eid}] Option {idx} is empty or non-string: {opt}")

    # 3. Permutation check for scrambleOrder
    order = exercise.get("scrambleOrder")
    if not isinstance(order, list):
        raise StarMarkValidationError(f"[{eid}] 'scrambleOrder' must be a list, got: {type(order)}")
    if len(order) != 4:
        raise StarMarkValidationError(f"[{eid}] 'scrambleOrder' must have length 4, got length {len(order)}: {order}")
    if sorted(order) != [1, 2, 3, 4]:
        raise StarMarkValidationError(f"[{eid}] 'scrambleOrder' must be a permutation of [1, 2, 3, 4], got: {order}")

    # 4. Slot structure & Star position in prompt question
    question = exercise.get("question", "")
    if not isinstance(question, str) or not question.strip():
        raise StarMarkValidationError(f"[{eid}] 'question' is empty or non-string")

    # Match standard JLPT 4-slot pattern: slot1 slot2 ★ slot4
    slot_pattern = re.search(r"＿＿\s*＿＿\s*★\s*＿＿", question)
    if not slot_pattern:
        raise StarMarkValidationError(
            f"[{eid}] Question prompt does not contain standard 4-slot pattern with ★ in slot 3 (＿＿ ＿＿ ★ ＿＿): '{question}'"
        )

    # 5. Keyed option correspondence
    correct_index = exercise.get("correctIndex")
    if not isinstance(correct_index, int) or correct_index < 0 or correct_index >= 4:
        raise StarMarkValidationError(f"[{eid}] 'correctIndex' must be an integer in 0..3, got: {correct_index}")

    # In slot 3 (index 2 of the 4 slots), the required option is order[2]
    # Since order is 1-based, 0-based option index is order[2] - 1
    expected_correct_index = order[2] - 1
    if correct_index != expected_correct_index:
        raise StarMarkValidationError(
            f"[{eid}] Keyed option mismatch: correctIndex is {correct_index} ('{options[correct_index]}'), "
            f"but slot 3 (★) has option {expected_correct_index} ('{options[expected_correct_index]}') based on scrambleOrder {order}"
        )

    # 6. Exact String Reconstruction
    prefix = question[:slot_pattern.start()].strip()
    suffix = question[slot_pattern.end():].strip()
    ordered_fragments = [options[pos - 1] for pos in order]
    assembled_sentence = prefix + "".join(ordered_fragments) + suffix

    reconstructed_sentence = exercise.get("reconstructedSentence", "")
    if not isinstance(reconstructed_sentence, str) or not reconstructed_sentence.strip():
        raise StarMarkValidationError(f"[{eid}] 'reconstructedSentence' is missing or empty")

    if assembled_sentence != reconstructed_sentence:
        raise StarMarkValidationError(
            f"[{eid}] Exact reconstruction mismatch:\n"
            f"  Assembled from prompt & ordered fragments: '{assembled_sentence}'\n"
            f"  Stored reconstructedSentence:              '{reconstructed_sentence}'"
        )

    # 7. Translation check
    translation = exercise.get("translation", "").strip()
    if not translation:
        raise StarMarkValidationError(f"[{eid}] Translation is missing or empty")
    if translation == question or translation == reconstructed_sentence:
        raise StarMarkValidationError(f"[{eid}] Translation is a placeholder matching question or sentence")

    # 8. Explanation options alignment
    explanation = exercise.get("explanation", {})
    if not isinstance(explanation, dict):
        raise StarMarkValidationError(f"[{eid}] 'explanation' must be a dict")

    expl_options = explanation.get("options", [])
    if not isinstance(expl_options, list) or len(expl_options) != 4:
        raise StarMarkValidationError(f"[{eid}] 'explanation.options' must have exactly 4 items, got {len(expl_options)}")

    for i in range(4):
        eo = expl_options[i]
        # Text alignment
        if eo.get("text") != options[i]:
            raise StarMarkValidationError(
                f"[{eid}] Option {i} text mismatch: explanation has '{eo.get('text')}' but options has '{options[i]}'"
            )
        # Correctness alignment
        is_corr = eo.get("isCorrect")
        if i == correct_index:
            if is_corr is not True:
                raise StarMarkValidationError(f"[{eid}] Explanation option {i} (correctIndex) must have isCorrect == True")
        else:
            if is_corr is not False:
                raise StarMarkValidationError(f"[{eid}] Explanation option {i} (distractor) must have isCorrect == False")

        # Distractor reason check
        reason = eo.get("reason", "")
        if not reason or not reason.strip():
            raise StarMarkValidationError(f"[{eid}] Option {i} explanation reason is empty")
        for bad_tmpl in GENERIC_TEMPLATES:
            if bad_tmpl in reason:
                raise StarMarkValidationError(
                    f"[{eid}] Option {i} contains generic template reason '{bad_tmpl}': {reason}"
                )


# ==============================================================================
# DELIBERATELY BROKEN TEST FIXTURES
# ==============================================================================

VALID_SAMPLE = {
    "id": "fixture-valid",
    "type": "star-mark",
    "question": "課長に、電車の ＿＿ ＿＿ ★ ＿＿ 伝えていただけますか。",
    "translation": "Could you please tell the section manager that I will be late due to a train delay?",
    "options": ["遅延で", "10分ほど", "遅れる", "と"],
    "correctIndex": 2,
    "scrambleOrder": [1, 2, 3, 4],
    "reconstructedSentence": "課長に、電車の遅延で10分ほど遅れると伝えていただけますか。",
    "explanation": {
        "overall": "文末の「伝えていただけますか」に呼応して、発言内容を引用する構造を作ります。",
        "options": [
            {"text": "遅延で", "isCorrect": False, "reason": "1番目の要素。遅刻の理由を示します。"},
            {"text": "10分ほど", "isCorrect": False, "reason": "2番目の要素。遅れる時間を指定します。"},
            {"text": "遅れる", "isCorrect": True, "reason": "【正解（★・3番目）】引用助詞「と」の直前に置く述語普通形です。"},
            {"text": "と", "isCorrect": False, "reason": "4番目の要素。引用格助詞です。"}
        ]
    }
}

BROKEN_FIXTURES = [
    # 1. Non-permutation: duplicate number
    ({**VALID_SAMPLE, "id": "fix-1-dup-order", "scrambleOrder": [1, 2, 2, 4]},
     "permutation"),

    # 2. Non-permutation: wrong length
    ({**VALID_SAMPLE, "id": "fix-2-short-order", "scrambleOrder": [1, 2, 3]},
     "length 4"),

    # 3. Non-permutation: out of range number
    ({**VALID_SAMPLE, "id": "fix-3-out-of-range", "scrambleOrder": [1, 2, 3, 5]},
     "permutation"),

    # 4. Question missing star slot
    ({**VALID_SAMPLE, "id": "fix-4-missing-star", "question": "課長に、電車の ＿＿ ＿＿ ＿＿ ＿＿ 伝えていただけますか。"},
     "standard 4-slot pattern with ★"),

    # 5. Star at wrong slot (slot 2 instead of slot 3)
    ({**VALID_SAMPLE, "id": "fix-5-star-slot-2", "question": "課長に、電車の ＿＿ ★ ＿＿ ＿＿ 伝えていただけますか。"},
     "standard 4-slot pattern with ★ in slot 3"),

    # 6. Keyed option mismatch (correctIndex doesn't point to slot 3)
    ({**VALID_SAMPLE, "id": "fix-6-wrong-correct-index", "correctIndex": 0},
     "Keyed option mismatch"),

    # 7. Exact reconstruction mismatch (assembled differs from reconstructedSentence)
    ({**VALID_SAMPLE, "id": "fix-7-recon-mismatch", "reconstructedSentence": "課長に、電車の遅延で20分ほど遅れると伝えていただけますか。"},
     "Exact reconstruction mismatch"),

    # 8. Explanation isCorrect flag mismatch (distractor has isCorrect=True)
    ({**VALID_SAMPLE, "id": "fix-8-wrong-is-correct", "explanation": {
        "overall": "test",
        "options": [
            {"text": "遅延で", "isCorrect": False, "reason": "r1"},
            {"text": "10分ほど", "isCorrect": True, "reason": "r2"},
            {"text": "遅れる", "isCorrect": False, "reason": "r3"},
            {"text": "と", "isCorrect": False, "reason": "r4"}
        ]
    }}, "must have isCorrect == False"),

    # 9. Explanation option text mismatch
    ({**VALID_SAMPLE, "id": "fix-9-text-mismatch", "explanation": {
        "overall": "test",
        "options": [
            {"text": "バスの遅延で", "isCorrect": False, "reason": "r1"},
            {"text": "10分ほど", "isCorrect": False, "reason": "r2"},
            {"text": "遅れる", "isCorrect": True, "reason": "r3"},
            {"text": "と", "isCorrect": False, "reason": "r4"}
        ]
    }}, "Option 0 text mismatch"),

    # 10. Generic distractor template in reason
    ({**VALID_SAMPLE, "id": "fix-10-generic-reason", "explanation": {
        "overall": "test",
        "options": [
            {"text": "遅延で", "isCorrect": False, "reason": "【不正解】文体・語用論・結束性において不適切です。"},
            {"text": "10分ほど", "isCorrect": False, "reason": "r2"},
            {"text": "遅れる", "isCorrect": True, "reason": "r3"},
            {"text": "と", "isCorrect": False, "reason": "r4"}
        ]
    }}, "contains generic template reason")
]


def run_fixtures_test():
    print("=" * 60)
    print("RUNNING DELIBERATELY BROKEN TEST FIXTURES...")
    print("=" * 60)

    # First verify valid sample passes cleanly
    try:
        validate_star_mark_exercise(VALID_SAMPLE)
        print("  ✓ VALID_SAMPLE passed cleanly as expected.")
    except Exception as e:
        print(f"  ✗ FAILED: VALID_SAMPLE raised unexpected exception: {e}")
        return False

    # Now verify all 10 broken fixtures are rejected
    passed_fixtures = 0
    for idx, (broken, expected_err_sub) in enumerate(BROKEN_FIXTURES, 1):
        try:
            validate_star_mark_exercise(broken)
            print(f"  ✗ FAILED: Fixture {idx} ({broken['id']}) was unexpectedly accepted!")
        except StarMarkValidationError as e:
            if expected_err_sub in str(e):
                print(f"  ✓ Fixture {idx} rejected as expected ({broken['id']}): {expected_err_sub}")
                passed_fixtures += 1
            else:
                print(f"  ✗ Fixture {idx} failed with unexpected error message: '{e}', expected substring '{expected_err_sub}'")
        except Exception as e:
            print(f"  ✗ Fixture {idx} raised unexpected exception type {type(e)}: {e}")

    print(f"\nFixtures test result: {passed_fixtures} / {len(BROKEN_FIXTURES)} broken fixtures rejected cleanly.\n")
    return passed_fixtures == len(BROKEN_FIXTURES)


def main():
    # 1. Run negative fixtures test
    fixtures_ok = run_fixtures_test()
    if not fixtures_ok:
        print("ERROR: Deliberately broken test fixtures suite failed!")
        return 1

    # 2. Run on production dataset
    print("=" * 60)
    print("RUNNING VALIDATION ON PRODUCTION DATASET...")
    print("=" * 60)
    with open(EXERCISES_FILE, "r", encoding="utf-8") as f:
        exercises = json.load(f)

    stars = [e for e in exercises if e.get("type") == "star-mark"]
    print(f"Found {len(stars)} star-mark exercises in {EXERCISES_FILE.name}.\n")

    errors = []
    for s in stars:
        try:
            validate_star_mark_exercise(s)
        except StarMarkValidationError as err:
            errors.append((s["id"], str(err)))

    if errors:
        print(f"FAILED: Found {len(errors)} validation errors among {len(stars)} exercises:")
        for eid, msg in errors:
            print(f"  • {eid}: {msg}")
        return 1
    else:
        print(f"SUCCESS: All {len(stars)} star-mark exercises passed all structural, permutation,")
        print("exact reconstruction, keyed option, and explanation alignment checks!")
        print("\nNote: Automated checks establish structural, permutation, and keying validity.")
        print("Pedagogical appropriateness and ordering ambiguity require separate linguistic review.")
        return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
