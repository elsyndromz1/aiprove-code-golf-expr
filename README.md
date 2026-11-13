# code-golf-expr — AIProve entry

`expr.py` exposes `evaluate(expr)` for `+ - * /`, decimal numbers,
parentheses, unary `+`/`-`, and surrounding whitespace.

- 311 bytes, no `eval`/`exec`, stdlib only (`ast`, `operator`).
- The parser is `ast.parse` — it only parses, it never executes code.
  The tree is then walked by hand: constants, unary minus/plus,
  and `Add`/`Sub`/`Mult`/`Div` via `operator`.
- Verified: 9/9 public cases, 23/23 extended cases (unary, spaces,
  `.5`, nested parens), and ~3,000 random expressions vs `eval` as
  oracle — all matching.

Test: `python3 -c "from expr import evaluate; print(evaluate('1+2*3'))"`
