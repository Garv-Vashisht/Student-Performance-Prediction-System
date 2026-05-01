from src.simulate import generate_data
from src.train import train_model
from src.evaluate import evaluate
from src.utils import create_folders


def main():
    create_folders()

    generate_data()

    model, X_test, y_test = train_model()

    evaluate(model, X_test, y_test)


if __name__ == "__main__":
    main()