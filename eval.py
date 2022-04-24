class Evaluator:
    def __init__(self, env: dict):
        self.env = env

    def eval(self, ast: list):
        if isinstance(ast, list):
            return self.eval_list(ast)
        else:
            return self.eval_atom(ast)