from typing import List
import yaml
import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

@CrewBase
class IdeaParaphraseRefinement():
    """Crew to refine and paraphrase user-submitted ideas through a multi-agent workflow."""

    agents: List[BaseAgent]
    tasks: List[Task]

    def load_knowledge_sources(self):
        """Load Markdown knowledge sources from kb.yaml."""
        with open(r"src\idea_paraphrase_refinement\config\kb.yaml", "r", encoding="utf-8") as file:
            kb_config = yaml.safe_load(file)
        knowledge = {}
        kb_sources = []
        for source in kb_config.get("knowledge_base_sources", []):
            if os.path.exists(source["path"]):
                with open(source["path"], "r", encoding="utf-8") as md_file:
                    knowledge[source["name"]] = md_file.read()
                    kb_sources.append(StringKnowledgeSource(content=knowledge[source["name"]]))
            else:
                knowledge[source["name"]] = f"Error: Markdown file {source['path']} not found."
        return knowledge, kb_sources

    @agent
    def content_moderator(self) -> Agent:
        """Detects offensive, aggressive, or harmful phrasing in the input idea and refines the tone."""
        return Agent(
            config=self.agents_config['content_moderator'],  # type: ignore[index]
            verbose=True
        )

    @task
    def detect_offensive_language_task(self) -> Task:
        """Detects offensive, harmful, or aggressive phrasing in the input idea."""
        return Task(
            config=self.tasks_config['detect_offensive_language_task'],
            agent=self.content_moderator()
        )

    @task
    def mitigate_tone_task(self) -> Task:
        """Rephrases flagged segments into respectful, inclusive language."""
        return Task(
            config=self.tasks_config['mitigate_tone_task'],
            agent=self.content_moderator(),
            context=[self.detect_offensive_language_task()]
        )

    @agent
    def clarity_simplifier(self) -> Agent:
        """Simplifies complex sentences into clearer, shorter units."""
        return Agent(
            config=self.agents_config['clarity_simplifier'],
            verbose=True
        )

    @task
    def split_and_rephrase_task(self) -> Task:
        """Simplifies complex sentences for better understanding."""
        return Task(
            config=self.tasks_config['split_and_rephrase_task'],
            agent=self.clarity_simplifier(),
            context=[self.mitigate_tone_task()]
        )

    @agent
    def essence_preserver(self) -> Agent:
        """Preserves the core meaning and key points during refinement."""
        return Agent(
            config=self.agents_config['essence_preserver'],
            verbose=True
        )

    @task
    def key_point_extractor_task(self) -> Task:
        """Extracts and ranks the most important key points from the idea."""
        return Task(
            config=self.tasks_config['key_point_extractor_task'],
            agent=self.essence_preserver(),
            context=[self.split_and_rephrase_task()]
        )

    @task
    def preserve_semantic_meaning_task(self) -> Task:
        """Ensures the core message and key points are preserved across refinements."""
        return Task(
            config=self.tasks_config['preserve_semantic_meaning_task'],
            agent=self.essence_preserver(),
            context=[self.split_and_rephrase_task(), self.key_point_extractor_task()]
        )

    @agent
    def relevance_assessor(self) -> Agent:
        """Evaluates how relevant the idea is to the original topic."""
        return Agent(
            config=self.agents_config['relevance_assessor'],
            verbose=True
        )

    @task
    def relevance_evaluator_task(self) -> Task:
        """Checks the alignment of the refined idea with the original topic."""
        return Task(
            config=self.tasks_config['relevance_evaluator_task'],
            agent=self.relevance_assessor(),
            context=[self.split_and_rephrase_task(), self.key_point_extractor_task()]
        )

    @task
    def clarity_refiner_task(self) -> Task:
        """Final refinement of the idea for grammar, clarity, and tone."""
        return Task(
            config=self.tasks_config['clarity_refiner_task'],
            agent=self.clarity_simplifier(),
            context=[self.split_and_rephrase_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the complete paraphrasing and refinement crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=self.load_knowledge_sources()[1],
        )
