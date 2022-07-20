"""
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

Good question!
Topological sorting: topological sorting of all recipes + ingredients
Kahn's algorithm, add supplies to the queue
ingredient/recipe -> recipe
{
    "yeast": ["bread"],
    "flour": ["bread"],
    "bread": ["sandwich"],
    "meat": ["sandwich"]
}

Can we use the classic DFS topological sort?
No. The classic DFS topological sort does not allow us to have only "n starting points". All the nodes with indegree=0 have to be the starting point. In Kahn we can enforce "n starting points" by putting n nodes into the queue to start with.
"""
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        for i,ingredient in enumerate(ingredients):
            for item in ingredient:
                if item not in graph:
                    graph[item] = []
                graph[item].append(recipes[i])
        
        indegrees = {}
        for i,recipe in enumerate(recipes):
            indegrees[recipe] = len(ingredients[i])
                
        queue = deque()
        result = []
        queue.extend(supplies)
        
        while queue:
            ingredient = queue.popleft()
            if ingredient in graph:
                for recipe in graph[ingredient]:
                    indegrees[recipe] -= 1
                    if indegrees[recipe] == 0:
                        result.append(recipe)
                        queue.append(recipe)
                        
        return result