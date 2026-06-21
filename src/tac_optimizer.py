import re


class TACOptimizer:
    def optimize(self, code):
        optimized = []

        for line in code:
            folded = self._fold_constants(line)
            simplified = self._simplify_neutral_ops(folded)

            if not self._is_useless_assignment(simplified):
                optimized.append(simplified)

        return optimized

    def print_code(self, code):
        for line in code:
            print(line)

    def _fold_constants(self, line):
        # Calcula operacoes com dois literais numericos ainda no codigo intermedio.
        match = re.fullmatch(r"(\w+) = (-?\d+(?:\.\d+)?) ([+\-*/%<>=!&|]+) (-?\d+(?:\.\d+)?)", line.strip())
        if not match:
            return line

        target, left, op, right = match.groups()
        result = self._eval_binary(left, op, right)

        if result is None:
            return line

        return f"{target} = {result}"

    def _simplify_neutral_ops(self, line):
        # Remove operacoes neutras simples para reduzir temporarios obvios.
        patterns = [
            (r"(\w+) = (\w+) \+ 0$", r"\1 = \2"),
            (r"(\w+) = 0 \+ (\w+)$", r"\1 = \2"),
            (r"(\w+) = (\w+) - 0$", r"\1 = \2"),
            (r"(\w+) = (\w+) \* 1$", r"\1 = \2"),
            (r"(\w+) = 1 \* (\w+)$", r"\1 = \2"),
            (r"(\w+) = (\w+) / 1$", r"\1 = \2"),
            (r"(\w+) = (\w+) \* 0$", r"\1 = 0"),
            (r"(\w+) = 0 \* (\w+)$", r"\1 = 0"),
        ]

        stripped = line.strip()
        for pattern, repl in patterns:
            if re.fullmatch(pattern, stripped):
                return re.sub(pattern, repl, stripped)

        return line

    def _is_useless_assignment(self, line):
        # Descarta atribuicoes do tipo x = x, que nao alteram o programa.
        match = re.fullmatch(r"(\w+) = \1", line.strip())
        return match is not None

    def _eval_binary(self, left, op, right):
        left_value = float(left) if "." in left else int(left)
        right_value = float(right) if "." in right else int(right)

        try:
            if op == "+":
                return self._format_number(left_value + right_value)
            if op == "-":
                return self._format_number(left_value - right_value)
            if op == "*":
                return self._format_number(left_value * right_value)
            if op == "/" and right_value != 0:
                return self._format_number(left_value / right_value)
            if op == "%" and right_value != 0:
                return self._format_number(left_value % right_value)
            if op == "<":
                return int(left_value < right_value)
            if op == "<=":
                return int(left_value <= right_value)
            if op == ">":
                return int(left_value > right_value)
            if op == ">=":
                return int(left_value >= right_value)
            if op == "==":
                return int(left_value == right_value)
            if op == "!=":
                return int(left_value != right_value)
            if op == "&&":
                return int(bool(left_value) and bool(right_value))
            if op == "||":
                return int(bool(left_value) or bool(right_value))
        except ZeroDivisionError:
            return None

        return None

    def _format_number(self, value):
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return value
