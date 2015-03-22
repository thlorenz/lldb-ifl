# adds gdb "info registers eflags" feature to lldb

import lldb

# See: http://en.wikipedia.org/wiki/FLAGS_register
#         0     1   2     3   4     5   6     7     8     9     10    11    12      13      14    15  16    17    18    19     20     21
FLAGS = [ 'CF', '', 'PF', '', 'AF', '', 'ZF', 'SF', 'TF', 'IF', 'DF', 'OF', 'IOPL', 'IOPL', 'NT', '', 'RF', 'VM', 'AC', 'VIF', 'VIP', 'ID' ]

def ifl(debugger, command, result, internal_dict):
  ci = debugger.GetCommandInterpreter()
  res = lldb.SBCommandReturnObject()
  ci.HandleCommand('register read --format b rflags', res)
  flags = str(res.GetOutput())[::-1].strip()
  syms = []
  for i in range(0,21):
    if flags[i] == '1' and FLAGS[i] != '': syms.append(FLAGS[i])

  res = lldb.SBCommandReturnObject()
  ci.HandleCommand('register read --format x rflags', res)
  print('rflags: %s %s' % (res.GetOutput()[11:-1], str(syms)))


def __lldb_init_module(debugger, internal_dict):
  debugger.HandleCommand('command script add -f ifl.ifl ifl')
