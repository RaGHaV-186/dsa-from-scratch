# Patterns & Notes

## Complexity basics
- Time = how many steps as n grows. Space = how many new boxes as n grows.
- Drop constants: O(2n) → O(n), O(n²/2) → O(n²).
- "The complexity" means worst case unless stated otherwise.
- Two sizes (m rows, n cols) → keep both letters: O(m·n), not O(n²).
- Ask "one per ___?" to pick the letter: per row → m, per column → n, per cell → m·n.

## Space: output vs extra
- Output = what you return (forced by the problem).
- Extra = everything else you create to help.
- Say both: "O(n) output, O(1) extra."
- A loop variable over rows (`for row in grid`) points at the row; it doesn't copy it → O(1).

## Hidden loops (look like one step, aren't)
- `x in list` → O(n)
- `sum(list)`, `max(list)`, `min(list)` → O(n)
- `list[a:b]` → O(b−a) time and space (copies)
- `a + b` on lists → O(len(a) + len(b)), new list
- `[0] * n` → O(n)
- But `max(a, b)` on two numbers → O(1)

## Reading constraints
- n ≤ 1,000 → O(n²) fine.  n ≤ 10⁵ → need O(n log n) or O(n).
- Python ≈ 10⁷ simple ops per time limit.
- Check for negatives, zeros, empty input → these are your edge cases.

## Pattern: running variable (don't store everything)
- Keep one variable updated as you go instead of a list of all values.
- Running sum: `prev += nums[i]` (prefix sum, Day 1 · LC 1480).
- Running max: `best = max(best, current)` (Day 1 · LC 1672).
- Starting value for max: `float('-inf')` if negatives are possible.

## Pattern: filling a pre-made list by index
- `ans = [0] * size`, then write `ans[i]`.
- Can write two slots per step: `ans[i]` and `ans[i + n]` (Day 1 · LC 1929).