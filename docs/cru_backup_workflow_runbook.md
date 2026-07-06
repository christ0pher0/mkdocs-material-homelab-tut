# Runbook: CRU Backup Drive Workflow
**Owner:** Alex (Storage) / Kai (Proxmox passthrough) | **Frequency:** As needed (drive swap sessions)
**Last Updated:** 2026-07-06 | **Last Run:** 2026-07-06 (STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL)

## Purpose
Covers the full lifecycle of a CRU backup drive session on restic-deb (VM 100, hosted on blaine): onboarding a new/swapped drive into the hot-swap bay, running the backup, the mandatory exit script chain, offboarding the drive, and syncing session notes back to the docs site. Consolidates tribal knowledge from the 2026-07-03 hotplug automation work (Sam + Kai) that was never written down as its own doc — this replaces the "10 steps that took hours" with the actual current automated procedure.

## Prerequisites
- [ ] SSH access to blaine (192.168.1.11) and restic-deb (192.168.1.40)
- [ ] Physical access to the CRU hot-swap bays (blaine)
- [ ] `~/cru_hotplug.sh`, `~/cru_vm_detach_check.sh`, `~/drives.db` present on blaine
- [ ] `~/scripts/cru_mount_vm.sh`, `~/scripts/cru_stats.sh`, `~/scripts/cru_plexfolder_stats.sh`, `~/scripts/backup_drives_update.sh` present on restic-deb
- [ ] `backup_drives.md` (blaine, `~/backup_drives.md`) open for reference/updating

---

## Procedure

### Part A — Onboarding a new/swapped CRU drive

#### Step 1: Snapshot the current drive baseline (before touching any hardware)
```bash
# On blaine (192.168.1.11)
./cru_hotplug.sh snapshot
```
**Expected result:** Baseline file saved (`~/.cru_hotplug_baseline`), lists current ATA drives with system/boot disks auto-excluded.
**If it fails:** Confirm you're not accidentally running this from inside a VM — this must run on the blaine host itself.

#### Step 2: Physically swap the drive
Remove the old drive from the bay (only after confirming it's clear — see Part C offboarding first if a drive is currently in use) and insert the new one.

#### Step 3: Detect the new drive
```bash
# On blaine (192.168.1.11)
./cru_hotplug.sh detect
```
**Expected result:** Rescans the SCSI bus automatically, diffs against the snapshot, prints the new drive's `by-id` path.
**If it fails:** "No new drives detected" after a real swap usually means the bay didn't hot-plug cleanly — reseat the drive and re-run.

#### Step 4: Identify the drive against the database
```bash
# On blaine (192.168.1.11)
./cru_hotplug.sh identify /dev/disk/by-id/<drive-from-step-3>
```
**Expected result:** Reads serial/model/size via smartctl, cross-references `drives.db`. Either matches a known drive (shows category/label/backup_date/smart) or reports UNKNOWN for a genuinely new drive.
**If it fails:** "Could not read serial" — drive may not be fully spun up yet, wait a few seconds and retry.

#### Step 5: Pre-flight check the target VM slot
```bash
# On blaine (192.168.1.11)
./cru_hotplug.sh preflight 100 scsi1
```
**Expected result:** Dry-run by default — reports whether `scsi1` on VM 100 (restic-deb) is clear or has a stale entry.
**If it fails / slot occupied:** Re-run with `--apply` to detach the stale entry, or use `cru_vm_detach_check.sh 100 scsi1` (does the same detach automatically, no dry-run gate — use when you're sure).

#### Step 6: Attach the drive to the VM
```bash
# On blaine (192.168.1.11)
./cru_hotplug.sh attach 100 /dev/disk/by-id/<drive-from-step-3> scsi1 --apply
```
**Expected result:** Runs `qm set 100 -scsi1 <path>` under the hood, drive becomes visible inside restic-deb.
**If it fails:** Check `qm config 100` for slot conflicts; confirm the by-id path still exists (`ls -la /dev/disk/by-id/`).

#### Step 7: Mount inside the VM
```bash
# On restic-deb (192.168.1.40)
./scripts/cru_mount_vm.sh mount
```
**Expected result:** Drive mounts at `/mnt/cru{1,2,3}` based on the UUID_MAP in the script. If this is a genuinely new drive/UUID, the script won't recognize it — update `UUID_MAP` in `cru_mount_vm.sh` first.
**If it fails:** Check `blkid` output for the actual UUID/filesystem type; NTFS drives need `ntfs-3g`, already handled by the script.

#### Step 8: Update the drive record
If Step 4 reported UNKNOWN (genuinely new drive), add a row to `~/backup_drives.md` on blaine (label, model, size, serial), then:
```bash
# On blaine (192.168.1.11)
python3 build_drives_db.py
```
**Expected result:** `drives.db` regenerated with the new row included.

---

### Part B — Running the backup
Standard rsync convention (see [[feedback_rsync_flags]]): dry-run first, then live.
```bash
# On restic-deb (192.168.1.40)
rsync -av --ignore-existing --info=progress2 --dry-run /mnt/plex/<source>/ /mnt/cru<N>/<dest>/
```
Review, then re-run without `--dry-run`. **Never use `--delete`** on archive drives.

---

### Part C — Exit script chain (mandatory, every session)
Run in this exact order after every backup session, before offboarding the drive:

```bash
# On restic-deb (192.168.1.40)
./scripts/cru_plexfolder_stats.sh -du --save
./scripts/cru_stats.sh
./scripts/backup_drives_update.sh
```
**Expected result:** Plex folder stats saved, per-drive usage stats written to `~/scripts/cru_stats/<label>.txt`, and `backup_drives.md` updated with current usage/backup date.
**If it fails:** Do not skip a step even if one errors — each writes to a different file; a failure in one doesn't invalidate the others. Re-run the failed one individually.

---

### Part D — Offboarding a drive (before physical removal)

#### Step 1: Check host-level mount status
```bash
# On blaine (192.168.1.11)
./cru_hotplug.sh mountcheck
```
**Expected result:** "All CRU drives clear — safe to physically remove any of them." If any show MOUNTED, the drive is in active use at the host level — do not pull it.

#### Step 2: Unmount inside the VM
```bash
# On restic-deb (192.168.1.40)
./scripts/cru_mount_vm.sh unmount
```

#### Step 3: Detach from the VM
```bash
# On blaine (192.168.1.11)
./cru_vm_detach_check.sh 100 scsi1
```
**Expected result:** Detects and detaches the existing passthrough entry automatically.

#### Step 4: Physically remove the drive
Safe to pull once Steps 1-3 are clean.

---

### Part E — Sync session notes to docs (mandatory, every session)
```powershell
# On amontillado (192.168.1.100) in PowerShell
scp "C:\Users\Edgar Allin Poet\Claude\Projects\Project - Homelab Executive Director & Project Manager\todo.md" cos@192.168.1.3:~/material/mkdocs_dev_material/docs/todo.md
```
```bash
# On git-ansible (192.168.1.3)
cd ~/material/mkdocs_dev_material && git add docs/todo.md && git commit -m "sync: todo.md" && git push
```
**Both steps required.** SCP alone leaves the git-ansible working directory ahead of Gitea, which breaks the checkbox-persistence webhook (port 9999) on the next commit attempt from any source.

**Also sync `backup_drives.md` if it was updated this session (Part C, Step 3 of the exit chain updates it on blaine):**
```bash
# On blaine (192.168.1.11)
scp ~/backup_drives.md cos@192.168.1.3:~/material/mkdocs_dev_material/docs/backup_drives.md
```
```bash
# On git-ansible (192.168.1.3)
cd ~/material/mkdocs_dev_material && git add docs/backup_drives.md && git commit -m "sync: backup_drives.md" && git push
```
⚠️ **Known gap (found 2026-07-06):** `backup_drives.md` lives on blaine and was being edited locally without ever pulling from/pushing back to git-ansible — the docs site fell behind blaine's actual data (missing STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL rows). Follow the same discipline as `todo.md`: pull before editing, push after, every session — don't let blaine's local copy become its own silent source of truth.

---

## Verification
- [ ] `cru_hotplug.sh mountcheck` (blaine) shows all drives clear if session is done
- [ ] `cru_mount_vm.sh status` (restic-deb) shows expected label/mount for each bay
- [ ] `backup_drives.md` (blaine) shows updated Backup date and Used/Free for the drive(s) touched this session
- [ ] `git log --oneline -1 -- docs/todo.md` (git-ansible) shows today's sync commit

## Troubleshooting
| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `cru_hotplug.sh detect` finds nothing after a real swap | Hot-swap bay didn't signal the kernel | Reseat drive, re-run `detect` (it auto-rescans) |
| `cru_mount_vm.sh mount` doesn't recognize the drive | New UUID not in `UUID_MAP` | Edit `UUID_MAP` in `cru_mount_vm.sh` on restic-deb, add the new bay/UUID pair |
| `attach`/`preflight` reports slot occupied unexpectedly | Stale passthrough from a previous session that wasn't cleanly detached | Run `cru_vm_detach_check.sh 100 scsi1` before retrying attach |
| Checkboxes on the MkDocs todo page don't persist | SCP was run without the git-ansible commit+push step | Re-run both steps together (Part E) — never SCP alone |
| `backup_drives.md` shows no Backup date/Used/Free after running the exit chain | **Confirmed path mismatch (2026-07-06):** `cru_stats.sh` writes stats to `/opt/cru_stats/<label>.txt`, but `backup_drives_update.sh` reads from a different path (`~/scripts/cru_stats/` per earlier finding) — the two scripts don't agree on where stats live, so the update script finds nothing even when stats were generated successfully. | Not a workaround — this is a real script bug for Sam to fix (make both scripts agree on one path). Until fixed, manually verify stats actually exist in `/opt/cru_stats/` before assuming a drive session's stats generation failed. |

## Rollback
- **Attach went wrong:** `qm unset 100 -scsi1` on blaine (or re-run `cru_hotplug.sh preflight 100 scsi1 --apply`) to clear the slot, then retry.
- **Wrong drive mounted/labeled:** `cru_mount_vm.sh relabel <bay> <label>` on restic-deb to correct without re-doing the whole attach.
- **Docs sync pushed bad content:** `git revert` the specific commit on git-ansible, then re-run Part E with corrected content.

## Escalation
| Situation | Contact | Method |
|-----------|---------|--------|
| Passthrough/VM attach failure, `qm` errors | Kai | Direct message / next standup |
| Drive physically failing (SMART errors, won't spin up) | Alex | Direct message |
| Docs site/webhook not updating after correct sync | Morgan | Direct message |

## History
| Date | Run By | Notes |
|------|--------|-------|
| 2026-07-03 | Sam + Kai | Hotplug automation built (`cru_hotplug.sh`, `cru_vm_detach_check.sh`), never written up as a standalone runbook until now |
| 2026-07-06 | Chris | STL_ACCESSORIES_TERRAIN, STL_SOURCE_MATERIAL sessions — this runbook drafted retroactively from the actual scripts to close that gap |
