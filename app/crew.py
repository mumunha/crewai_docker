from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os
import app.settings

# Uncomment the following line to use an example of a custom tool
# from multicrew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them

os.environ["OPENAI_MODEL_NAME"]=app.settings.OPENAI_MODEL_NAME
os.environ["OPENAI_API_KEY"]=app.settings.OPENAI_API_KEY


@CrewBase
class MulticrewCrew():
	"""Multicrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			# llm=llm
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			# llm=llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.researcher(),
			# llm=llm
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.reporting_analyst(),
			output_file='app/report.md',
			# llm=llm
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Multicrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)