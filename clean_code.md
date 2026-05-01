# Clean Code — Reflections & Examples

---

## 1. Understanding Clean Code Principles

### Core Principles

**Simplicity** — Code should do exactly what it needs to do, nothing more. Avoid clever tricks or unnecessary abstractions. If a junior developer would struggle to understand what a line does at a glance, it probably needs to be simplified.

**Readability** — Code is read far more often than it is written. Variable names, function names, and structure should communicate intent clearly without requiring the reader to trace through logic to figure out what something does.

**Maintainability** — Code should be written so that a future developer (or yourself, six months later) can confidently modify it without fear of breaking unrelated things. This means clear separation of concerns, good naming, and avoiding hidden dependencies.

**Consistency** — Following the same conventions throughout a project reduces cognitive load. Whether it's naming conventions, indentation style, or how errors are handled, consistency lets developers focus on logic rather than decoding style variations.

**Efficiency** — Write code that performs well, but don't prematurely optimise. Get it working and readable first, then optimise where profiling shows it's actually needed.

---

### Messy Code Example — Why It's Hard to Read

```js
// BAD: Messy, unclear code
function p(d) {
  let r = [];
  for (let i = 0; i < d.length; i++) {
    if (d[i].a === true && d[i].s !== "x" && d[i].v > 0) {
      r.push({ n: d[i].n, v: d[i].v * 1.1 });
    }
  }
  return r;
}
```

**Why it's hard to read:**

- `p`, `d`, `r`, `a`, `s`, `v`, `n` are all meaningless abbreviations.
- There is no indication of what the function does, what it accepts, or what it returns.
- The nested condition mixes multiple concerns inline with no explanation.
- A reader has to reverse-engineer intent from structure alone.

---

### Rewritten — Clean Version

```js
// GOOD: Clean, readable code
function getEligibleProductsWithIncreasedPrice(products) {
  return products
    .filter(
      (product) =>
        product.isActive &&
        product.status !== "discontinued" &&
        product.value > 0
    )
    .map((product) => ({
      name: product.name,
      value: product.value * 1.1,
    }));
}
```

**Why it's better:**

- The function name describes exactly what it does.
- Variable names (`products`, `product`, `isActive`, `status`, `value`, `name`) are self-documenting.
- The filter/map pattern makes the two-step intent (filter then transform) immediately obvious.
- No comments are needed because the code explains itself.

---

## 2. Code Formatting & Style Guides

### Why Code Formatting Matters

Consistent formatting makes a codebase feel like it was written by one person, even when it wasn't. It reduces the mental effort of reading unfamiliar code and eliminates style debates in code reviews, so the focus stays on logic and correctness.

The **Airbnb JavaScript Style Guide** is one of the most widely adopted style standards. Key rules include: using `const` and `let` instead of `var`, preferring arrow functions, enforcing single quotes for strings, requiring trailing commas in multi-line expressions, and keeping lines under 100 characters.

### Setting Up ESLint and Prettier

```bash
npm install --save-dev eslint prettier eslint-config-airbnb eslint-plugin-import eslint-plugin-react
```

`.eslintrc.json`:

```json
{
  "extends": ["airbnb"],
  "rules": {
    "no-console": "warn",
    "prefer-const": "error"
  }
}
```

`.prettierrc`:

```json
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "trailingComma": "es5"
}
```

### Issues the Linter Detected

Running ESLint on a typical first-draft codebase commonly surfaces:

- `var` used instead of `const`/`let`
- Missing semicolons (or inconsistent use)
- Unused variables left in scope
- Functions that could be simplified to arrow functions
- Inconsistent spacing around operators and after keywords
- Lines exceeding the character limit

### Did Formatting Make the Code Easier to Read?

Yes. After running Prettier and fixing ESLint warnings, files became visually uniform — consistent indentation, consistent quote style, and aligned structure. It also made `git diff` outputs cleaner since whitespace noise was eliminated. The biggest win was that reviewing code became faster because there was no style variation to adjust to between files.

---

## 3. Writing Small, Focused Functions

### Why Breaking Down Functions Is Beneficial

A function should do one thing and do it well. When a function handles multiple concerns — validation, data transformation, side effects, and formatting — it becomes difficult to test in isolation, hard to name accurately, and a risk when any single part needs to change.

Small functions are also easier to reuse. A `formatCurrency(amount)` function can be used anywhere, whereas the same logic buried in a `renderInvoice()` function cannot.

### Before — Long, Complex Function

```js
// BAD: One function doing everything
function processOrder(order) {
  if (!order.items || order.items.length === 0) {
    console.log("No items");
    return null;
  }
  let total = 0;
  for (let i = 0; i < order.items.length; i++) {
    if (order.items[i].qty > 0) {
      total += order.items[i].price * order.items[i].qty;
    }
  }
  if (order.coupon === "SAVE10") {
    total = total * 0.9;
  }
  const tax = total * 0.1;
  total = total + tax;
  const receipt = `Order for ${order.customer}: $${total.toFixed(2)}`;
  console.log(receipt);
  return receipt;
}
```

**What made it complex:**

- It validates input, calculates a subtotal, applies a discount, calculates tax, formats output, and logs — all in one place.
- If the discount logic changes, or the tax rate changes, you're editing a large block with many other responsibilities.
- It's nearly impossible to unit test the subtotal calculation without also triggering the logging.

### After — Refactored into Small Functions

```js
// GOOD: Each function has a single responsibility
function hasValidItems(order) {
  return order.items && order.items.length > 0;
}

function calculateSubtotal(items) {
  return items
    .filter((item) => item.qty > 0)
    .reduce((sum, item) => sum + item.price * item.qty, 0);
}

function applyDiscount(subtotal, coupon) {
  if (coupon === "SAVE10") return subtotal * 0.9;
  return subtotal;
}

function applyTax(amount, taxRate = 0.1) {
  return amount + amount * taxRate;
}

function formatReceipt(customerName, total) {
  return `Order for ${customerName}: $${total.toFixed(2)}`;
}

function processOrder(order) {
  if (!hasValidItems(order)) {
    console.log("No items");
    return null;
  }
  const subtotal = calculateSubtotal(order.items);
  const discounted = applyDiscount(subtotal, order.coupon);
  const total = applyTax(discounted);
  const receipt = formatReceipt(order.customer, total);
  console.log(receipt);
  return receipt;
}
```

### How Refactoring Improved the Structure

Each step of the process is now named, independently testable, and easy to modify. If the tax rate changes, only `applyTax` needs updating. If a new coupon type is added, only `applyDiscount` changes. The main `processOrder` function now reads almost like a plain-English description of the workflow.

---

## 4. Avoiding Code Duplication (DRY Principle)

### The DRY Principle

"Don't Repeat Yourself" means every piece of knowledge or logic should have a single, authoritative representation in the codebase. When the same logic appears in multiple places, a change to that logic requires finding and updating every copy — and missing even one creates bugs.

### Before — Duplicated Code

```js
// BAD: Validation logic repeated across multiple functions
function createUser(name, email) {
  if (!name || name.trim() === "") {
    throw new Error("Name is required");
  }
  if (!email || !email.includes("@")) {
    throw new Error("Valid email is required");
  }
  // create user...
}

function updateUser(name, email) {
  if (!name || name.trim() === "") {
    throw new Error("Name is required");
  }
  if (!email || !email.includes("@")) {
    throw new Error("Valid email is required");
  }
  // update user...
}

function inviteUser(name, email) {
  if (!name || name.trim() === "") {
    throw new Error("Name is required");
  }
  if (!email || !email.includes("@")) {
    throw new Error("Valid email is required");
  }
  // send invite...
}
```

**Issues with the duplicated code:**

- The validation logic appears three times. If the email validation rule changes (e.g., using a proper regex), it must be updated in three places.
- Any inconsistency between copies — even a small typo in an error message — creates subtle bugs that are hard to trace.
- The code is longer and harder to scan because most of what you're reading is repetition, not new information.

### After — DRY Refactor

```js
// GOOD: Validation extracted into a single reusable function
function validateUserInput(name, email) {
  if (!name || name.trim() === "") {
    throw new Error("Name is required");
  }
  if (!email || !email.includes("@")) {
    throw new Error("Valid email is required");
  }
}

function createUser(name, email) {
  validateUserInput(name, email);
  // create user...
}

function updateUser(name, email) {
  validateUserInput(name, email);
  // update user...
}

function inviteUser(name, email) {
  validateUserInput(name, email);
  // send invite...
}
```

### How Refactoring Improved Maintainability

The validation rule now lives in one place. If the email format check needs to become a proper regex, or a new "name must be at least 2 characters" rule is added, there is exactly one function to update. The three calling functions become shorter and easier to read, since they clearly delegate validation to a well-named helper rather than embedding it inline.

---

## 5. Refactoring Code for Simplicity

### Common Refactoring Techniques

- **Extract function** — pull a block of logic into its own named function.
- **Replace conditionals with polymorphism or lookup tables** — replace long `if/else` chains with data-driven structures.
- **Remove dead code** — delete code that is no longer reached or used.
- **Flatten nested logic** — use early returns to reduce indentation.
- **Replace magic numbers with named constants** — `MAX_RETRIES = 3` instead of the raw `3` appearing in logic.

### Before — Overly Complicated Code

```js
// BAD: Complex, deeply nested, hard to follow
function getShippingCost(order) {
  let cost = 0;
  if (order) {
    if (order.country) {
      if (order.country === "AU") {
        if (order.total > 100) {
          cost = 0;
        } else {
          cost = 9.95;
        }
      } else {
        if (order.country === "US" || order.country === "UK") {
          if (order.total > 200) {
            cost = 15;
          } else {
            cost = 29.95;
          }
        } else {
          cost = 49.95;
        }
      }
    }
  }
  return cost;
}
```

**What made the original code complex:**

- Deep nesting (5 levels) forces the reader to track context through multiple `if` blocks simultaneously.
- The `let cost = 0` pattern means you have to read to the end of every branch to know what value was assigned.
- Adding a new country or changing a threshold means carefully navigating the nested structure and risking breaking an existing branch.

### After — Refactored for Simplicity

```js
// GOOD: Flat, readable, easy to extend
const SHIPPING_RULES = [
  { countries: ["AU"], freeThreshold: 100, standardCost: 9.95 },
  { countries: ["US", "UK"], freeThreshold: 200, standardCost: 29.95 },
];

const INTERNATIONAL_SHIPPING_COST = 49.95;

function getShippingCost(order) {
  if (!order?.country) return 0;

  const rule = SHIPPING_RULES.find((r) => r.countries.includes(order.country));
  if (!rule) return INTERNATIONAL_SHIPPING_COST;

  return order.total > rule.freeThreshold ? 0 : rule.standardCost;
}
```

### How Refactoring Improved It

The nesting is gone. The shipping rules are declared as data rather than control flow, which means adding a new region is a one-line addition to the `SHIPPING_RULES` array rather than a structural change to the function. Early returns eliminate the need to mentally track the `cost` variable across branches. The final line reads almost like a sentence: if the total exceeds the free threshold, shipping is free; otherwise use the standard cost.

---

## 6. Commenting & Documentation

### Best Practices for Comments

Good comments explain **why**, not **what**. If the code itself clearly shows what is happening, a comment restating it is noise. Comments earn their place when they explain a non-obvious decision, a known limitation, a performance trade-off, or the reason a seemingly wrong-looking approach is actually intentional.

### When Should You Add Comments?

- **Explaining intent behind a non-obvious choice** — e.g., why a particular algorithm was chosen over a simpler one, or why a magic number exists.
- **Documenting external constraints** — e.g., "This API returns dates as Unix timestamps in milliseconds, not seconds."
- **Warning about gotchas** — e.g., "Do not call this function before the auth token has been set."
- **Public API documentation** — JSDoc / docstrings on exported functions, classes, and modules so consumers understand the contract without reading the implementation.
- **Temporarily marking incomplete work** — `// TODO:` and `// FIXME:` comments are acceptable during active development if they're tracked and resolved.

### When Should You Avoid Comments and Improve the Code Instead?

- **When the comment just restates the code** — `i++; // increment i` adds nothing.
- **When a better name would make the comment unnecessary** — if you're writing `// check if user is eligible`, consider renaming the function to `isUserEligible()` instead.
- **When the comment describes what a block does** — this is usually a signal to extract that block into a named function.
- **When the comment is outdated** — stale comments that no longer match the code are actively misleading and worse than no comment at all.

The general rule: if you feel the urge to write a comment, first ask whether the code could be rewritten to make the comment unnecessary.

### Before — Poorly Commented Code

```js
// function
function calc(u, t) {
  // do the thing
  let x = u.bal;
  // check
  if (t === 1) {
    x = x - 50; // minus
  } else {
    x = x - 100; // minus more
  }
  // return
  return x;
}
```

**Problems:**

- Comments like `// function`, `// do the thing`, `// check`, and `// return` describe obvious structure, not intent.
- `// minus` and `// minus more` restate the arithmetic without explaining why there are two different amounts.
- The real question — what is `t`? what does `1` mean? — is never answered.

### After — Useful Comments and Better Code

```js
/**
 * Calculates a user's balance after applying a withdrawal fee.
 * Premium users (tier 1) are charged a reduced fee of $50.
 * Standard users are charged the default fee of $100.
 *
 * @param {Object} user - User object with a `balance` property
 * @param {number} userTier - 1 for premium, any other value for standard
 * @returns {number} The updated balance after the fee
 */
function calculateBalanceAfterFee(user, userTier) {
  const PREMIUM_FEE = 50;
  const STANDARD_FEE = 100;

  const isPremium = userTier === 1;
  const fee = isPremium ? PREMIUM_FEE : STANDARD_FEE;

  return user.balance - fee;
}
```

**Why this is better:**

- The JSDoc block documents the public contract: what the function does, what parameters mean, and what it returns.
- Named constants (`PREMIUM_FEE`, `STANDARD_FEE`) eliminate the magic numbers.
- `isPremium` makes the condition self-documenting — no inline comment needed.
- The implementation comment is gone because the code now explains itself.
