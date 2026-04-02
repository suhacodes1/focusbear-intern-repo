# CI/CD Reflection

## What is the purpose of CI/CD?

CI/CD helps automate important parts of the software development process, such as running checks, tests, builds, and deployments whenever code changes are made. The purpose of Continuous Integration is to make sure new changes are regularly integrated and validated, while Continuous Deployment or Continuous Delivery helps make releases more consistent and reliable.

## How does automating style checks improve project quality?

Automating style checks improves project quality by catching formatting issues, spelling mistakes, and documentation problems early. This keeps the project more consistent and reduces the chance of small mistakes being merged into the repository. It also saves time during code review because reviewers do not need to focus as much on basic style issues.

## What are some challenges with enforcing checks in CI/CD?

One challenge is that strict checks can sometimes slow developers down if the rules are too sensitive or poorly configured. Another challenge is handling false positives, such as project-specific words being flagged by spell checkers. Teams also need to maintain the CI/CD configuration over time as the project grows.

## How do CI/CD pipelines differ between small projects and large teams?

In small projects, CI/CD pipelines are usually simpler and may only include a few checks such as linting, tests, and basic deployment steps. In larger teams, CI/CD pipelines are often much more detailed and can include multiple stages, security scans, environment-based deployments, approvals, and more complex testing. Large teams also rely more on CI/CD to keep work consistent across many contributors.
