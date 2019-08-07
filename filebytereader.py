import sys


def main():

    print("--------------------")
    print("| codedrome.com    |")
    print("| File Byte Reader |")
    print("--------------------\n")

    if len(sys.argv) != 2:
        print("input file must be specified")
    else:
        read_file(sys.argv[1])


def read_file(filepath):

    """
    Opens the specified text file and outputs details of each ASCII character, one per line.
    """

    mappings = populate_mappings()

    i = 1

    try:

        print("------------------------------------------------------")
        print("| Pos   | Code | Printable  | Character              |")
        print("------------------------------------------------------")

        fin = open(filepath, "r")

        while True:
            c = fin.read(1)
            if not c:
                break

            if ord(c) >= 0 and ord(c) <= 127:

                print("| {:<5d} | {:<4d} | {:10s} | {:22} |".format(i, ord(c), str(c.isprintable()), mappings[ord(c)]))

            else:

                print("| {:<5d} | {:<4d} | {:10s} | {:22} |".format(i, ord(c), str(c.isprintable()), "[Outside ASCII range]"))

            i += 1

        print("------------------------------------------------------")

        fin.close()

    except IOError as ioe:

        print(str(ioe))


def populate_mappings():

    """
    Creates a list indexed by ASCII codes of either printable
    characters or descriptions of non-printable characters.
    """

    mappings = []

    for i in range(0, 128):

        mappings.append(chr(i))

    # replace non-printable characters with descriptions
    mappings[0] = "[null]"
    mappings[1] = "[start of heading]"
    mappings[2] = "[start of text]"
    mappings[3] = "[end of text]"
    mappings[4] = "[end of transmission]"
    mappings[5] = "[enquiry]"
    mappings[6] = "[acknowledge]"
    mappings[7] = "[bell]"
    mappings[8] = "[backspace]"
    mappings[9] = "[tab]"
    mappings[10] = "[line feed]"
    mappings[11] = "[vertical tab]"
    mappings[12] = "[form feed]"
    mappings[13] = "[carriage return]"
    mappings[14] = "[shift out]"
    mappings[15] = "[shift in]"
    mappings[16] = "[data link escape]"
    mappings[17] = "[device control 1]"
    mappings[18] = "[device control 2]"
    mappings[19] = "[device control 3]"
    mappings[20] = "[device control 4]"
    mappings[21] = "[negative acknowledge]"
    mappings[22] = "[synchronous idle]"
    mappings[23] = "[end of trans. block]"
    mappings[24] = "[cancel]"
    mappings[25] = "[end of medium]"
    mappings[26] = "[substitute]"
    mappings[27] = "[escape]"
    mappings[28] = "[file separator]"
    mappings[29] = "[group separator]"
    mappings[30] = "[record separator]"
    mappings[31] = "[unit separator]"
    mappings[32] = "[space]"
    mappings[127] = "[delete]"

    return mappings


main()
