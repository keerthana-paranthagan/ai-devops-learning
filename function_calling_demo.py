def get_cluster_status():
    return "All 15 pods are healthy"

question = input("Ask: ")
if "cluster" in question.lower():
    result = get_cluster_status()

    print("Tool Result: ")
    print (result)
else:
    print("No matching tools found")