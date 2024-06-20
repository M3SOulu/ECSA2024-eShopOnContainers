import sys
import pandas as pd
import json


def clear_none(i, o):
    df = pd.read_csv(i)
    df = df[df.developer_a != '(none)']
    df = df[df.developer_b != '(none)']
    df.to_csv(o, index=False, header=True)


def clear_email(i, o, email_map):
    with open(email_map, 'r') as fi:
        d = json.load(fi)
    df = pd.read_csv(i)
    df['developer_a'] = df['developer_a'].replace(d)
    df['developer_b'] = df['developer_b'].replace(d)
    df.to_csv(o, index=False, header=True)


if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    email_map = sys.argv[3]
    clear_none(input, output)
    clear_email(output, output, email_map)

