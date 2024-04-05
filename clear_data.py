import pandas as pd
import json


def clear_none(f):
    df = pd.read_csv(f)
    df = df[df.developer_a != '(none)']
    df = df[df.developer_b != '(none)']
    df.to_csv(f, index=False, header=True)


def clear_email(f):
    with open('email_map.json', 'r') as fi:
        d = json.load(fi)
    df = pd.read_csv(f)
    df['developer_a'] = df['developer_a'].replace(d)
    df['developer_b'] = df['developer_b'].replace(d)
    df.to_csv(f, index=False, header=True)


def clear_zero(f):
    df = pd.read_csv(f)
    df = df[df.weight != 0]
    df.to_csv(f, header=True, index=False)
