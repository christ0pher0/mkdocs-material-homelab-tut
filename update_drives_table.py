#!/usr/bin/env python3
"""
update_drives_table.py
Updates backup_drives.md:
- Updates Used/Free/SMART/Backup columns from stats files for mounted drives
- Leaves existing values unchanged for unmounted drives (no stats file)
- Removes duplicate label entries
- Sorts all table rows alphabetically by label
Usage: python3 update_drives_table.py <doc_file> <stats_dir>
"""
import sys
import os
doc_file = sys.argv[1]
stats_dir = sys.argv[2]
# Load stats from txt files
stats = {}
for fname in os.listdir(stats_dir):
    if not fname.endswith('.txt'):
        continue
    label = fname[:-4]
    path = os.path.join(stats_dir, fname)
    used = total = free = smart = backup = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('===') and line.endswith('==='):
                # Header line: "=== <label> - <date output> ==="
                inner = line.strip('=').strip()
                if ' - ' in inner:
                    date_part = inner.split(' - ', 1)[1].strip()
                    parts = date_part.split()
                    # bash `date` default: Sun Jul  6 09:15:23 EDT 2026
                    if len(parts) >= 2:
                        month = parts[1]
                        year = parts[-1]
                        backup = f'{month} {year}'
            elif 'used /' in line and 'total' in line:
                parts = line.split()
                if len(parts) >= 7 and 'free' in line:
                    # New format: "4.6T used / 886G free / 5.5T total"
                    used = parts[0]
                    free = parts[3]
                    total = parts[6]
                elif len(parts) >= 4:
                    # Old format: "2.1T used / 2.8T total"
                    used = parts[0]
                    total = parts[3]
                    free = '—'
            elif line.startswith('SMART:'):
                raw = line.split(':', 1)[1].strip()
                if raw == 'PASS':
                    smart = '✅'
                elif raw == 'FAIL':
                    smart = '❌'
                else:
                    smart = '⚠️'
    if used and total:
        stats[label] = {
            'used': used,
            'free': free or '—',
            'total': total,
            'smart': smart or '—',
            'backup': backup
        }
with open(doc_file, 'r') as f:
    lines = f.readlines()
result = []
i = 0
while i < len(lines):
    line = lines[i]
    # Detect table header
    if line.startswith('| Label |') or line.startswith('| # | Label |'):
        header = line
        header_cols = [c.strip().lower() for c in header.split('|')]
        # Collect separator
        i += 1
        separator = lines[i] if i < len(lines) else ''
        # Collect data rows
        i += 1
        data_rows = []
        seen_labels = set()
        while i < len(lines) and lines[i].startswith('|'):
            row = lines[i]
            cols = row.split('|')
            try:
                label_idx = header_cols.index('label')
            except ValueError:
                label_idx = 2
            label = cols[label_idx].strip() if len(cols) > label_idx else ''
            # Skip duplicates
            if label and label in seen_labels:
                print(f"Removed duplicate: {label}")
                i += 1
                continue
            if label:
                seen_labels.add(label)
            # Only update if we have fresh stats — otherwise leave existing values alone
            if label in stats:
                s = stats[label]
                try:
                    used_idx = header_cols.index('used')
                    cols[used_idx] = f' {s["used"]} '
                except ValueError:
                    pass
                try:
                    free_idx = header_cols.index('free')
                    cols[free_idx] = f' {s["free"]} '
                except ValueError:
                    pass
                try:
                    smart_idx = header_cols.index('smart')
                    cols[smart_idx] = f' {s["smart"]} '
                except ValueError:
                    pass
                if s.get('backup'):
                    try:
                        backup_idx = header_cols.index('backup')
                        cols[backup_idx] = f' {s["backup"]} '
                    except ValueError:
                        pass
                row = '|'.join(cols)
                print(f"Updated: {label}")
            else:
                if label:
                    print(f"No stats for: {label} (keeping existing values)")
            data_rows.append(row)
            i += 1
        # Sort by label
        try:
            label_idx = header_cols.index('label')
        except ValueError:
            label_idx = 2
        data_rows.sort(key=lambda r: r.split('|')[label_idx].strip().lower() if len(r.split('|')) > label_idx else '')
        result.append(header)
        result.append(separator)
        result.extend(data_rows)
        continue
    result.append(line)
    i += 1
with open(doc_file, 'w') as f:
    f.writelines(result)
print("Done")
