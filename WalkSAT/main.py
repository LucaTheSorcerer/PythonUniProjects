import random

def gsat(formula, max_iterations, p=0.5, cooling_rate=0.99):
    n = len(formula.variables)
    current_assignment = [random.choice([True, False]) for _ in range(n)]
    best_assignment = current_assignment.copy()
    best_satisfied_clauses = formula.evaluate(best_assignment)

    temperature = 1.0
    for i in range(max_iterations):
        variable_to_flip = random.randint(0, n-1)
        current_assignment[variable_to_flip] = not current_assignment[variable_to_flip]
        current_satisfied_clauses = formula.evaluate(current_assignment)

        delta = current_satisfied_clauses - best_satisfied_clauses
        if delta > 0 or random.random() < p:
            best_assignment = current_assignment.copy()
            best_satisfied_clauses = current_satisfied_clauses

        if best_satisfied_clauses == len(formula.clauses):
            return best_assignment

        temperature *= cooling_rate
    return None


class SATFormula:
    def __init__(self, clauses, variables):
        self.clauses = clauses
        self.variables = variables

    def evaluate(self, assignment):
        satisfied_clauses = 0
        for clause in self.clauses:
            for literal in clause:
                if literal < 0:
                    var = -literal
                    value = not assignment[var]
                else:
                    var = literal
                    value = assignment[var]
                if value:
                    satisfied_clauses += 1
                    break
        return satisfied_clauses


clauses = [[1, -2, 3], [-1, 2, -3], [1, -2, -3], [1, 2, -3]]
variables = [1, 2, 3]

formula = SATFormula(clauses, variables)


result = gsat(formula, max_iterations = 100)

if result is not None:
    print("Solution found: ", result)
else:
    print("No solution found.")