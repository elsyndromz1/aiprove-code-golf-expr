import ast as a,operator as o
def evaluate(e):
 f=lambda n:n.value if hasattr(n,'value') else (-f(n.operand) if type(n.op)==a.USub else f(n.operand)) if hasattr(n,'operand') else {a.Add:o.add,a.Sub:o.sub,a.Mult:o.mul,a.Div:o.truediv}[type(n.op)](f(n.left),f(n.right));return f(a.parse(e.strip()).body[0].value)
