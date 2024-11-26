import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        type=str,
        default="input/optdigits-orig.txt",
        help="Input file to be formatted."
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    predictions = open("output/predictions.txt", "w")
    observations = open("output/observations.txt", "w")

    with open(args.input) as input_file:
        text = input_file.readlines()
        for line in text:
            line = line.rstrip()
            if line[0] == ' ':
                observations.write(line[1] + '\n')
                predictions.write('\n')
            else:
                for i in range(len(line)):
                    predictions.write(line[i] + ' ')

    predictions.close()
    observations.close()


# def process_line(str):
#     if line[0] == ' ':
        


if __name__ == "__main__":
    main()