from crewai import Crew, Process

from agents import (data_researcher, humanizer_agent, telegram_post_writer,
                    translator_agent)
from config.core import config
from tasks import find_data, humanizing_task, post_writing, translation_task


if __name__ == "__main__":

    crew = Crew(
        agents=[data_researcher, telegram_post_writer,
                humanizer_agent, translator_agent],
        tasks=[find_data, post_writing, humanizing_task, translation_task],
        process=Process.sequential,
        verbose=True
    )
    post_content = crew.kickoff(inputs={"topic": config.topic})
