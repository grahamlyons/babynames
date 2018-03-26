from argparse import ArgumentParser

from babynames.client import Client
from babynames.parser import Parser

argparser = ArgumentParser(prog = "babynames")
argparser.add_argument("name", type=str,
                   help="The boy's baby name to search for")
argparser.add_argument("start_year", type=int,
                   help="The year to start searching from")
argparser.add_argument("end_year", type=int,
                   help="The year to start searching from")

_client = Client()

OUTPUT_TEMPLATE = "Between {start_year} and {end_year}\
 the total number of male children named {name} was {count}"

def _client_post(year):
    return _client.post(year, 1000, "n")

def get_male_counts(year):
    data = _client_post(year)
    parser = Parser(data)
    return parser.get_male_counts()

def get_count_for_name(name, start_year, end_year):
    data = (get_male_counts(y) for y in range(start_year, end_year + 1))
    return sum(d.get(name, 0) for d in data)

def main():
    args = argparser.parse_args()
    count = get_count_for_name(args.name, args.start_year, args.end_year)
    output_vars = {
        "start_year": args.start_year,
        "end_year": args.end_year,
        "name": args.name,
        "count": count
    }
    print(OUTPUT_TEMPLATE.format(**output_vars))

if __name__ == "__main__":
    main()
