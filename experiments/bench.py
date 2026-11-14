import json

def main():
    with open('data/sample_vectors.json') as f:
        print(json.load(f))

if __name__ == '__main__':
    main()
