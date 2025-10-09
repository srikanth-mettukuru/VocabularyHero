from crewai import Task

def get_writer_task(agent):
    return Task(
        description=(
            "Using the vocabulary words from the previous task, write a short story (150-200 words) "
            "suitable for grade {grade_level} students. Make sure to use all the generated words naturally "
            "in the context of the story."
        ),
        expected_output="A cohesive story that naturally uses all provided words.",
        agent=agent
    )
