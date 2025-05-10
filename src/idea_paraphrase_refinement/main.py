#!/usr/bin/env python
"""Module Doc"""
import sys
import warnings

from datetime import datetime

from idea_paraphrase_refinement.crew import IdeaParaphraseRefinement

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {"topic": "Coronavirus Origins",
              "idea": "The coronavirus was"
              "clearly made in a lab by some irresponsible scientists"
              "who didn’t care how much damage they’d cause. And let’s be honest,"
              "people who ignore basic hygiene and travel rules are part of why it"
              "spread like wildfire. Some countries just lied and covered things up"
              "while the rest of us suffered."}

    try:
        IdeaParaphraseRefinement().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise RuntimeError(f"An error occurred while running the crew: {e}") from e


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}
    try:
        IdeaParaphraseRefinement().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise RuntimeError(f"An error occurred while training the crew: {e}") from e


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IdeaParaphraseRefinement().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise RuntimeError(f"An error occurred while replaying the crew: {e}") from e


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs", "current_year": str(datetime.now().year)}

    try:
        IdeaParaphraseRefinement().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise RuntimeError(f"An error occurred while testing the crew: {e}") from e
