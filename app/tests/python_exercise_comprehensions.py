tests = [
    {"name":"login", "status":"passed"},
    {"name":"logout", "status":"failed"},
    {"name":"search", "status":"passed"},
    {"name":"checkout", "status":"failed"},
]


results = [result for result in tests if result["name"] in {"checkout", "search"}]
print(results)


results = [result["name"] for result in tests if result["name"] in {"checkout", "search"}]
print(results)


status_results = {result["status"]: result["name"] for result in tests if result["name"] in {"checkout", "search"}}
print(status_results)

status_failed = {result["name"]: result["status"] for result in tests if result["status"] in {"failed"}}
print("status_failed:", status_failed)

print(type(results))

a = 1
b = 0
result = a/b
print(result)