def valid(closetoopen = closetoopen, s = s, stack = stack):
  for i in s[0]:
    if i in closetoopen:
      if stack and closetoopen[i] == stack[-1]:
        stack.pop(-1)
      else:
        return False
    else:
      stack.append(i)

  return True if not stack else False
