import sys

class Log:
    def __init__(self):
        self.content = ""

    def debug(self, content):
        line = "##[debug] " + content
        self.content += line

    def write_to_file(self):
        with open("log.txt", "w") as f:
            f.write(self.content)


def main():
    log = Log()

    log.debug("Starting Script")

    log.debug( str(sys.argv[1:]) )

    log.write_to_file()


if __name__ == "__main__":
    main()