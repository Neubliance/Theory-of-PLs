from lang import *
from classes import *

import copy

clone = copy.deepcopy

impl = LambdaExpr([VarDecl("p", boolType), VarDecl("q", boolType)], OrExpr(NotExpr("p"), "q"))

table = [
  resolve(CallExpr(clone(impl), [True, True])),
  resolve(CallExpr(clone(impl), [True, False])),
  resolve(CallExpr(clone(impl), [False, True])),
  resolve(CallExpr(clone(impl), [False, False]))
]