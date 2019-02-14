import argparse


parser = argparse.ArgumentParser(description='Powiedz: Witam Serdecznie Pana --name')
parser.add_argument('--name', type=str, help='Twoje imie prosze Pana!')
parser.add_argument('--powitanie', type=str, help='Powitanie str')


args = parser.parse_args()

print(args.powitanie + args.name)