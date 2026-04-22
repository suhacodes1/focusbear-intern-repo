# Git Understanding

## Part 1: Writing Meaningful Commit Messages

### What Makes a Good Commit Message?

A good commit message should:

- Be short but descriptive (ideally under 72 characters)
- Start with an action verb such as `Add`, `Fix`, `Update`, `Remove`, or `Refactor`
- Explain the **purpose** of the change, not every small detail
- Be easy to understand weeks or months later, by yourself or a teammate
- Focus on the _why_ behind the change, not just the _what_

### Three Commit Message Styles

#### 1. Vague Commit Message

```bash
git commit -m "fixed stuff"
```

**Why this is bad:**
This message tells a teammate (or future me) nothing about what was actually changed or why. If I need to track down a bug later, a message like this is useless in the commit history. It provides no context, no scope, and no direction.

#### 2. Overly Detailed Commit Message

```bash
git commit -m "updated navbar padding from 12px to 16px, fixed a typo in the footer copyright text, resized the homepage hero image to 1200px wide, adjusted the button hover animation duration from 0.3s to 0.2s, and removed three unused CSS classes from styles.css"
```

**Why this is not ideal:**
While it is better than being vague, this message is too long and difficult to quickly scan in a commit history. It suggests the commit contains too many unrelated changes at once, which also makes it harder to revert or review a specific fix. Each change ideally should be its own focused commit.

#### 3. Well-Structured Commit Message

```bash
git commit -m "Improve homepage UI and fix footer typo"
```

**Why this is good:**
It is clear, concise, and summarises the overall purpose of the commit. Anyone reading the history immediately understands the scope of the change without needing to open the diff. It uses an action verb and stays focused.

### Good vs. Bad Commit Messages — Summary

| Type    | Example                            | Why                                  |
| ------- | ---------------------------------- | ------------------------------------ |
| ❌ Bad  | `stuff`                            | Completely meaningless               |
| ❌ Bad  | `changes`                          | Too vague, no context                |
| ❌ Bad  | `final version`                    | Not descriptive, also never final    |
| ❌ Bad  | `update files`                     | Does not say what was updated or why |
| ✅ Good | `Fix login validation bug`         | Clear, action-driven, specific       |
| ✅ Good | `Add dark mode toggle`             | Explains what was added              |
| ✅ Good | `Refactor API error handling`      | Describes the purpose of the change  |
| ✅ Good | `Improve mobile navigation layout` | Communicates intent clearly          |

### What I Learned from Open-Source Projects

I explored the commit history of the **React** repository on GitHub ([github.com/facebook/react](https://github.com/facebook/react)) and observed how the core team writes commit messages. Some real examples I noticed:

- `Fix memory leak in useEffect cleanup`
- `Update error message for missing key prop`
- `Add tests for concurrent mode scheduler`
- `Refactor reconciler to improve readability`
  These are short, use action verbs, and describe the change clearly. None of them are vague or overloaded with detail. This showed me that even at a professional level with experienced engineers, the standard is simplicity and clarity — not exhaustive descriptions.

### How Does a Clear Commit Message Help in Team Collaboration?

When working in a team, commit messages are a shared communication tool. If I push a fix with the message `Fix null reference error in user profile loader`, a teammate reviewing the history immediately understands what happened without needing to ask me or read every line of the diff. This saves time during code reviews, debugging sessions, and when using tools like `git log` or `git blame`.

Clear messages also make it easier to write changelogs, onboard new team members, and understand the evolution of a feature over time.

### How Can Poor Commit Messages Cause Issues Later?

Poor commit messages create real problems down the track:

- **Debugging becomes harder.** If a bug was introduced three weeks ago and all commits say `update` or `fix`, there is no way to quickly identify which commit is responsible.
- **Reverting changes is risky.** Without knowing what a commit contains from its message, reverting it could accidentally undo unrelated work.
- **Onboarding takes longer.** New team members trying to understand the codebase from history will struggle if messages are meaningless.
- **Code reviews suffer.** Reviewers cannot efficiently assess the intent of a commit if the message does not explain it.
  In short, vague commit messages slow down everyone on the team, not just the person who wrote them.

---

## Part 2: Creating & Reviewing Pull Requests

### Why Are Pull Requests Important in a Team Workflow?

Pull Requests (PRs) are important because they create a structured and transparent way to introduce changes into the main codebase. Rather than pushing code directly to `main`, a PR gives teammates the opportunity to review the changes, ask questions, suggest improvements, and catch bugs before they reach production.

PRs also serve as a written record of _why_ a change was made. The title, description, and comment thread document the decision-making process, which is valuable for future reference. For distributed teams, PRs are often the primary space where collaboration and discussion actually happen.

Beyond quality control, PRs enforce accountability — the person submitting knows their work will be reviewed, which encourages more thoughtful, clean code.

### What Makes a Well-Structured Pull Request?

A well-structured PR should include:

- **A clear, descriptive title** that summarises what the PR does (e.g., `Fix null error on profile page load` not `bug fix`)
- **A written summary** explaining what was changed, why it was changed, and any relevant context
- **Small, focused changes** — one problem or feature per PR, not a mix of unrelated updates
- **Screenshots or recordings** if the change affects the UI, so reviewers can see the before and after
- **Testing confirmation** — a note that the changes have been tested locally or via automated tests
- **Links to related issues** so the PR is connected to the work item it resolves
- **Notes for reviewers** if any part of the code is complex or needs extra attention
  This structure makes reviews faster, reduces back-and-forth, and shows respect for the reviewer's time.

### What I Learned from Reviewing an Open-Source Pull Request

I reviewed a Pull Request in the **React** GitHub repository. The PR focused on fixing a user interface inconsistency and improving accessibility labels for screen readers.

From reviewing it, I observed the following:

- The developer wrote a detailed description explaining the problem, why it mattered for accessibility, and exactly what the fix involved
- Before-and-after screenshots were included so reviewers could visually confirm the change without running the code locally
- Reviewers asked specific questions about edge cases, such as behaviour in older browsers and how the change interacted with existing keyboard navigation
- Small, targeted code suggestions were made using GitHub's inline comment feature before the PR was approved
- The PR stayed tightly focused on one issue only, which made it straightforward to review without needing broader context
  This experience showed me that a PR is not just about the code — it is about communication, documentation, and making it easy for others to trust and approve your work.

---

## Part 3: Git Concepts — Staging vs. Committing

### What Is the Difference Between Staging and Committing?

**Staging** is the step where you select which changes you want to include in your next commit. When you run `git add <file>`, you are moving changes into the **staging area** (also called the index). The files are not saved to the repository history yet — they are simply queued up and ready.

**Committing** is the step where those staged changes are permanently recorded in the repository's history with a message. Running `git commit -m "your message"` takes everything in the staging area and creates a new snapshot.

Think of it like packing a box before posting it. Staging is placing items into the box. Committing is sealing it, labelling it, and sending it — it becomes a permanent record.

### Why Does Git Separate These Two Steps?

Git separates staging and committing to give you **precise control** over what goes into each commit. In practice, you might have modified three files but only want to commit two of them because the third is still a work in progress. Staging lets you do exactly that without losing your uncommitted changes on the third file.

This separation also encourages better commit hygiene. Instead of committing everything at once, you can group related changes into focused, meaningful commits — even if you worked on multiple things simultaneously.

### When Would You Want to Stage Without Committing?

There are several situations where staging without immediately committing is useful:

- **Grouping related changes:** You modified five files but only two relate to the same fix. Stage those two, commit them with a focused message, then stage the others separately.
- **Reviewing before committing:** Staging first lets you run `git status` and `git diff --staged` to double-check exactly what will be included before it is finalised.
- **Partial file staging:** Using `git add -p`, you can stage specific chunks within a single file rather than the whole file, for very fine-grained control.
- **Pausing mid-task:** You might stage completed work while continuing to edit other files, keeping your progress recorded without making a premature commit.

### What I Tried in My Repo

Here is the sequence of commands I ran to experiment with staging and committing:

```bash
# Modified a file called notes.txt, then staged it
git add notes.txt

# Checked the status — notes.txt showed as "Changes to be committed"
git status

# Decided I wasn't ready — unstaged the file
git reset HEAD notes.txt

# Checked status again — notes.txt moved back to "Changes not staged for commit"
git status

# Made a final edit, staged it again, then committed
git add notes.txt
git commit -m "Update notes with staging experiment observations"
```

**What I observed:** After `git add`, the file appeared in green under "Changes to be committed" in `git status`. After `git reset HEAD notes.txt`, it dropped back to red under "Changes not staged for commit". The file content itself was never touched — only its staging state changed. Seeing this in action made the two-step process feel deliberate and useful rather than unnecessarily complicated.

---

## Part 4: Debugging with `git bisect`

### What Does `git bisect` Do?

`git bisect` is a Git tool that uses **binary search** to find the exact commit that introduced a bug. Instead of manually checking every commit one by one, Git automatically narrows down the search by cutting the commit history in half with each step.

You tell Git which commit is "bad" (has the bug) and which earlier commit is "good" (did not). Git checks out the midpoint commit and asks you to test it. You mark it good or bad, and Git halves the range again — repeating until it pinpoints the single commit responsible.

### When Would You Use It in a Real-World Situation?

`git bisect` is most valuable when:

- A bug has appeared but you are not sure when it was introduced, and the commit history is too long to review manually
- Automated tests can confirm whether a commit is good or bad (enabling `git bisect run` to automate the entire process)
- You are working on a long-running project and need to trace a regression without spending hours reading diffs
  For example, if a feature that worked three weeks ago is now broken, and there have been 80 commits since then, `git bisect` can find the culprit in roughly 7 steps rather than 80 manual checks.

### My Experiment

I set up a small test repo and made a series of commits to simulate a bug being introduced midway through the history:

```bash
# Started a bisect session
git bisect start

# Marked the current broken commit as bad
git bisect bad

# Marked an earlier commit I knew was working fine as good
git bisect good a3f2c1b

# Git automatically checked out the midpoint commit
# I tested the code — it was still working correctly
git bisect good

# Git narrowed further and checked out another commit
# I tested — the bug was present
git bisect bad

# Git identified the first bad commit:
# "b7d9e4f is the first bad commit"
# Commit message: "Add discount calculation to cart total"

# Ended the session and returned to my original branch
git bisect reset
```

Git found the culprit in 3 steps across 10 commits — the `Add discount calculation to cart total` commit had introduced a logic error causing incorrect totals.

### How Does It Compare to Manually Reviewing Commits?

Manually reviewing commits means reading diffs one by one hoping to spot where something went wrong. With even 20–30 commits this becomes tedious and unreliable. `git bisect` turns debugging into a structured, efficient search — and it scales well. 1,000 commits only requires around 10 steps. It was one of the most surprisingly powerful Git tools I have come across so far.

---

## Part 5: Advanced Git Commands

### `git checkout main -- <file>`

**What it does:**
Restores a specific file to the version it has on the `main` branch, without switching branches or affecting any other files. It overwrites your local version of that file immediately.

**When I would use it:**
If I have been working on a feature branch and accidentally broken a file — or made changes I want to completely discard — this lets me reset just that one file without touching anything else. It is more surgical than a full branch reset.

**What surprised me:**
There is no confirmation prompt. The file is overwritten instantly and silently. This taught me to be careful, since there is no undo once the file is gone unless the changes were previously committed somewhere.

**Command I ran:**

```bash
git checkout main -- config.js
```

This immediately replaced my modified `config.js` with the clean version from `main`, while all my other working changes on the branch remained untouched.

---

### `git cherry-pick <commit>`

**What it does:**
Takes a single specific commit from any branch and applies it to your current branch. It does not merge the whole branch — it copies just that one commit's changes.

**When I would use it:**
The most common scenario is a hotfix. If a critical bug was fixed on a `dev` branch but you need that fix on `main` immediately — without merging all the other unfinished work from `dev` — you cherry-pick just the fix commit. It is also useful for pulling a single useful commit from an abandoned branch without reviving the whole thing.

**What surprised me:**
Cherry-pick creates a **brand new commit** with a different SHA hash, even though the content change is identical to the original. The original commit remains on its original branch unchanged. I assumed it would somehow move or link the commit — it is actually a copy.

**Command I ran:**

```bash
# While on main, applied a specific commit from the dev branch
git cherry-pick e5a1d3c
```

The changes from that commit appeared in `main`'s history as a fresh commit with a new hash.

---

### `git log`

**What it does:**
Displays the full commit history of the current branch — each commit's SHA hash, author, date, and message. It has many options to filter and format the output.

**When I would use it:**
I use `git log` to understand what has happened in a repo — reviewing recent changes before a merge, checking when a feature was added, or tracing who made a particular change. Useful variations I learned:

```bash
git log --oneline           # Compact one-line view per commit
git log --oneline --graph   # Visual branch and merge diagram in the terminal
git log --author="Name"     # Filter commits by a specific author
git log -- filename.js      # Show only commits that touched a specific file
```

**What surprised me:**
The `--graph` flag produces a surprisingly readable visual tree of branches and merges directly in the terminal. I expected it to look like noise, but for moderately complex histories it genuinely helps you understand how branches diverged and came back together over time.

---

### `git blame <file>`

**What it does:**
Annotates every line of a file with the commit hash, author, and date of the last change to that line. It shows you exactly who changed what and when, line by line.

**When I would use it:**
When I encounter confusing code and want to understand why it was written that way, `git blame` tells me which commit introduced it. I can then look up that commit to read the full context and message. It is also helpful for knowing who on the team has the most context about a particular section of a file.

**What surprised me:**
The name implies it is used to assign fault, but in practice it is simply a research tool. What surprised me technically is that `git blame` only shows the _most recent_ edit to each line. If a line has been changed multiple times, you only see the latest change and have to follow commit hashes manually to trace older history. There is also a `-C` flag that detects lines moved or copied from other files, which I did not know existed until I explored the documentation.

**Command I ran:**

```bash
git blame index.js
```

Each line of `index.js` was prefixed with the commit hash, author, and timestamp, making it immediately clear which parts of the file had been touched recently and which had not changed in months.

---

## Reflection

Each of these sections has deepened my understanding of Git beyond the basics of `add`, `commit`, and `push`. The staging model showed me that Git is designed for precision and intentional control. `git bisect` demonstrated that debugging does not always mean reading code — sometimes it means searching history efficiently. The advanced commands reinforced that Git is a research and collaboration tool as much as a version control system: `git log`, `git blame`, and `git cherry-pick` all exist to help teams understand, navigate, and selectively apply their project history.

Going forward I will treat Git as a core professional skill, not just a mechanism for saving work.
