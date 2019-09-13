def print_nice(obj, name=True):
	try:
		import inspect
	except:
		print("could not import 'inspect' module")
		return
	if name:
		callers_local_vars = inspect.currentframe().f_back.f_locals.items()
		get_name = [var_name for var_name, var_val in callers_local_vars if var_val is obj]
		print("\n\n\n%s:%s\n\n\n"%(get_name, obj))
	else:
		print("\n\n\n%s\n\n\n"%(obj))
	return