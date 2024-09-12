from crewai import Task

from agents import (data_researcher, humanizer_agent, telegram_post_writer,
                    translator_agent)
from config.core import config
from config.prompts import prompts


find_data = Task(
    description=prompts.explorer.prompt,
    expected_output=prompts.explorer.expected_output,
    agent=data_researcher,
)

post_writing = Task(
    description=prompts.writer.prompt,
    expected_output=prompts.writer.expected_output,
    agent=telegram_post_writer,
)

humanizing_task = Task(
    description=prompts.humanizer.prompt,
    expected_output=prompts.humanizer.expected_output,
    agent=humanizer_agent
)

translation_task = Task(
    description=prompts.translator.prompt,
    expected_output=prompts.translator.expected_output,
    tools=[],
    agent=translator_agent,
    output_file=config.output_file
)
