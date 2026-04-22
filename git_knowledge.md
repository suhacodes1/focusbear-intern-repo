# Git Knowledge

## Git Setup Reflections

### Have you used Git before? If so, in what context?

I have used Git before, but only at a basic level. My previous experience was mainly during school projects where I used it to save and submit code. I knew how to run `git add`, `git commit`, and `git push`, but I did not fully understand what was happening behind the scenes or why those steps mattered. I had not worked with branches, pull requests, or collaborative workflows before starting this internship, so most of what I am learning here is genuinely new to me.

---

### Verifying Git Installation

After installing Git, I ran the following command in the terminal to confirm it was set up correctly:

```bash
git --version
```

**Output:**

```bash
git version 2.47.1
```

This confirmed that Git was installed and ready to use on my system.

---

### Which Git Client Did You Choose? Why?

I decided to use **GitHub Desktop** alongside the Git command line tools.

I chose GitHub Desktop because it gives me a clear visual overview of changes before I commit them. Being able to see exactly which lines were added or removed in a diff view helps me double-check my work before pushing. Since I am still building confidence with Git, having a visual interface reduces the chance of making mistakes like committing to the wrong branch or staging files I did not intend to.

That said, I am also practising Git commands directly in the terminal so I understand what is actually happening under the hood. My plan is to rely less on the client over time as I become more comfortable with the command line workflow.

---

### What Was the Most Interesting Thing You Learned About Git Today?

The most interesting thing I learned today was how Git's **branching model** works and why it matters so much for team collaboration.

Before today, I thought of Git mainly as a save system — a way to keep a history of your files. But learning about branches changed how I see it. The idea that multiple people can work on completely separate versions of the same codebase at the same time, without interfering with each other, and then bring those changes together through a merge or pull request, is genuinely impressive.

I also found it interesting that `git commit` does not just save your work — it creates a permanent snapshot with a unique identifier (a SHA hash) that you can always return to. That means nothing is ever truly lost once it has been committed, which makes Git feel much safer to work with than I initially thought.

Seeing how professional teams use short-lived feature branches for every change, rather than committing directly to `main`, also helped me understand why Git is such a fundamental tool in software development — it is not just version control, it is how teams stay organised and move fast without breaking things.
