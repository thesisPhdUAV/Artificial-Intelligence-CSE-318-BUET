from collections import defaultdict

# from State import TERMINAL_STATE, INITIAL_STATE
from State import TERMINAL_STATE
# from Constants import TERMINAL_STATE, INITIAL_STATE


listStates = []


# This class represents a directed graph
# using adjacency list representation 
class Graph:

	def __init__(self):

		# default dictionary to store graph
		self.exploredDFS = 0
		self.bfs_path = None
		self.graph = defaultdict(list)
		self.bfs_parent = defaultdict(list)
		self.dfs_parent = {}
		self.expandedBFS = 0
		self.exploredBFS = 0

	def addEdge(self, u, v):
		if not u in self.graph.keys():
			self.graph[u] = []
		self.graph[u].append(v)

	def BFS(self, s):
		visited = defaultdict(list)
		for u in listStates:
			visited[u] = False

		queue = [s]

		visited[s] = True
		self.bfs_parent[s] = None
		s.level = 0

		self.exploredBFS = 1

		while queue:
			self.expandedBFS += 1

			u = queue.pop(0)

			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				# print("No of Explored Nodes: " + str(visited.__len__()))
				print("No of Explored Nodes: " + str(self.exploredBFS))
				queue.clear()
				self.bfs_parent[TERMINAL_STATE] = u
				return self.bfs_parent

			for v in u.successors():
				if not visited[v]:
					self.bfs_parent[v] = u
					v.level = u.level + 1
					queue.append(v)
					visited[v] = True
					self.exploredBFS += 1
		# else:
		# print(" -> ",end=" ");
		# print(v)

		self.bfs_parent = {}
		return []

	def DFS(self, start):
		visited = defaultdict(list)
		for u in listStates:
			visited[u] = False

		visited[start] = True
		self.dfs_parent[start] = None
		stack = [start]

		while stack:
			u = stack.pop()
			if u.isGoalState():
				print("No of Expanded Nodes: " + str(self.exploredDFS))
				self.dfs_parent[TERMINAL_STATE] = u
				stack.clear()
				# print(self.dfs_parent)
				return self.dfs_parent
			# if v not in path:
			# 	path.append(v)
			for v in u.successors():
				if not visited[v]:
					self.exploredDFS += 1
					visited[v] = True
					self.dfs_parent[v] = u
					stack.append(v)
		return {}

	def print(self):
		for u in listStates:
			print(u, end=" -> ")
			print(self.graph[u])

	def printPath(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		self.printPath(parentList, parentList[tail])
		if tail != TERMINAL_STATE: print(tail)

	def printPathL(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		if tail == TERMINAL_STATE: tail = parentList[tail]

		stack = []

		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]
		# stack.append(tail)

		while stack:
			print(stack.pop())
# print(g.bfs_path)
# This code is contributed by Neelam Yadav