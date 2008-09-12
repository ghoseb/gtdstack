#!/usr/bin/env python

# GTD Stack

import pickle 
import sys

class GTDStack:
	def __init__(self):
		self.stack = []
	
	def getTasks(self):
		temp = self.stack[:]
		temp.reverse()
		return temp
	
	def addTask(self, task):
		if len(task.strip()) > 0:
			self.stack.append(task)	
			
	def getNextTask(self):
		try:
			return self.stack.pop()
		except IndexError:
			return None
	
	def do(self, number):
		task = self.stack[number-1]
		del self.stack[number-1]
		return task
	
	def save(self):
		outfile = open("saved.data","w+")
		pickle.dump(self.stack, outfile)
		outfile.close()

	def load(self):
		infile = open("saved.data","r+")
		temp = pickle.load(infile)
		for task in self.stack:
			temp.append(task)
		self.stack  = temp
		infile.close()

def main():
	stack = GTDStack()
	current_task = ""
	
	while True:
		try:
			input = raw_input("> ")
			cmd = input.split(" ")[0]
			task = ' '.join(input.split(" ")[1:])

			if cmd == "a":
				task = task.strip()
				
				if len(task) > 0:
					
					if len(current_task) > 0:
						stack.addTask(current_task)
						
					current_task = task
					print "Now working on: %s." % task
					
				else:
					print "Working on mystery task? (try h for help)"
					
			elif cmd == "c":
				print "Current Task: %s" % current_task
				
			elif cmd == "n":
				task = stack.getNextTask()
				
				if task != None:
					print "Continuing work on: %s." % task
				else:
					print "Relax!"
					
			elif cmd == "l":
				tasks = stack.getTasks()
				print current_task
				print "--------------------"
				
				if tasks != None and len(tasks) > 0:
					x = len(tasks)
					
					for task in tasks:
						print x, task
						x -= 1
						
				else:
					print "No pending tasks!"

			elif cmd == "do":
				stack.addTask(current_task)
				current_task = stack.do(int(task))
				print "Continuing work on: %s." % current_task

			elif cmd == "save":
				stack.addTask(current_task)
				stack.save()

			elif cmd == "load":
				stack.load()

			elif cmd == "q":
				sys.exit()
				
			else:
				print """Commands:
				a <task> : add a new task
				c : current task
				n : get next task to work with
				l : list of tasks
				do <task number> : select a task from the list to do right now
				save : to save the current tasks on disk
				load : to load previously saved tasks from disk
				q : quit
				"""
				
		except KeyboardInterrupt:
			print "Bye"
			sys.exit()
		

if __name__ == "__main__":
	main()