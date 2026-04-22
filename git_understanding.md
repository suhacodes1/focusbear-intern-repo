# Git Understanding

---

## Part 1: Writing Meaningful Commit Messages

### What Makes a Good Commit Message?

A good commit message should:

- Be short but descriptive (ideally under 72 characters)
- Start with an action verb such as `Add`, `Fix`, `Update`, `Remove`, or `Refactor`
- Explain the **purpose** of the change, not every small detail
- Be easy to understand weeks or months later, by yourself or a teammate
- Focus on the _why_ behind the change, not just the _what_

---

### Three Commit Message Styles

#### 1. Vague Commit Message

```
git commit -m "fixed stuff"
```

**Why this is bad:**
This message tells a teammate (or future me) nothing about what was actually changed or why. If I need to track down a bug later, a message like this is useless in the commit history. It provides no context, no scope, and no direction.

---

#### 2. Overly Detailed Commit Message

```
git commit -m "updated navbar padding from 12px to 16px, fixed a typo in the footer copyright text, resized the homepage hero image to 1200px wide, adjusted the button hover animation duration from 0.3s to 0.2s, and removed three unused CSS classes from styles.css"
```

**Why this is not ideal:**
While it is better than being vague, this message is too long and difficult to quickly scan in a commit history. It suggests the commit contains too many unrelated changes at once, which also makes it harder to revert or review a specific fix. Each change ideally should be its own focused commit.

---

#### 3. Well-Structured Commit Message

```
git commit -m "Improve homepage UI and fix footer typo"
```

**Why this is good:**
It is clear, concise, and summarises the overall purpose of the commit. Anyone reading the history immediately understands the scope of the change without needing to open the diff. It uses an action verb and stays focused.

---

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

---

### What I Learned from Open-Source Projects

I explored the commit history of the **React** repository on GitHub ([github.com/facebook/react](https://github.com/facebook/react)) and observed how the core team writes commit messages. Some real examples I noticed:

- `Fix memory leak in useEffect cleanup`
- `Update error message for missing key prop`
- `Add tests for concurrent mode scheduler`
- `Refactor reconciler to improve readability`
  These are short, use action verbs, and describe the change clearly. None of them are vague or overloaded with detail. This showed me that even at a professional level with experienced engineers, the standard is simplicity and clarity — not exhaustive descriptions.

---

### How Does a Clear Commit Message Help in Team Collaboration?

When working in a team, commit messages are a shared communication tool. If I push a fix with the message `Fix null reference error in user profile loader`, a teammate reviewing the history immediately understands what happened without needing to ask me or read every line of the diff. This saves time during code reviews, debugging sessions, and when using tools like `git log` or `git blame`.

Clear messages also make it easier to write changelogs, onboard new team members, and understand the evolution of a feature over time.

---

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

---

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

---

### What I Learned from Reviewing an Open-Source Pull Request

I reviewed a Pull Request in the **React** GitHub repository. The PR focused on fixing a user interface inconsistency and improving accessibility labels for screen readers.

From reviewing it, I observed the following:

- The developer wrote a detailed description explaining the problem, why it mattered for accessibility, and exactly what the fix involved
- Before-and-after screenshots were included so reviewers could visually confirm the change without running the code locally
- Reviewers asked specific questions about edge cases, such as behaviour in older browsers and how the change interacted with existing keyboard navigation
- Small, targeted code suggestions were made using GitHub's inline comment feature before the PR was approved
- The PR stayed tightly focused on one issue only, which made it straightforward to review without needing broader context
  This experience showed me that a PR is not just about the code — it is about communication, documentation, and making it easy for others to trust and approve your work. The clarity of the description and the quality of the screenshots made the review process much smoother than it would have been otherwise.

---

### Reflection

Working through both tasks gave me a clearer sense of how professional development teams maintain quality and communication through Git. Commit messages and pull requests both serve the same underlying purpose: making it easier for a team to understand, trust, and build on each other's work.

I used to think commit messages were just a formality, but now I see them as a log that future me — or a teammate — will genuinely rely on. The same goes for PRs: they are not a hurdle, they are a checkpoint that protects the whole team.

Going forward, I will write every commit message as if a teammate needs to understand it at a glance, and every PR as if I am handing my work to someone who has no prior context about what I was trying to do.
