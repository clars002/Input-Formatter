import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        type=str,
        default="input/optdigits-orig.txt",
        help="Input file to be formatted.",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    inp = open("output/predictors.txt", "w")
    lab = open("output/responses.txt", "w")

    with open(args.input) as input_file:
        text = input_file.readlines()
        for line in text:
            line = line.rstrip()
            if line[0] == " ":
                rep = [None] * 10
                num = line[1]
                num_int = int(line[1])
                rep[num_int] = "1"
                for char in rep:
                    if char == None:
                        char = "0"
                    lab.write(char + " ")
                lab.write("\n")
                inp.write("\n")
            else:
                for i in range(len(line)):
                    inp.write(line[i] + " ")

    inp.close()
    lab.close()


if __name__ == "__main__":
    main()
