"""
Public module for checking student CoNLL-U files.
"""

import sys
from pathlib import Path

from config.cli_unifier import _run_console_tool, choose_python_exe
from config.console_logging import get_child_logger

logger = get_child_logger(__file__)


def check_via_official_validator(conllu_path: Path) -> tuple[str, str, int]:
    """
    Run validator checks for the project.

    URL: https://github.com/UniversalDependencies/tools/blob/master/validate.py

    Args:
        conllu_path: Path to conllu file

    Returns:
        subprocess.CompletedProcess: Program execution values
    """
    validator_args = [
        str(Path(__file__).parent / "ud_validator" / "validate.py"),
        "--lang",
        "ru",
        "--max-err",
        "0",
        "--level",
        "2",
        str(conllu_path),
    ]
    return _run_console_tool(str(choose_python_exe()), validator_args, debug=True)


def main() -> None:
    """
    Module entrypoint.
    """
    if len(sys.argv) < 2:
        logger.info("Provide path to the file to check.")
        sys.exit(1)
    conllu_path = Path(sys.argv[1])
    if not conllu_path.exists():
        logger.info("Total CONLLU file is not present. Analyze first.")
        sys.exit(1)

    _, _, return_code = check_via_official_validator(conllu_path=conllu_path)
    if return_code != 0:
        logger.info("Check failed.")
        sys.exit(1)
    else:
        logger.info("Check passed.")


if __name__ == "__main__":
    main()
