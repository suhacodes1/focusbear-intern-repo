# Understanding Git Merge Conflicts and Pull Requests

## What caused the conflict?

The merge conflict happened when two different changes were made to the same file in separate branches. Git was unable to automatically decide which version to keep because both branches modified the same section of the file.

## How did you resolve it?

I resolved the conflict by opening the affected file and reviewing the conflict markers added by Git. I compared both versions of the code, selected the correct changes, and combined any important parts. After removing the conflict markers, I saved the file, staged the changes using `git add`, and completed the merge with a commit.

## What did you learn?

I learned that merge conflicts are a normal part of working with Git, especially when multiple people edit the same files. I also learned how important it is to pull updates regularly, communicate with team members, and keep branches organised. Resolving conflicts helped me better understand version control and collaboration workflows.

---

# Understanding Pull Requests

## Why are Pull Requests important in a team workflow?

Pull Requests (PRs) are important because they create a structured way for developers to propose changes before merging code into the main branch. They allow teammates to review code, give feedback, catch bugs early, and discuss improvements. PRs also help maintain code quality and ensure everyone understands what changes are being introduced.

## What makes a well-structured Pull Request?

A well-structured PR should include:

- A clear and descriptive title
- A summary explaining what was changed and why
- Small, focused changes instead of many unrelated updates
- Clean and readable code
- Testing completed before submission
- Screenshots if UI changes were made
- Comments or notes for reviewers if needed

This makes the review process faster and easier for the team.

## What did I learn from reviewing an open-source Pull Request?

I reviewed a Pull Request in the Github repository.

The PR focused on fixing a user interface issue and improving accessibility labels. From reviewing it, I noticed:

- The developer clearly explained the problem before showing the fix
- Screenshots were included for before and after comparisons
- Reviewers asked questions about edge cases and browser behaviour
- Small code suggestions were made before approval
- The PR stayed focused on one issue only, making it easier to review

This showed me that PRs are not just about code—they are also about communication, collaboration, and maintaining project standards.

## Example Screenshot / Evidence

I viewed the PR discussion page on GitHub and observed reviewer comments, requested changes, and the final approval workflow.
