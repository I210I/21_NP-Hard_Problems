"""
    The 3-SAT problem is a well-known NP-complete problem in computer science and logic.
    It is a specific variation of the Boolean satisfiability problem (SAT) and involves 
    determining the satisfiability of a given boolean formula in conjunctive normal form (CNF).

    In the 3-SAT problem, the boolean formula consists of a conjunction (AND) of multiple 
    clauses, and each clause contains exactly three literals connected by a disjunction (OR).
    A literal represents a boolean variable or its negation.

    The goal of the 3-SAT problem is to determine if there exists an assignment of truth values 
    to the variables that satisfies the entire formula, making it evaluate to "true." If such an
    assignment exists, the formula is considered satisfiable; otherwise, if no such assignment
    exists, the formula is unsatisfiable.
"""

def is_satisfiable(clauses, assignment):
    for clause in clauses:
        x, y, z = clause
        if (x < 0 and not assignment[abs(x) - 1] or x > 0 and assignment[abs(x) - 1]) and \
           (y < 0 and not assignment[abs(y) - 1] or y > 0 and assignment[abs(y) - 1]) and \
           (z < 0 and not assignment[abs(z) - 1] or z > 0 and assignment[abs(z) - 1]):
            return True
    return False

def solve_3sat(clauses):
    num_vars = max(abs(x) for clause in clauses for x in clause)
    for i in range(2 ** num_vars):
        assignment = [bool((i >> j) & 1) for j in range(num_vars)]
        if is_satisfiable(clauses, assignment):
            return True
    return False

# Example usage:
clauses = [(1, -2, 3), (-1, 2, -3), (1, 2, 3)]
result = solve_3sat(clauses)
print("Satisfiable" if result else "Unsatisfiable")
