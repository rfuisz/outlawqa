import sys
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()


# Add the path to the submodules/paper-qa directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'submodules', 'paper-qa')))

# Now import from paperqa
from paperqa import Settings, ask



def main():
    answer = ask(
        "What manufacturing challenges are unique to bispecific antibodies?",
        settings=Settings( paper_directory="downloaded_papers"),
    )

main()
