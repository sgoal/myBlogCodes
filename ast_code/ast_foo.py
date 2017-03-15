import ast
from copy import copy

assign_foo = ast.Name(id='foo',ctx=ast.Store())
two = ast.Num(n=2)

# assign_2 = ast.Assign(targets=[copy(assign_foo)],value=copy(two))
# assign_2.lineno = 1
# assign_2.col_offset = 0
# ast.fix_missing_locations(assign_2)


use_foo = ast.Name(id='foo',ctx = ast.Load()) 

if_ = ast.If()
if_.test = ast.Compare() 
if_.test.left = copy(use_foo)
if_.test.ops = [ast.Eq()]
if_.test.comparators = [copy(two)]

if_.body = [ast.Print(dest=None,values=[copy(use_foo)],nl=True)]
if_.orelse = [ast.Print(dest=None,values=[ast.Str(s="not equal")],nl=True)]

if_.lineno = 2
if_.col_offset = 0
ast.fix_missing_locations(if_)

mod = ast.Module(body = [assign_2,if_])

code = compile(mod,'<test>','exec')
exec code

print ast.dump(mod,include_attributes = True)
