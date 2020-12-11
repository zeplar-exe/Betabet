list:
## if no datatype is provided, any type can be inserted into the list

list(datatype, size = n) myList = [object1, object2]
list.cut(start, end) ## cuts everything before start, and after end

list(int, size = 8) nums = [1, 2, 10, 15, 100, 200, 900, 3090]
nums.cut(3, 5) ## nums now only contains 15, 100, and 200

function:

## No datatype represents no return

datatype foo : arg1, arg2 {
	## content
}

int add : a, b {
	return (a + b)
}

process:

foo : bar, varadic = {...} {
	bar(tuple(varadic))
}
## runs bar, a function, with the given parameters (varadic)

int n = 5
process proc = process(arg1, arg2) { return str(arg1) + str(arg2) }

foo(proc, n, 5)
## process allows functions to be used as parameters without being predefined.
