with open('jlpt-exam-prep/scripts/repair_skm2_part1_b.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '"skm2-p1-c26-q12"' in line:
        # line i+2 is the opt_reasons dict
        lines[i+2] = lines[i+2].rstrip()
        if not lines[i+2].endswith(')'):
            lines[i+2] = lines[i+2] + ')\n'
        break

with open('jlpt-exam-prep/scripts/repair_skm2_part1_b.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Successfully patched repair_skm2_part1_b.py')
