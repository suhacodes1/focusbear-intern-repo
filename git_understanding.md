# Understanding Git Merge Conflicts

## What caused the conflict?

The merge conflict happened when two different changes were made to the same file in separate branches. Git was unable to automatically decide which version to keep because both branches modified the same section of the file.

## How did you resolve it?

I resolved the conflict by opening the affected file and reviewing the conflict markers added by Git. I compared both versions of the code, selected the correct changes, and combined any important parts. After removing the conflict markers, I saved the file, staged the changes using `git add`, and completed the merge with a commit.

## What did you learn?

I learned that merge conflicts are a normal part of working with Git, especially when multiple people edit the same files. I also learned how important it is to pull updates regularly, communicate with team members, and keep branches organised. Resolving conflicts helped me better understand version control and collaboration workflows.
