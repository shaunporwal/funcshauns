import subprocess

def get_repo_root():
    """
    Get the root directory of the current Git repository.

    This function runs the `git rev-parse --show-toplevel` command to determine
    the root directory of the current Git repository. If the command is successful,
    it returns the path to the root directory as a string. If the command fails
    (e.g., if the current directory is not part of a Git repository), it returns None.

    Returns:
        str: The root directory of the current Git repository, or None if not in a Git repository.
    """
    try:
        repo_root = subprocess.check_output(
            ['git', 'rev-parse', '--show-toplevel'],
            stderr=subprocess.DEVNULL
        ).strip().decode('utf-8')
        return repo_root
    except subprocess.CalledProcessError:
        return None  # Not in a Git repository
