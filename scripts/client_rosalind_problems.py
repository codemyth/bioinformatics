"""client file to call functions from other modules."""

# from rosalind.problems import group_one
from main.rosalind import rosalind_problems


def main():
    """Main method serving as the entry point to the script file."""
    rosalind_problems.main()

if __name__ == "__main__":
    main()
